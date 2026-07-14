import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from eagle.model.ea_model import RuntimeLevelController


def test_runtime_level_controller_uses_frozen_policy_bins(tmp_path):
    policy_path = tmp_path / "policy.json"
    policy_path.write_text(
        json.dumps(
            {
                "controller": {
                    "params": {
                        "entropy_mean": 2.0,
                        "entropy_std": 1.0,
                        "risk_bin_edges": [-0.5, 0.0, 0.5],
                        "bin_lengths": [4, 2, 1],
                    },
                    "config": {
                        "alpha_entropy": 0.2,
                        "alpha_top1": 0.2,
                    },
                }
            }
        ),
        encoding="utf-8",
    )

    controller = RuntimeLevelController(policy_path=str(policy_path))
    controller.reset()

    assert controller.select_length(draft_entropy=1.0, draft_top1_prob=0.9) == 4
    assert controller.select_length(draft_entropy=3.0, draft_top1_prob=0.5) == 2
    assert controller.select_length(draft_entropy=4.0, draft_top1_prob=0.2) == 1
