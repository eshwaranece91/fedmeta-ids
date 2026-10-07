"""Symmetric 8-bit quantization."""
import torch


def symmetric_quantize(tensor, bits=8):
    qmax = 2 ** (bits - 1) - 1
    scale = tensor.abs().max()
    if scale == 0:
        return tensor
    q = torch.round(tensor / scale * qmax).clamp(-qmax, qmax)
    return q / qmax * scale


def dequantize(tensor, scale, bits=8):
    qmax = 2 ** (bits - 1) - 1
    return tensor / qmax * scale