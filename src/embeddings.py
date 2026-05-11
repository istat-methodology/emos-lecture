from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy import sparse


def load_embedding_model(model_name="paraphrase-multilingual-MiniLM-L12-v2", trust_remote_code=False):
    """
    Loads a multilingual sentence embedding model.

    Parameters:
        model_name: name of the sentence-transformers model
        trust_remote_code: whether to allow custom model code from Hugging Face

    Returns:
        SentenceTransformer model
    """

    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(model_name, trust_remote_code=trust_remote_code)


def compute_sentence_embeddings(texts, model):
    """
    Converts text into dense semantic embeddings.

    Parameters:
        texts: list or Series of text strings
        model: SentenceTransformer model

    Returns:
        numpy array with one embedding per text
    """

    return model.encode(list(texts), convert_to_numpy=True, show_progress_bar=True)


def compute_tfidf_embeddings(query_texts, descriptor_texts, tokenizer=None):
    """
    Converts text into simple TF-IDF vectors.

    Parameters:
        query_texts: query text strings to classify
        descriptor_texts: descriptor text strings
        tokenizer: optional function used to split text into tokens

    Returns:
        tuple with query vectors and descriptor vectors
    """

    if tokenizer is None:
        vectorizer = TfidfVectorizer()
    else:
        vectorizer = TfidfVectorizer(tokenizer=tokenizer, token_pattern=None)

    all_texts = list(query_texts) + list(descriptor_texts)
    all_vectors = vectorizer.fit_transform(all_texts)

    n_queries = len(query_texts)
    query_vectors = all_vectors[:n_queries]
    descriptor_vectors = all_vectors[n_queries:]

    return query_vectors, descriptor_vectors


def compute_centroid_embeddings(descriptor_embeddings, descriptor_codes):
    """
    Averages descriptor embeddings to obtain one vector per target code.

    Parameters:
        descriptor_embeddings: embeddings for individual descriptor rows
        descriptor_codes: target code for each descriptor row

    Returns:
        tuple with target codes and centroid embeddings
    """

    codes = list(dict.fromkeys(descriptor_codes))
    centroid_rows = []

    for code in codes:
        indices = [index for index, value in enumerate(descriptor_codes) if value == code]
        centroid = descriptor_embeddings[indices].mean(axis=0)
        centroid_rows.append(np.asarray(centroid).ravel())

    centroid_matrix = np.vstack(centroid_rows)

    if sparse.issparse(descriptor_embeddings):
        centroid_matrix = sparse.csr_matrix(centroid_matrix)

    return codes, centroid_matrix
