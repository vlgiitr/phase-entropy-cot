# H1 Results

## Config

- corpus_path: corpus/v1
- entropy_source: draft_entropy
- dataset_filter: None
- split_filter: calibration
- min_trace_len: 50
- n_surrogates: 10
- bootstrap_reps: 20
- ar_max_lag: 12
- pelt_penalty: 3.0

## View Summary

| view | n_traces | dip_reject_fraction | gmm_prefer_2_fraction | dip_stat_median | delta_bic_median | n_eff_median | hmm_lr_reject_fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| raw | 5 | 0.0 | 0.8 | 0.01119480706708201 | 44.99414717967602 | 640.0 | 1.0 |
| masked | 5 | 0.0 | 0.8 | 0.013864308228358952 | 20.956103889326187 | 323.5214183396373 | 0.8 |
| think_only | 0 | None | None | None | None | None | None |

## Interpretation

- `raw` is the primary H1 analysis view.
- `masked` reruns H1 after removing formatting/cue tokens.
- `think_only` reruns H1 on the longest contiguous `<think>` span.
- Silverman testing is included as a hook and will be marked skipped if the package API is unavailable.

