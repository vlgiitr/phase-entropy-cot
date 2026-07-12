# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: math500
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 25076 / 28479
- matched EWMA alpha: 0.3000
- HMM mean run length: 2.7877

## Model ladder
- M_a c-index: 0.854462
- M_b c-index: 0.850870
- M_c c-index: 0.849247
- delta(M_c - M_b): -0.001622
- bootstrap 95% CI: [-0.002436, -0.000766]

## LR tests
- M_b vs M_a: LR=31.1434, p=2.3966e-08
- M_c vs M_b: LR=2.9706, p=8.4792e-02

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
