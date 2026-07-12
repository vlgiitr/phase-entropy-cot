# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: math500
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 25076 / 28479
- matched EWMA alpha: 0.0049
- HMM mean run length: 211.2395
- bootstrap refit: True

## Model ladder
- M_a c-index: 0.854462
- M_b c-index: 0.848190
- M_c c-index: 0.847721
- delta(M_c - M_b): -0.000470
- bootstrap 95% CI: [-0.001687, 0.000646]

## LR tests
- M_b vs M_a: LR=56.5599, p=5.4512e-14
- M_c vs M_b: LR=16.1665, p=5.8010e-05

## Collinearity diagnostics
- corr(analysis_entropy, hmm_gamma): 0.393547
- design matrix condition number (M_c): 198.34

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
