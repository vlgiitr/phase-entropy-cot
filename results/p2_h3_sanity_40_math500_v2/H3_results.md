# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: math500
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 25076 / 28479
- matched EWMA alpha: 0.1000
- HMM mean run length: 211.2395

## Model ladder
- M_a c-index: 0.854462
- M_b c-index: 0.848874
- M_c c-index: 0.848704
- delta(M_c - M_b): -0.000171
- bootstrap 95% CI: [-0.000907, 0.000569]

## LR tests
- M_b vs M_a: LR=60.6171, p=6.8834e-15
- M_c vs M_b: LR=2.5147, p=1.1279e-01

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
