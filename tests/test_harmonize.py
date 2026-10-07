"""Unit tests for data harmonization."""
import numpy as np
import pandas as pd
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.harmonize import COMMON_FEATURES, _select_features


def test_common_features_length():
    assert len(COMMON_FEATURES) == 16


def test_select_features_fills_missing():
    df = pd.DataFrame({"flow_duration": [1.0], "Label": ["BENIGN"]})
    out = _select_features(df)
    assert set(COMMON_FEATURES).issubset(out.columns)
    assert "Label" in out.columns