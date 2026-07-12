# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: None
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 26352 / 27729
- matched EWMA alpha: 0.1000
- HMM mean run length: 227.6393

## Model ladder
- M_a c-index: 0.855191
- M_b c-index: 0.850596
- M_c c-index: 0.849220
- delta(M_c - M_b): -0.001376
- bootstrap 95% CI: [-0.003019, 0.000229]

## LR tests
- M_b vs M_a: LR=44.9395, p=2.0322e-11
- M_c vs M_b: LR=13.8564, p=1.9732e-04

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
