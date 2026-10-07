"""Generate Dirichlet(alpha)-skewed non-IID partitions for federated training."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def dirichlet_partition(
    labels: np.ndarray,
    num_nodes: int,
    alpha: float,
    seed: int,
) -> dict:
    rng = np.random.default_rng(seed)
    classes = np.unique(labels)
    num_classes = len(classes)

    class_indices = {c: np.where(labels == c)[0] for c in classes}

    node_indices = {i: [] for i in range(num_nodes)}
    for c in classes:
        idx = class_indices[c]
        rng.shuffle(idx)
        proportions = rng.dirichlet([alpha] * num_nodes)
        counts = (proportions * len(idx)).astype(int)
        # Distribute remainder
        remainder = len(idx) - counts.sum()
        for i in range(remainder):
            counts[i % num_nodes] += 1
        start = 0
        for i in range(num_nodes):
            node_indices[i].extend(idx[start:start + counts[i]].tolist())
            start += counts[i]

    return {str(i): sorted(v) for i, v in node_indices.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True,
                    choices=["cicids2017", "aidps", "ciciot2023"])
    ap.add_argument("--harmonized-dir", default="data/harmonized")
    ap.add_argument("--alpha", type=float, default=0.5)
    ap.add_argument("--nodes", type=int, default=500)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    df = pd.read_parquet(Path(args.harmonized_dir) / f"{args.dataset}_harmonized.parquet")
    labels = df["Label"].values

    partition = dirichlet_partition(labels, args.nodes, args.alpha, args.seed)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "dataset": args.dataset,
            "alpha": args.alpha,
            "num_nodes": args.nodes,
            "seed": args.seed,
            "partition": partition,
        }, f)

    sizes = [len(v) for v in partition.values()]
    print(f"Wrote {out_path}")
    print(f"  nodes={args.nodes}  min={min(sizes)}  max={max(sizes)}  mean={np.mean(sizes):.1f}")


if __name__ == "__main__":
    main()