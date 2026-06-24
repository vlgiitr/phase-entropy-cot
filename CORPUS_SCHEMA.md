# Corpus Schema

## Overview

The phase-entropy-cot corpus is stored as **Parquet**, partitioned by:
```
(model, drafter, dataset, temperature, split)
```

Location: `corpus/v1/model=llama8b/drafter=EAGLE-3/dataset={math500,livecodebench}/temperature=0/split=none/`

**Total rows**: 236,235 token-level rows across 350 traces (200 MATH-500 + 150 LiveCodeBench)

---

## Column Reference

### Partition Columns (in directory structure, not stored in files)

| Column | Type | Values | Notes |
|--------|------|--------|-------|
| `model` | string | `"llama8b"` | Target model name (DeepSeek-R1-Distill-Llama-8B) |
| `drafter` | string | `"EAGLE-3"` | Drafter head name |
| `dataset` | string | `"math500"`, `"livecodebench"` | Source dataset |
| `temperature` | int | `0` | Sampling temperature (frozen at 0 for this corpus) |
| `split` | string | `"none"` | Placeholder; to be assigned in P1.4 split locking (will become `"calibration"`, `"validation"`, `"test"`) |

---

### Core Per-Token Columns (stored in Parquet files)

#### Identifiers & Metadata

| Column | Type | Description |
|--------|------|-------------|
| `run_id` | string | Unique trace identifier (UUID) |
| `problem_id` | string | Problem source identifier (e.g., `"test/algebra/1035.json"` or `"1873_B"`) |
| `model_name` | string | Full model name (e.g., `"llama-8b"`) |
| `drafter_name` | string | Full drafter name (e.g., `"EAGLE-3"`) |
| `step` | int | Global token step within trace (0-indexed from prompt end) |
| `position` | int | Position in generation (alias for `step` in some contexts) |

#### Entropy & Confidence

| Column | Type | Description | Units |
|--------|------|-------------|-------|
| `target_entropy` | float32 | Shannon entropy on target model's full softmax | bits |
| `draft_entropy` | float32 | Shannon entropy on drafter's full softmax | bits |
| `draft_top1_prob` | float32 | Probability of top-1 token in drafter distribution | [0, 1] |
| `draft_topk_probs` | object (array-like) | Top-k probabilities (k=32) from drafter logits | JSON array of floats |

#### Acceptance & Tree Dynamics

| Column | Type | Description |
|--------|------|-------------|
| `accepted` | bool | Whether the draft token was accepted at verification |
| `tree_depth_at_accept` | int | Depth of the speculative tree when this token was accepted/rejected |
| `tree_depth` | int | Tree depth (synonym for `tree_depth_at_accept`) |
| `accept_length` | int | Length of accepted run (cumulative) |

#### Token Information

| Column | Type | Description |
|--------|------|-------------|
| `token_id` | int | Token ID in vocabulary |
| `token_str` | string | Decoded token string |

#### Semantic Context

| Column | Type | Description | Values |
|--------|------|-------------|--------|
| `is_inside_think` | bool | Whether token is inside a `<think>...</think>` span | `true` or `false` |
| `phase_label_hmm` | float/null | HMM-derived phase label (null at corpus generation, filled in P2.C.1) | `null`, `0`, `1` |

---

### Auxiliary Columns (metadata, debugging)

| Column | Type | Description | Notes |
|--------|------|-------------|-------|
| `best_candidate` | object/null | Best candidate info from tree search | JSON or null |
| `error` | object/null | Error info if generation failed | JSON or null |
| `retrieve_indices_shape` | string | Shape of retrieve indices tensor | Debugging artifact |
| `candidates_shape` | string | Shape of candidates tensor | Debugging artifact |
| `hidden_state_new_shape` | string | Shape of hidden state | Debugging artifact |
| `logits_shape` | string | Shape of logits tensor | Debugging artifact |

---

## Data Types (PyArrow / Pandas)

```python
{
    # Partition columns (structural, not in file schema)
    "model": "string",
    "drafter": "string", 
    "dataset": "string",
    "temperature": "int32",
    "split": "string",
    
    # Core token data
    "run_id": "string",
    "problem_id": "string",
    "model_name": "string",
    "drafter_name": "string",
    "step": "int32",
    "position": "int32",
    "token_id": "int32",
    "token_str": "string",
    "target_entropy": "float32",
    "draft_entropy": "float32",
    "draft_top1_prob": "float32",
    "draft_topk_probs": "object",  # JSON array
    "accepted": "bool",
    "tree_depth_at_accept": "int32",
    "tree_depth": "int32",
    "accept_length": "int32",
    "is_inside_think": "bool",
    "phase_label_hmm": "float64 or null",
    
    # Auxiliary
    "best_candidate": "object or null",
    "error": "object or null",
    "retrieve_indices_shape": "string",
    "candidates_shape": "string",
    "hidden_state_new_shape": "string",
    "logits_shape": "string",
}
```

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total token-level rows | 236,235 |
| Unique traces | 350 |
| MATH-500 traces | 200 |
| LiveCodeBench traces | 150 |
| Average tokens per trace | 675 |
| Max tokens per trace | 962 |
| Min tokens per trace | 171 |

---

## Notes for Analysis

1. **Partition by split**: At P1.4 completion, this corpus will be repartitioned or re-assigned with `split` ∈ {`"calibration"`, `"validation"`, `"test"`} based on problem_id groupings (50:25:25).

2. **Phase labels (P2)**: The `phase_label_hmm` column is null in the frozen corpus; it will be populated during P2.C.1 when the 2-state Gaussian HMM is fit on the calibration split.

3. **Entropy units**: All entropy values are in **bits** (log₂ scale), computed from softmax distributions.

4. **Acceptance ground truth**: `accepted` is the oracle label; use `draft_top1_prob` as a proxy feature for controller design.

5. **Tree depth**: Controlled at generation time (depth=3, top_k=8); tree_depth_at_accept ≤ 3 always.

6. **Filtering for analysis**: Remove rows where `error` is not null before statistical tests; use `is_inside_think` to stratify or mask reasoning spans as needed (see P2.A.4).

---

## Reading the Corpus

```python
import pandas as pd
import pyarrow.dataset as ds
from pathlib import Path

corpus_path = Path("/root/phase-entropy-cot/corpus/v1/model=llama8b")

# Read as PyArrow dataset (respects partitioning)
dataset = ds.dataset(str(corpus_path), format='parquet')
table = dataset.to_table()
df = table.to_pandas()

# Filter to a specific subset
math500_df = df[df['dataset'] == 'math500']

# Group by trace
traces = df.groupby('run_id')
for run_id, trace_df in traces:
    print(f"Trace {run_id}: {len(trace_df)} tokens")
```

---

## Commit Info

- **Generated**: 2026-06-24 (P1.3 completion)
- **Repartitioned**: 2026-06-24 (P1.4 completion)
- **Locked test set**: 2026-06-24
- **Owner**: phase-entropy-cot P1 pipeline
