"""Statistical helpers."""
import numpy as np
from scipy import stats


def mean_sd(values):
    arr = np.asarray(values, dtype=float)
    return float(arr.mean()), float(arr.std(ddof=1))


def wilcoxon_test(a, b, alpha=0.05):
    stat, p = stats.wilcoxon(a, b)
    return {"statistic": float(stat), "p_value": float(p), "significant": p < alpha}