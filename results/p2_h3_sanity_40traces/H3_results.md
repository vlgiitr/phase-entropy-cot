# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: None
- entropy col: draft_entropy
- runs train/eval: 40 / 40
- rows train/eval: 26352 / 27729
- matched EWMA alpha: 0.5000
- HMM mean run length: 2.4021

## Model ladder
- M_a c-index: 0.855191
- M_b c-index: 0.852978
- M_c c-index: 0.852893
- delta(M_c - M_b): -0.000085
- bootstrap 95% CI: [-0.000126, -0.000047]

## LR tests
- M_b vs M_a: LR=18.1986, p=1.9902e-05
- M_c vs M_b: LR=0.0037, p=9.5137e-01

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
