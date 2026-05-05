import pandas as pd


def top_k_accuracy(predictions, k=1):
    """
    Computes Top-k accuracy for automatic coding results.

    Parameters:
        predictions: DataFrame with true_code and top_codes columns
        k: number of suggested codes to consider

    Returns:
        accuracy as a float between 0 and 1
    """

    correct = predictions.apply(
        lambda row: row["true_code"] in row["top_codes"][:k],
        axis=1,
    )
    return correct.mean()


def summarize_accuracy(predictions, ks=(1, 3, 5)):
    """
    Summarizes Top-k accuracy for several values of k.

    Parameters:
        predictions: DataFrame with true_code and top_codes columns
        ks: iterable of k values to evaluate

    Returns:
        DataFrame with one row per Top-k metric
    """

    rows = []
    for k in ks:
        rows.append({"metric": f"Top-{k} accuracy", "value": top_k_accuracy(predictions, k)})

    return pd.DataFrame(rows)


def get_error_examples(predictions, k=1, n=10):
    """
    Selects examples where the correct code is not among the Top-k suggestions.

    Parameters:
        predictions: DataFrame with true_code and top_codes columns
        k: number of suggested codes to consider
        n: maximum number of rows to return

    Returns:
        DataFrame with error examples
    """

    is_error = predictions.apply(
        lambda row: row["true_code"] not in row["top_codes"][:k],
        axis=1,
    )

    columns = ["query", "true_code", "predicted_code", "confidence", "top_codes"]
    return predictions.loc[is_error, columns].head(n)
