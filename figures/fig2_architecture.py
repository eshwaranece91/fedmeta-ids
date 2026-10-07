"""Generate Fig. 2: Five-layer architecture."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.axis("off")

layers = [
    (8.5, "Application Layer", "#f4c2c2"),
    (6.8, "Federated Meta-Learning Layer", "#c2d4f4"),
    (5.1, "Edge Layer", "#c2f4c2"),
    (3.4, "Communication Layer", "#f4e2c2"),
    (1.7, "Physical Layer", "#d4c2f4"),
]

for y, name, color in layers:
    ax.add_patch(Rectangle((0.5, y - 0.7), 9, 1.4, facecolor=color,
                           edgecolor="black"))
    ax.text(5, y, name, ha="center", va="center", fontsize=11, fontweight="bold")

ax.set_title("FedMeta-IDS: Five-Layer Architecture")
plt.tight_layout()
plt.savefig("figures/fig2_architecture.pdf", dpi=300)
print("Wrote figures/fig2_architecture.pdf")