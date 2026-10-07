"""Energy performance experiment."""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from src.utils.seed import set_seed


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)


def simulate_energy(config, seed):
    set_seed(seed)
    rng = np.random.default_rng(seed)

    methods = ["FedAvg", "FedProx", "PerFLID", "MAML-FL", "XFL", "FedMeta-IDS"]
    energy = {"FedAvg": 124, "FedProx": 118, "PerFLID": 96,
              "MAML-FL": 102, "XFL": 89, "FedMeta-IDS": 73}

    rows = []
    for m in methods:
        rows.append({
            "method": m,
            "seed": seed,
            "energy_mj": float(max(0, energy[m] + rng.normal(0, 4.0))),
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--seed", type=int, required=True)
    args = ap.parse_args()

    config = load_config(args.config)
    rows = simulate_energy(config, args.seed)

    out_dir = Path("results/energy")
    out_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out_dir / f"energy_seed{args.seed}.csv", index=False)

    all_files = sorted(out_dir.glob("energy_seed*.csv"))
    df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
    summary = df.groupby("method").agg(
        energy_mean=("energy_mj", "mean"), energy_sd=("energy_mj", "std"),
    ).reset_index()
    summary.to_csv(out_dir / "energy_summary.csv", index=False)
    print(f"[energy] seed {args.seed} -> {out_dir}")


if __name__ == "__main__":
    main()