"""Pruned feedforward network for static sensors and gliders."""
import torch
import torch.nn as nn


class PrunedFFN(nn.Module):
    def __init__(self, layers, input_dim=16, num_classes=6, dropout=0.1):
        super().__init__()
        modules = []
        prev = input_dim
        for h in layers:
            modules += [nn.Linear(prev, h), nn.ReLU(), nn.Dropout(dropout)]
            prev = h
        modules.append(nn.Linear(prev, num_classes))
        self.net = nn.Sequential(*modules)

    def forward(self, x):
        return self.net(x)

    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())

    def memory_bytes(self) -> int:
        return self.num_params() * 4  # fp32