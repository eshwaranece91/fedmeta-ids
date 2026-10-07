"""1D-CNN for AUVs and edge gateways."""
import torch
import torch.nn as nn


class CNN1D(nn.Module):
    def __init__(self, channels=(16, 32, 64), kernel_size=3,
                 input_dim=16, num_classes=6, dropout=0.2):
        super().__init__()
        layers = []
        prev = 1
        for c in channels:
            layers += [
                nn.Conv1d(prev, c, kernel_size, padding=kernel_size // 2),
                nn.BatchNorm1d(c),
                nn.ReLU(),
                nn.Dropout(dropout),
            ]
            prev = c
        self.features = nn.Sequential(*layers)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.classifier = nn.Linear(prev, num_classes)

    def forward(self, x):
        # x: (B, input_dim) -> (B, 1, input_dim)
        if x.dim() == 2:
            x = x.unsqueeze(1)
        h = self.features(x)
        h = self.pool(h).squeeze(-1)
        return self.classifier(h)

    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())


class CNN1DMeta(nn.Module):
    """CNN with a meta-head for edge gateways."""

    def __init__(self, channels=(32, 64, 128), kernel_size=3,
                 input_dim=16, num_classes=6, meta_head_dim=64, dropout=0.2):
        super().__init__()
        self.backbone = CNN1D(
            channels=channels,
            kernel_size=kernel_size,
            input_dim=input_dim,
            num_classes=meta_head_dim,
            dropout=dropout,
        )
        self.meta_head = nn.Sequential(
            nn.Linear(meta_head_dim, meta_head_dim),
            nn.ReLU(),
            nn.Linear(meta_head_dim, num_classes),
        )

    def forward(self, x):
        z = self.backbone(x)
        return self.meta_head(z)

    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())