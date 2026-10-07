"""Client-side local training for FedMeta-IDS and baselines."""
import copy
import torch
import torch.nn as nn

from src.meta.inner_loop import inner_loop_adapt
from src.compression.prune import magnitude_prune
from src.compression.quantize import symmetric_quantize


class Client:
    def __init__(self, node_id, model, device="cpu",
                 prune_sparsity=0.30, quantize_bits=8):
        self.node_id = node_id
        self.model = model.to(device)
        self.device = device
        self.prune_sparsity = prune_sparsity
        self.quantize_bits = quantize_bits

    def local_meta_step(self, task, inner_lr=0.01, inner_steps=3):
        adapted = inner_loop_adapt(
            copy.deepcopy(self.model), task,
            lr=inner_lr, steps=inner_steps, device=self.device,
        )
        return adapted.state_dict()

    def compress(self, state_dict):
        pruned = {
            k: magnitude_prune(v, self.prune_sparsity)
            for k, v in state_dict.items()
        }
        quantized = {
            k: symmetric_quantize(v, self.quantize_bits)
            for k, v in pruned.items()
        }
        return quantized

    def upload(self, state_dict, compress=True):
        if compress:
            state_dict = self.compress(state_dict)
        return state_dict

    def evaluate(self, X, y):
        self.model.eval()
        with torch.no_grad():
            X, y = X.to(self.device), y.to(self.device)
            logits = self.model(X)
            preds = logits.argmax(dim=1)
            acc = (preds == y).float().mean().item()
        return acc