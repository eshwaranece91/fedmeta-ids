"""Magnitude pruning."""
import torch


def magnitude_prune(tensor, sparsity=0.30):
    if sparsity <= 0:
        return tensor
    flat = tensor.flatten()
    k = int(flat.numel() * sparsity)
    if k == 0:
        return tensor
    threshold = torch.kthvalue(flat.abs(), k).values
    mask = tensor.abs() > threshold
    return tensor * mask.float()