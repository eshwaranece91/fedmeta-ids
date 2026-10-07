"""First-order MAML for FedMeta-IDS."""
import copy
import torch
import torch.nn as nn
from .inner_loop import inner_loop_adapt


class MAML:
    def __init__(self, model: nn.Module, inner_lr=0.01, inner_steps=3,
                 outer_lr=0.001, device="cpu"):
        self.model = model.to(device)
        self.inner_lr = inner_lr
        self.inner_steps = inner_steps
        self.outer_lr = outer_lr
        self.device = device
        self.optim = torch.optim.Adam(self.model.parameters(), lr=outer_lr)

    def meta_train_step(self, tasks):
        """One outer-loop update over a list of tasks."""
        self.optim.zero_grad()
        outer_loss = 0.0
        for task in tasks:
            adapted = inner_loop_adapt(
                copy.deepcopy(self.model),
                task,
                lr=self.inner_lr,
                steps=self.inner_steps,
                device=self.device,
            )
            x, y = task["query"]
            x, y = x.to(self.device), y.to(self.device)
            logits = adapted(x)
            outer_loss = outer_loss + nn.functional.cross_entropy(logits, y)
        outer_loss = outer_loss / max(len(tasks), 1)
        outer_loss.backward()
        self.optim.step()
        return outer_loss.item()

    def state_dict(self):
        return self.model.state_dict()

    def load_state_dict(self, sd):
        self.model.load_state_dict(sd)