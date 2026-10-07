"""Unit tests for the energy model."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.energy.energy_model import energy_per_detection


def test_energy_positive():
    e = energy_per_detection(model_params=2100, quantize_bits=8)
    assert e > 0


def test_energy_scales_with_params():
    e1 = energy_per_detection(2100)
    e2 = energy_per_detection(21000)
    assert e2 > e1