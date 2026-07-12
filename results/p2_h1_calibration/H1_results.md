# H1 Results

## Config

- corpus_path: corpus/v1
- entropy_source: draft_entropy
- dataset_filter: None
- split_filter: calibration
- min_trace_len: 50
- n_surrogates: 200
- bootstrap_reps: 200
- ar_max_lag: 12
- pelt_penalty: 3.0

## View Summary

| view | n_traces | dip_reject_fraction | gmm_prefer_2_fraction | dip_stat_median | delta_bic_median | n_eff_median | hmm_lr_reject_fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| raw | 175 | 0.18857142857142858 | 0.9885714285714285 | 0.0146665912653749 | 92.01955067366498 | 443.7521844576633 | 1.0 |
| masked | 175 | 0.13714285714285715 | 0.9714285714285714 | 0.016340628825675156 | 45.91495887683004 | 308.0 | 0.9885714285714285 |
| think_only | 0 | None | None | None | None | None | None |

## Interpretation

- `raw` is the primary H1 analysis view.
- `masked` reruns H1 after removing formatting/cue tokens.
- `think_only` reruns H1 on the longest contiguous `<think>` span.
- Silverman testing is included as a hook and will be marked skipped if the package API is unavailable.

