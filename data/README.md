# Data

This folder contains the data used in the EMOS automatic coding lab.

## Folder structure

- `raw/`: original labelled queries.
- `classification/`: ATECO classification descriptors and metadata.

## Main files

- `raw/labelled_queries.csv`: labelled search queries. Each row contains a query text and the corresponding true code.
- `classification/ateco22_descriptors.csv`: short textual descriptors for ATECO 2022 target codes.
- `classification/ateco22_classification.csv`: official ATECO classification metadata.

## Teaching use

The lab does not start from the full research pipeline. Instead, it uses:

1. Labelled queries as examples of text that must be coded.
2. ATECO descriptors as the target classification knowledge base.

The goal is clarity: students should see how text is mapped to a classification code step by step.
