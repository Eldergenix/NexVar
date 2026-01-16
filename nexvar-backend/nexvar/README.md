# NexVar: A Foundation Model for Genomic Design and Analysis

![NexVar Architecture](nexvar.jpg)

**NexVar** is a state-of-the-art genomic foundation model designed to advance the frontiers of long-context DNA sequence modeling. Built upon the [StripedHyena 2](https://github.com/Zymrael/savanna/blob/main/paper.pdf) architecture, NexVar offers single-nucleotide resolution modeling with an unprecedented context window of up to **1 million base pairs**.

Trained autoregressively on the [OpenGenome2](https://huggingface.co/datasets/arcinstitute/opengenome2) diverse dataset—comprising 8.8 trillion tokens spanning all domains of life—NexVar serves as a robust engine for variant effect prediction (VEP), sequence generation, and evolutionary analysis.

## Research Abstract

For a comprehensive technical analysis, please refer to our preprint:

> **"Genome modeling and design across all domains of life with NexVar"**  
> [Read on bioRxiv](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1)

## System Requirements & Installation

### Hardware Prerequisites

NexVar leverages high-performance computing capabilities.

- **Minimum Requirement**: NVIDIA GPU with Compute Capability ≥ 8.9 (e.g., H100) for FP8 Transformer Engine support.
- **Recommended**: Multi-GPU setup for `nexvar_40b` inference.

### Installation

We recommend deploying NexVar within a dedicated Conda environment (Python ≥ 3.11).

#### Option A: Source Build (Recommended)

Cloning the repository ensures access to the latest research checkpoints and inference utilities.

```bash
git clone --recurse-submodules git@github.com:Eldergenix/NexVar.git
cd nexvar
pip install .
```

#### Verification

Validate the installation by running the test suite:

```bash
python ./test/test_nexvar.py --model_name nexvar_7b
```

## Model Zoo

We provide a suite of pre-trained checkpoints optimized for various computational budgets and context requirements. Models are hosted on [HuggingFace](https://huggingface.co/arcinstitute).

| Model Variant         | Parameters | Context Length | Description                                                                |
| :-------------------- | :--------- | :------------- | :------------------------------------------------------------------------- |
| **`nexvar_40b`**      | 40B        | 1,000,000 bp   | Flagship model; contexts extended from `nexvar_40b_base`.                  |
| **`nexvar_7b`**       | 7B         | 1,000,000 bp   | High-performance efficient model; contexts extended from `nexvar_7b_base`. |
| **`nexvar_40b_base`** | 40B        | 8,192 bp       | Base pre-training model.                                                   |
| **`nexvar_7b_base`**  | 7B         | 8,192 bp       | Base pre-training model.                                                   |
| **`nexvar_1b_base`**  | 1B         | 8,192 bp       | Lightweight experimental model.                                            |

## Computational Capabilities

NexVar exposes a Python API for three primary modes of operation: Likelihood Scoring (Forward), Embedding Extraction, and Sequence Generation.

### 1. Zero-Shot Variant Effect Prediction (Forward Pass)

Calculate the likelihood of a given DNA sequence to predict pathogenicity or functional impact.

```python
import torch
from nexvar import NexVar

# Initialize Model
model = NexVar('nexvar_7b')

# Prepare Input
sequence = 'ACGT' * 10
input_ids = torch.tensor(
    model.tokenizer.tokenize(sequence),
    dtype=torch.int,
).unsqueeze(0).to('cuda:0')

# Inference
outputs, _ = model(input_ids)
logits = outputs[0]

print(f"Logits Shape: {logits.shape}") # (Batch, Length, Vocab)
```

### 2. High-Dimensional Embedding Extraction

Extract latent representations for downstream discriminative tasks. Research indicates intermediate layers often yield superior representations for biological tasks.

```python
layer_target = 'blocks.28.mlp.l3'
outputs, embeddings = model(input_ids, return_embeddings=True, layer_names=[layer_target])
print(f"Embedding Dimensions: {embeddings[layer_target].shape}")
```

### 3. Generative Design

Generate novel DNA sequences conditioned on prompt contexts (e.g., promoter design, regulatory element synthesis).

```python
output = model.generate(
    prompt_seqs=["ATG..."],
    n_tokens=400,
    temperature=0.9,
    top_k=4
)
print(f"Generated Sequence: {output.sequences[0]}")
```

## Examples & Notebooks

- **[Variant Effect Prediction (BRCA1)](notebooks/brca1/brca1_zero_shot_vep.ipynb)**: A comprehensive workflow for zero-shot pathogenicity prediction of SNVs in the _BRCA1_ gene using delta-likelihood scores.
- **[Generative Design](notebooks/generation/generation_notebook.ipynb)**: Demonstrates "DNA autocompletion" and phylogenetic-tag guided generation.

## Cloud Inference (NVIDIA NIM)

For enterprise-grade scalability, NexVar is integrated into NVIDIA NIM.

- [NIM Documentation](https://docs.nvidia.com/nim/bionemo/nexvar/latest/overview.html)
- [Hosted API Endpoint](https://build.nvidia.com/arc/nexvar-40b)

## Citation

Please cite the following preprint when utilizing NexVar in your research:

```bibtex
@article {Brixi2025.NexVar,
	author = {Brixi, Garyk and others},
	title = {Genome modeling and design across all domains of life with NexVar},
	year = {2025},
	doi = {10.1101/2025.02.18.638918},
	journal = {bioRxiv}
}
```
