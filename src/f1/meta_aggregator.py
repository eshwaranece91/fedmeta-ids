"""Global meta-aggregator with robust aggregation."""
from src.fl.robust_agg import robust_aggregate


class MetaAggregator:
    def __init__(self, trim_ratio=0.10, cosine_threshold=0.30):
        self.trim_ratio = trim_ratio
        self.cosine_threshold = cosine_threshold

    def aggregate(self, edge_states, weights=None):
        return robust_aggregate(
            edge_states,
            trim_ratio=self.trim_ratio,
            cosine_threshold=self.cosine_threshold,
            weights=weights,
        )