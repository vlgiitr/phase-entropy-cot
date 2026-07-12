# P2.C H3 Results

## Setup
- corpus: corpus/v1
- train split: calibration
- eval split: validation
- dataset filter: livecodebench
- entropy col: draft_entropy
- runs train/eval: 40 / 37
- rows train/eval: 25445 / 24609
- matched EWMA alpha: 0.1000
- HMM mean run length: 311.7758

## Model ladder
- M_a c-index: 0.836662
- M_b c-index: 0.836735
- M_c c-index: 0.836315
- delta(M_c - M_b): -0.000420
- bootstrap 95% CI: [-0.001452, 0.000711]

## LR tests
- M_b vs M_a: LR=1.0419, p=3.0739e-01
- M_c vs M_b: LR=5.5250, p=1.8746e-02

## Artifacts
- p2_h3_summary.json
- p2_h3_model_scores.csv
- p2_h3_token_features.csv
