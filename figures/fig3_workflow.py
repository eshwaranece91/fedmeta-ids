"""Generate Fig. 3: Operational workflow."""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 6); ax.set_ylim(0, 2)
ax.axis("off")

steps = [
    "1. Local\ntask sampling",
    "2. Inner-loop\nadaptation",
    "3. Model\nupload",
    "4. Meta-\naggregation",
    "5. Rapid\nadaptation",
    "6. In-network\ndetection",
]

for i, s in enumerate(steps):
    ax.add_patch(plt.Rectangle((i + 0.1, 0.5), 0.8, 1.0,
                               facecolor="lightblue", edgecolor="black"))
    ax.text(i + 0.5, 1.0, s, ha="center", va="center", fontsize=9)
    if i < len(steps) - 1:
        ax.annotate("", xy=(i + 1.1, 1.0), xytext=(i + 0.9, 1.0),
                    arrowprops=dict(arrowstyle="->"))

ax.set_title("FedMeta-IDS: Six-Step Operational Workflow")
plt.tight_layout()
plt.savefig("figures/fig3_workflow.pdf", dpi=300)
print("Wrote figures/fig3_workflow.pdf")