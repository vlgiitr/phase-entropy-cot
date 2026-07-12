# Frozen controller policy summary

- Fit target: level-only controller with EWMA entropy/top1 features.
- Split policy: fit on calibration only, evaluate on validation only; the test split was not used.
- Locked split sources: [splits/calibration_locked.json](splits/calibration_locked.json), [splits/validation_locked.json](splits/validation_locked.json), [splits/test_locked.json](splits/test_locked.json).
- Evaluation artifact: [controller_real_corpus_eval_v2.json](controller_real_corpus_eval_v2.json).
- The original budget of 0.12 was inherited from the synthetic self-test defaults and was infeasible on the frozen real-corpus calibration data, so it caused the policy to collapse to length 1 everywhere.
- For the current diagnostic pass, the offline simulator uses a provisional fixed+variable cost proxy: efficiency = tokens_per_call / (c_fixed + c_variable * L), with c_fixed = 4 and c_variable = 1 as a placeholder ratio inspired by short-sequence verification overhead. This is not a measured hardware cost; full FLOPs/wall-clock-matched accounting is deferred to P4.2's real EAGLE-3 harness per PHASES.md P4.2.
- Frozen cost ratio: c_fixed = 4, c_variable = 1 (provisional, HeteroSpec-motivated placeholder; to be replaced by measured values in P4.2).
- Sensitivity range checked: c_fixed in {2, 4, 8}; the shape (low-entropy bins -> longer L) holds directionally at 2 and 8, while the frozen operating point at 4 flattens to a single length across bins. This is documented openly rather than obscured.
- Selected lengths per bin at the frozen value: [4, 4, 4, 4, 4, 4].
- This is a policy-shape sanity check for the offline controller and not a final speedup number.

## Calibration-only budget sweep

| budget | tokens_per_call | rejection_rate | adaptive_policy | distinct_lengths | selected_bin_lengths |
| --- | ---: | ---: | --- | ---: | --- |
| 0.25 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.28 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.31 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.34 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.37 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.40 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.43 | 0.6401243232404251 | 0.3598756767595749 | no | 1 | [1,1,1,1,1,1] |
| 0.46 | 0.7301784640064167 | 0.40164427511529976 | yes | 2 | [2,1,1,1,1,1] |
| 0.49 | 0.7301784640064167 | 0.40164427511529976 | yes | 2 | [2,1,1,1,1,1] |
| 0.52 | 0.811810707840385 | 0.44224984960898334 | yes | 2 | [2,2,1,1,1,1] |

Selected budget: 0.52.

## Frozen validation result

- Validation tokens per call: 1.6672916138839624
- Validation rejection rate: 0.7684148298285618
- Oracle replay (HMM-gamma threshold): recovered fraction = 0.6908512220053898
- Cluster-bootstrap 95% CI for recovered fraction (bootstrap over validation run_ids, 160 resamples): [0.6781169535155199, 0.70651908881049]
