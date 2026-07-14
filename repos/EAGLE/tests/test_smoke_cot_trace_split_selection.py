import json
from pathlib import Path

from tools import smoke_cot_trace as smoke_cot_trace


def test_validation_split_selection_uses_locked_ids(tmp_path):
    dataset = [
        {"unique_id": "test/algebra/1004.json"},
        {"unique_id": "test/algebra/1035.json"},
        {"unique_id": "test/algebra/1072.json"},
    ]
    validation_lock = tmp_path / "validation_locked.json"
    validation_lock.write_text(json.dumps({"math500": ["test/algebra/1004.json"]}), encoding="utf-8")

    selected = smoke_cot_trace.select_dataset_rows(
        "math500",
        dataset,
        "validation",
        split_locks_dir=tmp_path,
    )

    assert [row["unique_id"] for row in selected] == ["test/algebra/1004.json"]


def test_test_split_requires_explicit_confirmation(tmp_path):
    dataset = [
        {"unique_id": "test/algebra/1004.json"},
        {"unique_id": "test/algebra/1035.json"},
    ]
    test_lock = tmp_path / "test_locked.json"
    test_lock.write_text(json.dumps({"math500": ["test/algebra/1004.json"]}), encoding="utf-8")

    try:
        smoke_cot_trace.select_dataset_rows(
            "math500",
            dataset,
            "test",
            split_locks_dir=tmp_path,
            allow_test_split=False,
            confirm_fn=lambda *_: False,
        )
    except RuntimeError as exc:
        assert "test split" in str(exc).lower()
    else:
        raise AssertionError("Expected test split selection to require confirmation")
