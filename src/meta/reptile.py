"""Reptile meta-learning (first-order alternative)."""
import copy
import torch
import torch.nn as nn
from .inner_loop import inner_loop_adapt


class Reptile:
    def __init__(self, model: nn.Module, inner_lr=0.01, inner_steps=3,
                 outer_lr=0.001, device="cpu"):
        self.model = model.to(device)
        self.inner_lr = inner_lr
        self.inner_steps = inner_steps
        self.outer_lr = outer_lr
        self.device = device

    def meta_train_step(self, tasks):
        init = copy.deepcopy(self.model.state_dict())
        adapted_states = []
        for task in tasks:
            adapted = inner_loop_adapt(
                copy.deepcopy(self.model),
                task,
                lr=self.inner_lr,
                steps=self.inner_steps,
                device=self.device,
            )
            adapted_states.append(adapted.state_dict())
        # Reptile update: theta <- theta + eps * mean(adapted - theta)
        new_state = copy.deepcopy(init)
        for k in init.keys():
            deltas = [s[k] - init[k] for s in adapted_states]
            mean_delta = torch.stack(deltas).mean(dim=0)
            new_state[k] = init[k] + self.outer_lr * mean_delta
        self.model.load_state_dict(new_state)
        return float(torch.stack([d.abs().mean() for d in deltas]).mean())

    def state_dict(self):
        return self.model.state_dict()

    def load_state_dict(self, sd):
        self.model.load_state_dict(sd)