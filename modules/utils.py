import pandas as pd
import os
import torch
import glob
from typing import Dict

def get_div_sec_map(ateco_calssification_df: pd.DataFrame) -> Dict[str, str]:
    """Create a mapping from division codes to section codes."""

    filtered_df = ateco_calssification_df[ateco_calssification_df["GERARCHIA"] == 2]
    grouped_df = filtered_df.groupby("CODICE", as_index=False).agg({"CODICE_PADRE": "first"})
    div_sec_map = dict(zip(grouped_df["CODICE"], grouped_df["CODICE_PADRE"]))

    return div_sec_map

def load_ateco_data(approach: str, synthetic: bool = False) -> pd.DataFrame:
    """Load the appropriate ATECO dataframe based on the specified approach and synthetic flag."""

    assert approach in ["naive", "disentangled", "centroid"], "Approach not recognized."
    if approach == "naive":
        assert not synthetic, "Synthetic data not available for the naive approach."

    if approach == "naive":
        ateco_df = pd.read_csv("data/ateco22_descriptor.csv")
        ateco_df["code"] = ateco_df["code"].apply(lambda x: x[:-1])
        ateco_df = ateco_df.groupby("code", as_index=False).agg({
            "text": lambda x: "\n\n".join(x)
        })
    
    elif approach in ["disentangled", "centroid"]:
        if not synthetic:
            ateco_df = pd.read_csv("data/ateco22_disentangled.csv")
            ateco_df["code"] = ateco_df["code"].apply(lambda x: x[:-1])
        else:
            ateco_df = pd.read_csv("data/ateco22_synthetic.csv")
            ateco_df["code"] = ateco_df["code"].apply(lambda x: x[:-1])
    
    return ateco_df

def load_query_embeddings(model_id: str) -> torch.Tensor:
    """Load query embeddings from disk based on the model identifier."""

    model_id = model_id.split("/")[-1]
    
    pattern = f"data/circe_embeddings/{model_id}/{model_id}_*.pt"
    files = sorted(glob.glob(pattern))
    
    if not files:
        raise FileNotFoundError(f"No embedding files found for model_id: {model_id}")

    parts = [torch.load(f) for f in files]
    embeddings = torch.cat(parts, dim=0)
    
    return embeddings