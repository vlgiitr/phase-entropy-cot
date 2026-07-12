# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: livecodebench
- entropy col: draft_entropy
- runs train/eval: 40 / 37
- rows train/eval: 25445 / 24609
- matched EWMA alpha: 0.0032
- HMM mean run length: 311.7758
- bootstrap refit: True

## Model ladder
- M_a c-index: 0.836662
- M_b c-index: 0.835999
- M_c c-index: 0.835944
- delta(M_c - M_b): -0.000054
- bootstrap 95% CI: [-0.000517, 0.000264]

## LR tests
- M_b vs M_a: LR=10.2021, p=1.4028e-03
- M_c vs M_b: LR=2.8852, p=8.9396e-02

## Collinearity diagnostics
- corr(analysis_entropy, hmm_gamma): 0.317037
- design matrix condition number (M_c): 427.31

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
