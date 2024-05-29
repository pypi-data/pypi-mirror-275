import itertools
import typing as t

import nltk.metrics
import numpy as np
from scipy.spatial import distance as scipy_dist
from spacy.language import Language as SpacyLanguage
from spacy.tokens import Token

from nlp_service import nlp_pb
from nlp_service.typing import NumpyMatrix, NumpyVector, SpacyObj, SpacyVector

__all__ = (
    "get",
    "get_spacy",
    "cosine",
    "angular",
    "dynamax_jaccard",
    "maxpool_jaccard",
    "dynamax_dice",
    "dynamax_otsuka",
    "edit",
    "jaccard",
)


# https://github.com/babylonhealth/fuzzymax/blob/master/similarity/fuzzy.py
def _fuzzify(s: NumpyMatrix, u: NumpyMatrix) -> NumpyVector:
    """
    Sentence fuzzifier.
    Computes membership vector for the sentence S with respect to the
    universe U
    :param s: list of word embeddings for the sentence
    :param u: the universe matrix U with shape (K, d)
    :return: membership vectors for the sentence
    """
    f_s: NumpyMatrix = np.dot(s, u.T)
    m_s: NumpyVector = np.max(f_s, axis=0)
    m_s: NumpyVector = np.maximum(m_s, 0, m_s)
    return m_s


def cosine(vec1: NumpyVector, vec2: NumpyVector) -> float:
    if np.any(vec1) and np.any(vec2):
        return t.cast(float, 1 - scipy_dist.cosine(vec1, vec2))

    return 0.0


def cosine_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    return t.cast(float, 1 - scipy_dist.cosine(obj1.vector.data, obj2.vector.data))


def angular(vec1: NumpyVector, vec2: NumpyVector) -> float:
    if vec1.any() and vec2.any():
        try:
            return (
                1.0
                - np.arccos(
                    np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
                )
                / np.pi
            )
        except Exception:
            pass

    return 0.0


def angular_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    return angular(t.cast(NumpyVector, obj1.vector), t.cast(NumpyVector, obj2.vector))


def dynamax_jaccard(x: NumpyMatrix, y: NumpyMatrix) -> float:
    """
    DynaMax-Jaccard similarity measure between two sentences
    :param x: list of word embeddings for the first sentence
    :param y: list of word embeddings for the second sentence
    :return: similarity score between the two sentences
    """
    u = np.vstack((x, y))
    m_x = _fuzzify(x, u)
    m_y = _fuzzify(y, u)

    m_inter: float = np.sum(np.minimum(m_x, m_y))
    m_union: float = np.sum(np.maximum(m_x, m_y))
    return m_inter / m_union


def dynamax_jaccard_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    vecs1 = _token_vectors(obj1)
    vecs2 = _token_vectors(obj2)

    return dynamax_jaccard(t.cast(NumpyVector, vecs1), t.cast(NumpyVector, vecs2))


def maxpool_jaccard(x: NumpyMatrix, y: NumpyMatrix) -> float:
    """
    MaxPool-Jaccard similarity measure between two sentences
    :param x: list of word embeddings for the first sentence
    :param y: list of word embeddings for the second sentence
    :return: similarity score between the two sentences
    """
    m_x: NumpyVector = np.max(x, axis=0)
    m_x: NumpyVector = np.maximum(m_x, 0, m_x)
    m_y: NumpyVector = np.max(y, axis=0)
    m_y: NumpyVector = np.maximum(m_y, 0, m_y)
    m_inter: float = np.sum(np.minimum(m_x, m_y))
    m_union: float = np.sum(np.maximum(m_x, m_y))
    return m_inter / m_union


def maxpool_jaccard_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    vecs1 = _token_vectors(obj1)
    vecs2 = _token_vectors(obj2)

    return maxpool_jaccard(t.cast(NumpyVector, vecs1), t.cast(NumpyVector, vecs2))


def dynamax_dice(x: NumpyMatrix, y: NumpyMatrix) -> float:
    """
    DynaMax-Dice similarity measure between two sentences
    :param x: list of word embeddings for the first sentence
    :param y: list of word embeddings for the second sentence
    :return: similarity score between the two sentences
    """
    u = np.vstack((x, y))
    m_x = _fuzzify(x, u)
    m_y = _fuzzify(y, u)

    f_inter = np.sum(np.minimum(m_x, m_y))
    m_x_card = np.sum(m_x)
    m_y_card = np.sum(m_y)
    return 2 * f_inter / (m_x_card + m_y_card)


def dynamax_dice_spacy(obj1, obj2) -> float:
    vecs1 = _token_vectors(obj1)
    vecs2 = _token_vectors(obj2)

    return dynamax_dice(t.cast(NumpyVector, vecs1), t.cast(NumpyVector, vecs2))


def dynamax_otsuka(x: NumpyMatrix, y: NumpyMatrix) -> float:
    """
    DynaMax-Otsuka similarity measure between two sentences
    :param x: list of word embeddings for the first sentence
    :param y: list of word embeddings for the second sentence
    :return: similarity score between the two sentences
    """
    u = np.vstack((x, y))
    m_x = _fuzzify(x, u)
    m_y = _fuzzify(y, u)

    m_inter = np.sum(np.minimum(m_x, m_y))
    m_x_card = np.sum(m_x)
    m_y_card = np.sum(m_y)
    return m_inter / np.sqrt(m_x_card * m_y_card)


