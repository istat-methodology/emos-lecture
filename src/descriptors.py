from src.utils import format_ateco_code


def build_descriptors(descriptors, method="CONCAT"):
    """
    Builds descriptor text for the target coding level.

    Parameters:
        descriptors: DataFrame with ATECO code and descriptor text
        method: CONCAT or CENTROID

    Returns:
        DataFrame with target code and descriptor text
    """

    method = method.upper()
    if method not in {"CONCAT", "CENTROID"}:
        raise ValueError("method must be either 'CONCAT' or 'CENTROID'")

    descriptors = descriptors.copy()
    descriptors["code"] = descriptors["ateco_code"].apply(format_ateco_code)
    descriptors = descriptors.rename(columns={"descriptor": "descriptor_text"})

    if method == "CENTROID":
        return descriptors[["code", "descriptor_text"]].reset_index(drop=True)

    grouped = (
        descriptors.groupby("code")["descriptor_text"]
        .apply(lambda values: " | ".join(dict.fromkeys(values)))
        .reset_index(name="descriptor_text")
    )

    return grouped
