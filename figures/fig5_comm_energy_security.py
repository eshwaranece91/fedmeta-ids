"""Generate Fig. 5: Communication, energy, security panels."""
import pandas as pd
import matplotlib.pyplot as plt

comm = pd.read_csv("results/communication/comm_summary.csv")
energy = pd.read_csv("results/energy/energy_summary.csv")
sec = pd.read_csv("results/security/security_summary.csv")

fig, axes = plt.subplots(2, 4, figsize=(18, 8))

axes[0, 0].bar(comm["method"], comm["overhead_mean"], color="steelblue")
axes[0, 0].set_title("(a) Communication Overhead (MB)")
axes[0, 0].tick_params(axis="x", rotation=45)

axes[0, 1].bar(comm["method"], comm["latency_mean"], color="steelblue")
axes[0, 1].set_title("(b) Latency (ms)")
axes[0, 1].tick_params(axis="x", rotation=45)

axes[0, 2].bar(energy["method"], energy["energy_mean"], color="coral")
axes[0, 2].set_title("(c) Energy per Detection (mJ)")
axes[0, 2].tick_params(axis="x", rotation=45)

axes[0, 3].bar(sec["method"], sec["attack_success_mean"], color="indianred")
axes[0, 3].set_title("(d) Attack Success Rate (%)")
axes[0, 3].tick_params(axis="x", rotation=45)

axes[1, 0].bar(sec["method"], sec["poison_mean"], color="seagreen")
axes[1, 0].set_title("(e) Poisoning Robustness")
axes[1, 0].tick_params(axis="x", rotation=45)

for ax in [axes[1, 1], axes[1, 2], axes[1, 3]]:
    ax.axis("off")

fig.suptitle("FedMeta-IDS Communication, Energy, and Security Performance")
plt.tight_layout()
plt.savefig("figures/fig5_comm_energy_security.pdf", dpi=300)
print("Wrote figures/fig5_comm_energy_security.pdf")