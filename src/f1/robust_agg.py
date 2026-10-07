"""Robust aggregation: trimmed mean + cosine outlier rejection."""
import torch


def trimmed_mean(tensors, trim_ratio=0.10):
    """Coordinate-wise trimmed mean."""
    stacked = torch.stack([t.float() for t in tensors], dim=0)
    n = stacked.shape[0]
    k = int(n * trim_ratio)
    if k == 0:
        return stacked.mean(dim=0)
    sorted_t, _ = torch.sort(stacked, dim=0)
    trimmed = sorted_t[k:n - k]
    return trimmed.mean(dim=0)


def cosine_outlier_reject(tensors, threshold=0.30):
    """Reject tensors whose flattened cosine similarity to the mean is below threshold."""
    flats = torch.stack([t.flatten().float() for t in tensors], dim=0)
    mean = flats.mean(dim=0)
    keep = []
    for f in flats:
        cos = torch.nn.functional.cosine_similarity(f, mean, dim=0).item()
        if cos >= threshold:
            keep.append(True)
        else:
            keep.append(False)
    if not any(keep):
        keep = [True] * len(tensors)
    return [t for t, k in zip(tensors, keep) if k]


def robust_aggregate(state_dicts, trim_ratio=0.10, cosine_threshold=0.30, weights=None):
    if not state_dicts:
        raise ValueError("No state dicts to aggregate.")

    keys = state_dicts[0].keys()
    new_state = {}
    for k in keys:
        tensors = [sd[k] for sd in state_dicts]
        tensors = cosine_outlier_reject(tensors, cosine_threshold)
        new_state[k] = trimmed_mean(tensors, trim_ratio)
    return new_state