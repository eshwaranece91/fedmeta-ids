"""Meta-head utilities for personalized adaptation."""
import torch
import torch.nn as nn


class MetaHead(nn.Module):
    def __init__(self, in_dim=64, out_dim=6):
        super().__init__()
        self.fc = nn.Linear(in_dim, out_dim)

    def forward(self, z):
        return self.fc(z)

    def clone(self):
        new = MetaHead(self.fc.in_features, self.fc.out_features)
        new.load_state_dict(self.state_dict())
        return new