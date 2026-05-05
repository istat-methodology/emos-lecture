# Data

This folder contains the data used in the EMOS automatic coding lab.

## Folder structure

- `raw/`: original labelled queries.
- `reference/`: ATECO classification descriptors and metadata.
- `sample/`: small teaching-ready files used directly in the notebook.
- `legacy/`: older research-support files kept for provenance or possible extensions.

## Main files

- `raw/labelled_queries.csv`: labelled search queries. Each row contains a query text and the corresponding true code.
- `sample/labelled_queries_sample.csv`: 500 multi-word examples derived from the raw labelled file for classroom use.
- `reference/ateco22_disentangled.csv`: short textual descriptors for ATECO 2022 classes.
- `reference/ateco22_classification.csv`: fuller ATECO classification metadata.

## Teaching use

The lab does not start from the full research pipeline. Instead, it uses:

1. Labelled queries as examples of text that must be coded.
2. ATECO descriptors as the target classification knowledge base.
3. A small reproducible classroom sample for fast exercises.

The goal is clarity: students should see how text is mapped to a classification code step by step.
