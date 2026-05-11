# Classification Data

This folder contains ATECO classification information used in the lab.

## `ateco22_classification.csv`

Official ATECO classification in CSV format. It includes:

- code
- title
- hierarchy level
- parent code
- official notes

Some notes contain line breaks inside CSV fields. This is expected.

## `ateco22_descriptors.csv`

Processed descriptor file prepared for the lab. The official notes at detailed levels have been split into shorter text snippets.

In the notebook, these snippets are used as text descriptors for automatic coding.
