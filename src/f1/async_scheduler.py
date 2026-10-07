"""Asynchronous freshness-weighted scheduler."""
import time


class AsyncScheduler:
    def __init__(self, staleness_halflife=10.0):
        self.halflife = staleness_halflife
        self.timestamps = {}

    def mark(self, node_id):
        self.timestamps[node_id] = time.time()

    def freshness_weight(self, node_id):
        if node_id not in self.timestamps:
            return 1.0
        age = time.time() - self.timestamps[node_id]
        return 0.5 ** (age / self.halflife)