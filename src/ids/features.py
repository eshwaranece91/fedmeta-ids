"""Flow feature extraction — 16-D common subset."""
import numpy as np

FEATURE_NAMES = [
    "flow_duration", "total_fwd_packets", "total_bwd_packets",
    "total_fwd_bytes", "total_bwd_bytes", "flow_bytes_per_s",
    "flow_packets_per_s", "fwd_iat_mean", "bwd_iat_mean",
    "fwd_iat_std", "bwd_iat_std", "syn_flag_count",
    "ack_flag_count", "fin_flag_count", "pkt_size_entropy",
    "flow_dir_entropy",
]


def _entropy(counts):
    counts = np.asarray(counts, dtype=float)
    if counts.sum() == 0:
        return 0.0
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def extract_features(flow):
    """Extract 16-D feature vector from a flow dict."""
    duration = max(flow.get("duration", 1e-6), 1e-6)
    fwd_pkts = flow.get("fwd_packets", 0)
    bwd_pkts = flow.get("bwd_packets", 0)
    fwd_bytes = flow.get("fwd_bytes", 0)
    bwd_bytes = flow.get("bwd_bytes", 0)
    fwd_iats = flow.get("fwd_iats", [0.0])
    bwd_iats = flow.get("bwd_iats", [0.0])
    pkt_sizes = flow.get("pkt_sizes", [0])
    directions = flow.get("directions", [0, 0])

    return np.array([
        duration,
        fwd_pkts,
        bwd_pkts,
        fwd_bytes,
        bwd_bytes,
        (fwd_bytes + bwd_bytes) / duration,
        (fwd_pkts + bwd_pkts) / duration,
        float(np.mean(fwd_iats)) if fwd_iats else 0.0,
        float(np.mean(bwd_iats)) if bwd_iats else 0.0,
        float(np.std(fwd_iats)) if fwd_iats else 0.0,
        float(np.std(bwd_iats)) if bwd_iats else 0.0,
        flow.get("syn", 0),
        flow.get("ack", 0),
        flow.get("fin", 0),
        _entropy(pkt_sizes),
        _entropy(directions),
    ], dtype=np.float32)