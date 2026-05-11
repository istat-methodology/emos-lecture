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


def load_ateco_descriptors(path=None):
    """
    Loads short textual descriptors for ATECO target codes.

    Parameters:
        path: optional path to the ATECO descriptor CSV file

    Returns:
        DataFrame with ATECO code and descriptor text
    """

    if path is None:
        path = project_root() / "data" / "classification" / "ateco22_descriptors.csv"

    descriptors = pd.read_csv(path)
    descriptors = descriptors.rename(columns={"code": "ateco_code", "text": "descriptor"})
    descriptors["ateco_code"] = descriptors["ateco_code"].astype(str)
    descriptors["descriptor"] = descriptors["descriptor"].astype(str).str.strip()

    return descriptors


def load_ateco_classification(path=None):
    """
    Loads the official ATECO classification file.

    Parameters:
        path: optional path to the official ATECO classification CSV file

    Returns:
        DataFrame with official ATECO codes, titles, hierarchy, and notes
    """

    if path is None:
        path = project_root() / "data" / "classification" / "ateco22_classification.csv"

    classification = pd.read_csv(path)
    classification["CODICE"] = classification["CODICE"].astype(str).str.strip()
    classification["IT_TITOLO"] = classification["IT_TITOLO"].astype(str).str.strip()
    classification["GERARCHIA"] = classification["GERARCHIA"].astype(int)

    return classification
