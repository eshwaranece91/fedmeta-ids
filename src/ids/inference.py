"""On-node IDS inference."""
import torch


class IDSInference:
    def __init__(self, model, device="cpu"):
        self.model = model.to(device)
        self.model.eval()
        self.device = device

    @torch.no_grad()
    def predict(self, x):
        x = torch.as_tensor(x, dtype=torch.float32, device=self.device)
        if x.dim() == 1:
            x = x.unsqueeze(0)
        logits = self.model(x)
        return logits.argmax(dim=1).cpu().numpy()

    @torch.no_grad()
    def predict_proba(self, x):
        x = torch.as_tensor(x, dtype=torch.float32, device=self.device)
        if x.dim() == 1:
            x = x.unsqueeze(0)
        return torch.softmax(self.model(x), dim=1).cpu().numpy()