# AGENTS.md — EMOS Coding Lab (AI-based Coding in Official Statistics)

## 🎯 Goal

This repository is being adapted for a teaching lab for EMOS students  
(European Master in Official Statistics), Bergamo, May 2026.

The objective is **not** to produce a research-grade pipeline, but a:

- clean  
- understandable  
- well-documented  
- reproducible  

coding lab that demonstrates how **AI-based automatic coding** works in Official Statistics.

---

## 👥 Audience

Target: EMOS students

Assume that students:

- know basic Python (not advanced)
- are NOT experts in machine learning
- are NOT familiar with embeddings or vector search
- need clear explanations and intuitive examples

👉 Code must be readable before being “optimal”.

---

## 🧠 Teaching Philosophy

When modifying the repository, ALWAYS prioritize:

### 1. Clarity over performance
- Avoid complex abstractions
- Avoid premature optimization
- Prefer explicit logic over “smart tricks”

### 2. Learnability over completeness
- Show the **core idea**, not every edge case
- Reduce noise from the original research code

### 3. Step-by-step logic
Students should be able to answer:
> “What is happening in this step?”

---

## 🧩 Target Learning Outcomes

By the end of the lab, students should understand:

- what **automatic coding** is
- how **text → classification** mapping works
- what **embeddings** are (intuitively)
- how **semantic similarity** works
- how to assign a code using similarity
- what **Top-1 / Top-k accuracy** means
- why **validation and transparency** matter in Official Statistics

---

## 📚 Suggested Lab Story (VERY IMPORTANT)

Structure the code and notebook around this narrative:

1. We start from **textual descriptions**
2. We define a **target classification**
3. We build **descriptors for each class**
4. We compute **embeddings**
5. We compute **similarity**
6. We assign the **most similar code**
7. We evaluate results
8. We discuss **errors and limitations**

👉 Every piece of code should map to one of these steps.

---

## 🗂️ Suggested Repository Structure

Refactor only if useful:

.
├── README.md
├── AGENTS.md
├── requirements.txt
├── data/
│   ├── sample/
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
└── outputs/

⚠️ Do NOT over-engineer. Simpler is better.

---

## 📓 Notebook Requirements

The notebook is the **core teaching artifact**.

It MUST be:

- self-contained
- readable top-to-bottom
- structured in sections

### Required sections:

1. Introduction
2. Data loading
3. Classification & descriptors
4. Embeddings
5. Similarity-based coding
6. Evaluation
7. Error analysis
8. Discussion (Official Statistics perspective)

Each section must include:

- short Markdown explanation
- clean code cells
- no long hidden logic

---

## 🧪 Code Refactoring Rules

### Functions

- Keep functions small
- One responsibility per function
- Use clear names:
  - ❌ process_data()
  - ✅ compute_similarity_matrix()

### Docstrings (MANDATORY)

Each function must include:

def compute_similarity_matrix(embeddings_a, embeddings_b):
    """
    Computes cosine similarity between two sets of embeddings.

    Parameters:
        embeddings_a: array-like
        embeddings_b: array-like

    Returns:
        similarity matrix (n x m)
    """

---

## 💬 Comments (VERY IMPORTANT)

Use comments to explain:

- WHY something is done
- WHAT it means in statistical terms

Avoid:

- explaining obvious Python syntax
- redundant comments

---

## 🔁 Reproducibility

- No hardcoded paths
- Use relative paths
- Provide small sample data if possible
- Ensure code runs:
  - locally
  - or in Google Colab

---

## 📦 Dependencies

Keep dependencies minimal:

- pandas
- numpy
- scikit-learn
- sentence-transformers (if needed)

Avoid heavy or unnecessary libraries.

---

## 📖 README Requirements

The README must be student-friendly and include:

- What this lab is about
- What students will learn
- How to install dependencies
- How to run the notebook
- Description of the data
- Simplified workflow explanation

Tone: friendly and accessible

---

## 🧠 Concepts to Explain (SHORT & INTUITIVE)

Include short explanations in the notebook for:

- automatic coding
- classification systems
- embeddings
- cosine similarity
- Top-1 vs Top-k
- accuracy
- uncertainty / confidence
- human-in-the-loop validation

---

## ⚠️ Handling Original Research Code

The original repository may contain:

- complex logic
- experimental code
- non-documented pipelines

Codex should:

- simplify where possible
- keep only what is useful for teaching
- clearly separate:
  - teaching logic
  - research logic

---

## 🚀 Expected Workflow for Codex

When working on this repo:

1. Inspect current code
2. Identify key components
3. Propose a simplified structure
4. Refactor incrementally
5. Add documentation and comments
6. Create/clean notebook
7. Update README

After each major change, explain:

- what was changed
- why it improves clarity
- what students will learn from it

---

## 🗣️ Tone

Use a tone that feels like:

“Let’s build this together step by step”

NOT:

“Here is a complex ML pipeline”

---

## 🧩 Final Objective

This lab should feel:

- intuitive
- transparent
- hands-on
- relevant for Official Statistics

Students should leave thinking:

“Ok, I understand how this works. I could try this myself.”
