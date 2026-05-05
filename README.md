# EMOS Coding Lab: Automatic Coding in Official Statistics

This repository contains a teaching lab for EMOS students at the University of Bergamo, May 2026.

The lab introduces **AI-based automatic coding** with a small, transparent workflow. The goal is not to build a research-grade production system. The goal is to understand the core idea:

> How can we map a short text description to a statistical classification code?

## What students will learn

By the end of the lab, students should understand:

- what automatic coding is
- what a classification system is
- how target code descriptors can represent possible codes
- the intuition behind text embeddings
- what Hugging Face is used for in this workflow
- how cosine similarity can suggest candidate codes
- what Top-1 and Top-k accuracy mean
- why validation and transparency matter in Official Statistics

## Lab story

The notebook follows this sequence:

1. Start from labelled text queries.
2. Load the target classification descriptors.
3. Convert texts into numerical representations.
4. Compute similarity between queries and target code descriptors.
5. Assign the most similar code.
6. Evaluate the predictions.
7. Inspect errors and limitations.
8. Discuss human-in-the-loop validation.

## Repository structure

```text
.
├── data/
│   ├── raw/
│   │   └── labelled_queries.csv
│   ├── reference/
│   │   ├── ateco22_disentangled.csv
│   │   └── ateco22_classification.csv
│   ├── sample/
│   │   └── labelled_queries_sample.csv
│   └── README.md
├── notebooks/
│   └── emos_coding_lab.ipynb
├── src/
│   ├── data_loading.py
│   ├── descriptors.py
│   ├── embeddings.py
│   ├── similarity.py
│   ├── evaluation.py
│   └── utils.py
├── outputs/
├── requirements.txt
└── README.md
```

The repository is centered on `notebooks/emos_coding_lab.ipynb` and the simple helpers in `src/`.

## Installation

Create and activate a Python environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

If you are using Google Colab, upload the repository files or mount them from Drive, then run the same installation command in a notebook cell:

```python
%pip install -r requirements.txt
```

## Running the lab

Open:

```text
notebooks/emos_coding_lab.ipynb
```

Run the notebook from top to bottom.

The main path uses a simple TF-IDF representation so the lab runs quickly and reliably. The notebook also includes an optional cell for multilingual sentence embeddings with `sentence-transformers`.

The optional embedding model is loaded from Hugging Face, a public hub for pre-trained machine learning models. This lets students see how modern AI workflows often reuse existing models instead of training everything from scratch.

## Models and Compute

In the classroom notebook we use:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

This model is a good teaching choice because it is multilingual, relatively small, and can run on an ordinary laptop. It lets students focus on the automatic coding workflow instead of waiting for a large model to run.

In research or production experiments, it is useful to compare several embedding models. Examples include:

```text
BAAI/bge-m3
intfloat/multilingual-e5-base
intfloat/multilingual-e5-large
Alibaba-NLP/gte-multilingual-base
Qwen/Qwen3-Embedding-0.6B
```

Larger models may produce better semantic representations, but they also require more compute. This matters in practice:

- Small models are easier to run locally and are better for teaching.
- Larger models can be slower and may need more memory.
- GPU environments can make embedding computation much faster.
- Cloud platforms such as Azure are useful when evaluating many models or running larger models.

This is an important lesson for Official Statistics: model quality is not the only criterion. A real workflow also needs to consider cost, reproducibility, infrastructure, transparency, and whether the system can be maintained over time.

## Descriptor Strategies

The labelled data uses 5-digit target codes such as `73.11.0`. The ATECO descriptor file is more detailed and contains 6-digit codes such as `73.11.01`.

The notebook lets students compare two ways of representing each 5-digit target code:

- `CONCAT`: join all detailed descriptor texts belonging to the same 5-digit code, then compute one embedding.
- `CENTROID`: compute embeddings for the detailed descriptor texts first, then average the vectors for each 5-digit code.

This is a useful modelling choice to discuss. It shows that automatic coding is not only about choosing an AI model; it is also about deciding how to represent the classification system.

## Data

The main labelled dataset is `data/raw/labelled_queries.csv`. It contains:

- `query`: text query to be coded
- `n_words`: number of words in the query
- `true_code`: labelled true code, written in dotted ATECO style such as `73.11.0`

The classroom notebook starts from `data/sample/labelled_queries_sample.csv`, a small reproducible subset of the raw labelled data.

The target code descriptors come from `data/reference/ateco22_disentangled.csv`. These descriptors are used as the text representation of the target classification.

## Teaching principle

Every step should be understandable:

```text
text query
  → text descriptor for each code
  → numerical representation
  → similarity score
  → suggested code
  → evaluation
```

This is a lab about transparent statistical learning, not a black-box demo.
