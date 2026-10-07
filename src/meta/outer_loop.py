"""Outer-loop aggregation helpers."""
import torch


def outer_loop_update(global_state, client_states, weights=None):
    """Weighted average of client state dicts."""
    if weights is None:
        weights = [1.0] * len(client_states)
    total = sum(weights)
    weights = [w / total for w in weights]

    new_state = {}
    for k in global_state.keys():
        new_state[k] = sum(
            w * s[k].float() for w, s in zip(weights, client_states)
        )
        if global_state[k].dtype != torch.float32:
            new_state[k] = new_state[k].to(global_state[k].dtype)
    return new_state