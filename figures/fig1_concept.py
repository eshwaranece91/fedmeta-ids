"""Generate Fig. 1: Conceptual overview."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
ax.axis("off")

# Water line
ax.axhline(4.5, color="blue", linestyle="--", alpha=0.4)
ax.text(0.1, 4.6, "Surface", color="blue")

# Nodes
for x, y, label in [(1.5, 1.0, "Static"), (3.0, 1.0, "AUV"),
                    (4.5, 1.0, "Glider"), (6.0, 1.0, "Static"),
                    (7.5, 1.0, "AUV"), (9.0, 1.0, "Glider")]:
    ax.add_patch(Rectangle((x - 0.2, y - 0.15), 0.4, 0.3,
                           facecolor="orange", edgecolor="black"))
    ax.text(x, y - 0.4, label, ha="center", fontsize=8)

# Edge gateway
ax.add_patch(Rectangle((4.5, 4.8), 1.0, 0.5, facecolor="gold"))
ax.text(5.0, 5.05, "Edge Gateway", ha="center", fontsize=9)

# Arrows to gateway
for x in [1.5, 3.0, 4.5, 6.0, 7.5, 9.0]:
    ax.add_patch(FancyArrowPatch((x, 1.2), (5.0, 4.7),
                                 arrowstyle="->", color="gray", alpha=0.5))

ax.set_title("FedMeta-IDS: Conceptual Deployment")
plt.tight_layout()
plt.savefig("figures/fig1_concept.pdf", dpi=300)
print("Wrote figures/fig1_concept.pdf")