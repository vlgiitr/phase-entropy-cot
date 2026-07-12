# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: None
- entropy col: draft_entropy
- runs train/eval: 175 / 87
- rows train/eval: 116892 / 59205
- matched EWMA alpha: 0.4050
- HMM mean run length: 2.5457
- bootstrap refit: True

## Model ladder
- M_a c-index: 0.850322
- M_b c-index: 0.849275
- M_c c-index: 0.848927
- delta(M_c - M_b): -0.000348
- bootstrap 95% CI: [-0.002111, 0.001531]

## LR tests
- M_b vs M_a: LR=32.2368, p=1.3648e-08
- M_c vs M_b: LR=0.1767, p=6.7426e-01

## Collinearity diagnostics
- corr(analysis_entropy, hmm_gamma): 0.933333
- design matrix condition number (M_c): 201.39

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
- WARNING: High correlation between analysis_entropy and hmm_gamma (|r| > 0.9).