def dynamax_otsuka_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    vecs1 = _token_vectors(obj1)
    vecs2 = _token_vectors(obj2)

    return dynamax_otsuka(t.cast(NumpyVector, vecs1), t.cast(NumpyVector, vecs2))


def fbow_jaccard_factory(u: NumpyMatrix):
    """
    Factory for building FBoW-Jaccard similarity measures
    with the custom universe matrix U
    :param u: the universe matrix U
    :return: similarity function
    """

    def u_jaccard(x: NumpyMatrix, y: NumpyMatrix) -> float:
        m_x = _fuzzify(x, u)
        m_y = _fuzzify(y, u)

        m_inter: float = np.sum(np.minimum(m_x, m_y))
        m_union: float = np.sum(np.maximum(m_x, m_y))
        return m_inter / m_union

    return u_jaccard


def edit(text1: str, text2: str) -> float:
    return dist2sim(nltk.metrics.edit_distance(text1, text2))


def edit_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    return edit(obj1.text, obj2.text)


def jaccard(set1: t.AbstractSet[str], set2: t.AbstractSet[str]) -> float:
    return dist2sim(nltk.metrics.jaccard_distance(set1, set2))


def jaccard_spacy(obj1: SpacyObj, obj2: SpacyObj) -> float:
    set1 = _token_set(obj1)
    set2 = _token_set(obj2)

    return jaccard(set1, set2)


def _token_set(obj: SpacyObj) -> set[str]:
    if isinstance(obj, Token):
        return set() if obj.is_stop else {obj.text}

    return {t.text for t in obj if not t.is_stop}


def _token_vectors(obj: SpacyObj) -> list[SpacyVector]:
    return [obj.vector] if isinstance(obj, Token) else [t.vector for t in obj]


def dist2sim(distance: float) -> float:
    return 1 / (1 + distance)


mapping: dict[nlp_pb.SimilarityMethod, t.Callable[[t.Any, t.Any], float]] = {
    nlp_pb.SimilarityMethod.UNSPECIFIED: cosine,
    nlp_pb.SimilarityMethod.COSINE: cosine,
    nlp_pb.SimilarityMethod.ANGULAR: angular,
    nlp_pb.SimilarityMethod.DYNAMAX_JACCARD: dynamax_jaccard,
    nlp_pb.SimilarityMethod.MAXPOOL_JACCARD: maxpool_jaccard,
    nlp_pb.SimilarityMethod.DYNAMAX_DICE: dynamax_dice,
    nlp_pb.SimilarityMethod.DYNAMAX_OTSUKA: dynamax_otsuka,
    nlp_pb.SimilarityMethod.EDIT: edit,
    nlp_pb.SimilarityMethod.JACCARD: jaccard,
}

spacy_mapping: dict[nlp_pb.SimilarityMethod, t.Callable[[t.Any, t.Any], float]] = {
    nlp_pb.SimilarityMethod.UNSPECIFIED: cosine_spacy,
    nlp_pb.SimilarityMethod.COSINE: cosine_spacy,
    nlp_pb.SimilarityMethod.ANGULAR: angular_spacy,
    nlp_pb.SimilarityMethod.DYNAMAX_JACCARD: dynamax_jaccard_spacy,
    nlp_pb.SimilarityMethod.MAXPOOL_JACCARD: maxpool_jaccard_spacy,
    nlp_pb.SimilarityMethod.DYNAMAX_DICE: dynamax_dice_spacy,
    nlp_pb.SimilarityMethod.DYNAMAX_OTSUKA: dynamax_otsuka_spacy,
    nlp_pb.SimilarityMethod.EDIT: edit_spacy,
    nlp_pb.SimilarityMethod.JACCARD: jaccard_spacy,
}


get = mapping.get
get_spacy = spacy_mapping.get


@SpacyLanguage.factory("similarity_factory")
class SimilarityFactory:
    def __init__(self, nlp, name, method):
        if method:
            self.func = spacy_mapping[method]

    def __call__(self, doc):
        if self.func:
            doc.user_hooks["similarity"] = self.func
            doc.user_span_hooks["similarity"] = self.func
            doc.user_token_hooks["similarity"] = self.func

        return doc


try:
    from gensim.models import KeyedVectors

    def _wmd_model(obj) -> tuple[list[str], list[SpacyVector]]:
        if isinstance(obj, Token):
            return ([], []) if obj.is_stop else ([obj.text], [obj.vector])

        return [t.text for t in obj if not t.is_stop], [
            t.vector for t in obj if not t.is_stop
        ]

    def _wmd(obj1, obj2) -> float:
        words1, vecs1 = _wmd_model(obj1)
        words2, vecs2 = _wmd_model(obj2)

        dim = max(vec.shape[0] for vec in itertools.chain(vecs1, vecs2))
        gensim_model = KeyedVectors(dim)
        gensim_model.add_vectors(words1 + words2, vecs1 + vecs2)

        return dist2sim(gensim_model.wmdistance(words1, words2))

    # TODO: Implement generic version `wmd` for use without spacy
    # mapping[nlp_pb.SimilarityMethod.SimilarityMethod.WMD] = wmd
    spacy_mapping[nlp_pb.SimilarityMethod.WMD] = _wmd


except ImportError:
    pass
