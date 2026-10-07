"""Unit tests for inner-loop adaptation."""
import torch
import torch.nn as nn
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.models.ffn import PrunedFFN
from src.meta.inner_loop import inner_loop_adapt


def test_inner_loop_runs():
    model = PrunedFFN([8, 4], input_dim=4, num_classes=2)
    x = torch.randn(16, 4)
    y = torch.randint(0, 2, (16,))
    task = {"support": (x, y), "query": (x, y)}
    adapted = inner_loop_adapt(model, task, lr=0.01, steps=2)
    assert adapted is not None