import pandas as pd

from src.utils import project_root
from src.utils import format_ateco_code


def load_labelled_queries(path=None):
    """
    Loads the labelled queries used as examples to code.

    Parameters:
        path: optional path to the raw labelled query CSV file

    Returns:
        DataFrame with query text, query length, and true code
    """

    if path is None:
        path = project_root() / "data" / "raw" / "labelled_queries.csv"

    queries = pd.read_csv(path)
    queries["query"] = queries["query"].astype(str).str.strip()
    queries["n_words"] = queries["n_words"].astype(int)
    queries["true_code"] = queries["true_code"].apply(format_ateco_code)

    return queries


def load_teaching_sample(path=None):
    """
    Loads the small labelled query sample used in the notebook.

    Parameters:
        path: optional path to the teaching sample CSV file

    Returns:
        DataFrame with query text, query length, and true code
    """

    if path is None:
        path = project_root() / "data" / "sample" / "labelled_queries_sample.csv"

    sample = pd.read_csv(path)
    sample["query"] = sample["query"].astype(str).str.strip()
    sample["n_words"] = sample["n_words"].astype(int)
    sample["true_code"] = sample["true_code"].apply(format_ateco_code)

    return sample


def load_ateco_descriptors(path=None):
    """
    Loads short textual descriptors for ATECO target codes.

    Parameters:
        path: optional path to the ATECO descriptor CSV file

    Returns:
        DataFrame with ATECO code and descriptor text
    """

    if path is None:
        path = project_root() / "data" / "reference" / "ateco22_disentangled.csv"

    descriptors = pd.read_csv(path)
    descriptors = descriptors.rename(columns={"code": "ateco_code", "text": "descriptor"})
    descriptors["ateco_code"] = descriptors["ateco_code"].astype(str)
    descriptors["descriptor"] = descriptors["descriptor"].astype(str).str.strip()

    return descriptors


def create_teaching_sample(queries, min_words=3, sample_size=500, random_state=42):
    """
    Creates a small reproducible sample for classroom use.

    Parameters:
        queries: DataFrame returned by load_labelled_queries
        min_words: minimum number of words in a query
        sample_size: maximum number of rows to keep
        random_state: seed used for reproducible sampling

    Returns:
        DataFrame with a manageable set of labelled queries
    """

    sample = queries[queries["n_words"] >= min_words].copy()
    sample["true_code"] = sample["true_code"].apply(format_ateco_code)

    # Duplicated queries are useful in production data, but they make a teaching
    # notebook harder to read. Here each row is one distinct coding example.
    sample = sample.drop_duplicates(subset=["query", "true_code"])

    if len(sample) > sample_size:
        sample = sample.sample(sample_size, random_state=random_state)

    return sample.sort_values("query").reset_index(drop=True)
