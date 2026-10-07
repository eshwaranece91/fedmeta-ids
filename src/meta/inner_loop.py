"""Inner-loop adaptation used by all meta-learners."""
import torch
import torch.nn as nn


def inner_loop_adapt(model, task, lr=0.01, steps=3, device="cpu"):
    model = model.to(device)
    model.train()
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    x, y = task["support"]
    x, y = x.to(device), y.to(device)
    for _ in range(steps):
        opt.zero_grad()
        logits = model(x)
        loss = nn.functional.cross_entropy(logits, y)
        loss.backward()
        opt.step()
    return model