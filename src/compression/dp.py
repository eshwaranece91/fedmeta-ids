"""Gaussian mechanism for differential privacy."""
import torch


def gaussian_mechanism(tensor, sigma=0.5, sensitivity=1.0):
    if sigma <= 0:
        return tensor
    noise = torch.randn_like(tensor) * sigma * sensitivity
    return tensor + noise