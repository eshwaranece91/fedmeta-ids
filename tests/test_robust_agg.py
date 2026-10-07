"""Unit tests for robust aggregation."""
import torch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.fl.robust_agg import trimmed_mean, robust_aggregate


def test_trimmed_mean_removes_outliers():
    good = [torch.ones(5) for _ in range(8)]
    bad = [torch.full((5,), 100.0)]
    all_t = good + bad
    result = trimmed_mean(all_t, trim_ratio=0.1)
    assert result.mean().item() < 5.0


def test_robust_aggregate_runs():
    sd = [{"w": torch.randn(4)} for _ in range(5)]
    out = robust_aggregate(sd)
    assert "w" in out