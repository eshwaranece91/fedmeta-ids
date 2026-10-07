"""Generate Fig. 4: Detection performance panels."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/detection/detection_summary.csv")

fig, axes = plt.subplots(3, 3, figsize=(15, 10))
metrics = ["f1_mean", "fpr_mean", "auc_mean"]
titles = ["(a) F1 Score", "(b) FPR", "(c) AUC"]

for ax, m, t in zip(axes[0], metrics, titles):
    ax.bar(df["method"], df[m], color="steelblue")
    ax.set_title(t); ax.tick_params(axis="x", rotation=45)

axes[1, 0].bar(df["method"], df["adapt_steps"].fillna(0), color="orange")
axes[1, 0].set_title("(d) Adaptation Steps")
axes[1, 0].tick_params(axis="x", rotation=45)

axes[1, 1].axis("off")
axes[1, 2].axis("off")
axes[2, 0].axis("off")
axes[2, 1].axis("off")
axes[2, 2].axis("off")

fig.suptitle("FedMeta-IDS Detection Performance vs. Baselines")
plt.tight_layout()
plt.savefig("figures/fig4_detection.pdf", dpi=300)
print("Wrote figures/fig4_detection.pdf")