import pandas as pd
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from collections import defaultdict
from typing import List, Tuple
from tqdm import tqdm


def get_knowledge_base(model: SentenceTransformer, ateco_df: pd.DataFrame, approach: str) -> Tuple[List[str], torch.Tensor]:
    """Generate embeddings for the knowledge base using a given model and ATECO dataframe."""

    if approach != "centroid":
        texts, codes = ateco_df["text"].tolist(), ateco_df["code"].tolist()
        embeddings = model.encode(texts, convert_to_tensor=True, show_progress_bar=True)
    
    else:
        codes, embeddings = compute_centroids(model, ateco_df)

    return codes, embeddings

def compute_centroids(model: SentenceTransformer, ateco_df: pd.DataFrame) -> Tuple[List[str], torch.Tensor]:
    """Compute centroids of embeddings for each 5-digit code."""
    
    code_groups = ateco_df.groupby("code")["text"].apply(list).reset_index()
    codes = code_groups["code"].tolist()
    descriptions = code_groups["text"].tolist()
    
    embeddings = []
    for desc_list in tqdm(descriptions, desc="Computing centroids"):
        desc_embeddings = model.encode(desc_list, convert_to_tensor=True)
        centroid = torch.mean(desc_embeddings, dim=0)
        embeddings.append(centroid)
    
    embeddings_tensor = torch.stack(embeddings)
    return codes, embeddings_tensor

def get_similarity(query_embeddings, embeddings, top_k: int = 5) -> Tuple[torch.Tensor, torch.Tensor]:
    """Compute cosine similarity between query embeddings and a set of embeddings."""

    query_norm = F.normalize(query_embeddings, p=2, dim=-1)
    embed_norm = F.normalize(embeddings, p=2, dim=-1)

    sims = query_norm @ embed_norm.T

    top_k = sims.topk(top_k, sorted=True)
    values, indices = top_k.values, top_k.indices

    return values, indices

def extract_top_k(res, top_k=5) -> Tuple[List[str], List[float]]:
    """Extract top-k unique ids in one-to-many approaches based on maximum similarity values."""
    max_dict = defaultdict(float)
    for y, v in res:
        if v > max_dict[y]:
            max_dict[y] = v
    
    unique_ids = list(max_dict.keys())[:top_k]
    similarities = list(max_dict.values())[:top_k]

    return unique_ids, similarities

def get_matches(
    similarities: torch.Tensor,
    ids: torch.Tensor,
    codes: List[str],
    y_true: List[str],
    approach: str,
    ks: List[int] = [1, 3, 5],
    similarity_threshold: float = 0.0,
) -> Tuple[dict, dict]:
    """Calculate match@k for category and division levels."""

    match_at_ks = {k: [] for k in ks}
    match_at_ks_div = {k: [] for k in ks}

    for sim, i, y_t in tqdm(zip(similarities, ids, y_true), total=len(y_true)):
        y_p = [codes[j] for j in i]

        if approach == "disentangled":
            res = [(y, v) for y, v in zip(y_p, sim)]
            y_p, sims = extract_top_k(res, max(ks))

        y_p_div = [code[:2] for code in y_p]
        y_t_div = y_t[:2]
        
        for k in ks:
            match_at_ks[k].append(int(y_t in y_p[:k]))
            match_at_ks_div[k].append(int(y_t_div in y_p_div[:k]))

    return match_at_ks, match_at_ks_div

def print_results(match_at_ks, match_at_ks_div):
    """Print match@k results for category and division levels."""

    print("Division Level (2-digit)")
    for k, v in match_at_ks_div.items():
        print(f"Match@{k}: {sum(v)/len(v):.4f}")
    print("\nCategory Level (5-digit)")
    for k, v in match_at_ks.items():
        print(f"Match@{k}: {sum(v)/len(v):.4f}")
