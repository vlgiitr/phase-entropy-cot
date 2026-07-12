# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: livecodebench
- entropy col: draft_entropy
- runs train/eval: 40 / 37
- rows train/eval: 25445 / 24609
- matched EWMA alpha: 0.5000
- HMM mean run length: 2.3237

## Model ladder
- M_a c-index: 0.836662
- M_b c-index: 0.836723
- M_c c-index: 0.835745
- delta(M_c - M_b): -0.000978
- bootstrap 95% CI: [-0.001426, -0.000526]

## LR tests
- M_b vs M_a: LR=0.2192, p=6.3965e-01
- M_c vs M_b: LR=2.2078, p=1.3732e-01

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
