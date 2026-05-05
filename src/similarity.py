import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity_matrix(query_embeddings, target_embeddings):
    """
    Computes cosine similarity between queries and target code descriptors.

    Parameters:
        query_embeddings: array-like with one vector per query
        target_embeddings: array-like with one vector per target code

    Returns:
        similarity matrix with shape n_queries x n_target_codes
    """

    return cosine_similarity(query_embeddings, target_embeddings)


def get_top_k_predictions(similarity_matrix, target_codes, k=3):
    """
    Finds the most similar target codes for each query.

    Parameters:
        similarity_matrix: matrix returned by compute_similarity_matrix
        target_codes: list or Series of target codes matching the matrix columns
        k: number of suggestions to return for each query

    Returns:
        list of dictionaries with predicted codes and similarity scores
    """

    target_codes = list(target_codes)
    top_k_rows = []

    for row in similarity_matrix:
        best_indices = np.argsort(row)[::-1][:k]
        top_k_rows.append(
            {
                "predicted_codes": [target_codes[index] for index in best_indices],
                "similarity_scores": [float(row[index]) for index in best_indices],
            }
        )

    return top_k_rows


def add_predictions_to_queries(queries, top_k_predictions):
    """
    Adds prediction columns to the query DataFrame.

    Parameters:
        queries: DataFrame with labelled queries
        top_k_predictions: output of get_top_k_predictions

    Returns:
        DataFrame with predicted codes and similarity scores
    """

    predictions = queries.copy()
    predictions["top_codes"] = [item["predicted_codes"] for item in top_k_predictions]
    predictions["top_scores"] = [item["similarity_scores"] for item in top_k_predictions]
    predictions["predicted_code"] = predictions["top_codes"].apply(lambda codes: codes[0])
    predictions["confidence"] = predictions["top_scores"].apply(lambda scores: scores[0])

    return predictions
