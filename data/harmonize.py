"""Harmonize CIC-IDS-2017, AIDPS, and CICIoT2023 to a common 16-D feature space."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import MinMaxScaler

COMMON_FEATURES = [
    "flow_duration",
    "total_fwd_packets",
    "total_bwd_packets",
    "total_fwd_bytes",
    "total_bwd_bytes",
    "flow_bytes_per_s",
    "flow_packets_per_s",
    "fwd_iat_mean",
    "bwd_iat_mean",
    "fwd_iat_std",
    "bwd_iat_std",
    "syn_flag_count",
    "ack_flag_count",
    "fin_flag_count",
    "pkt_size_entropy",
    "flow_dir_entropy",
]

ATTACK_LABELS = {
    "BENIGN": 0,
    "DDoS": 1,
    "Wormhole": 2,
    "Sinkhole": 3,
    "Blackhole": 4,
    "Eavesdropping": 5,
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_raw(dataset_dir: Path) -> pd.DataFrame:
    csvs = sorted(dataset_dir.glob("*.csv"))
    if not csvs:
        raise FileNotFoundError(f"No CSVs found in {dataset_dir}")
    frames = [pd.read_csv(c, low_memory=False) for c in csvs]
    return pd.concat(frames, ignore_index=True)


def _select_features(df: pd.DataFrame) -> pd.DataFrame:
    present = [c for c in COMMON_FEATURES if c in df.columns]
    missing = set(COMMON_FEATURES) - set(present)
    if missing:
        print(f"  WARNING: missing features {missing}; filling with 0.")
        for c in missing:
            df[c] = 0.0
        present = COMMON_FEATURES
    return df[present + ["Label"]].copy()


def _rank_features_by_mi(df: pd.DataFrame, top_k: int = 16) -> list:
    X = df.drop(columns=["Label"]).fillna(0.0)
    y = df["Label"].values
    mi = mutual_info_classif(X, y, random_state=42)
    ranked = sorted(zip(X.columns, mi), key=lambda t: -t[1])
    return [name for name, _ in ranked[:top_k]]


def harmonize(dataset_dir: Path, name: str, out_dir: Path) -> Path:
    print(f"Harmonizing {name} from {dataset_dir} ...")
    df = _load_raw(dataset_dir)
    df = _select_features(df)
    df["Label"] = df["Label"].astype(str).str.strip().map(
        lambda x: ATTACK_LABELS.get(x, 0)
    )
    df = df.fillna(0.0)

    scaler = MinMaxScaler()
    X = scaler.fit_transform(df[COMMON_FEATURES])
    out = pd.DataFrame(X, columns=COMMON_FEATURES)
    out["Label"] = df["Label"].values

    out_path = out_dir / f"{name}_harmonized.parquet"
    out.to_parquet(out_path, index=False)
    print(f"  Wrote {out_path}  ({len(out)} rows)")

    meta = {
        "dataset": name,
        "rows": len(out),
        "features": COMMON_FEATURES,
        "feature_ranking": _rank_features_by_mi(df),
        "sha256": _sha256(out_path),
    }
    with open(out_dir / f"{name}_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", default="data/raw")
    ap.add_argument("--out", default="data/harmonized")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    raw = Path(args.raw_dir)
    for name, sub in [
        ("cicids2017", "cicids2017"),
        ("aidps", "aidps"),
        ("ciciot2023", "ciciot2023"),
    ]:
        d = raw / sub
        if d.exists():
            harmonize(d, name, out_dir)
        else:
            print(f"Skipping {name}: {d} not found.")


if __name__ == "__main__":
    main()