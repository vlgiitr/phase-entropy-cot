# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: None
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 26352 / 27729
- matched EWMA alpha: 0.0044
- HMM mean run length: 227.6393
- bootstrap refit: True

## Model ladder
- M_a c-index: 0.855191
- M_b c-index: 0.848499
- M_c c-index: 0.847355
- delta(M_c - M_b): -0.001144
- bootstrap 95% CI: [-0.002357, -0.000028]

## LR tests
- M_b vs M_a: LR=71.6696, p=0.0000e+00
- M_c vs M_b: LR=22.7514, p=1.8437e-06

## Collinearity diagnostics
- corr(analysis_entropy, hmm_gamma): 0.372069
- design matrix condition number (M_c): 215.86

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
