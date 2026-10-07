"""Edge gateway partial aggregation."""
from src.meta.outer_loop import outer_loop_update


class EdgeGateway:
    def __init__(self, gateway_id):
        self.gateway_id = gateway_id

    def partial_aggregate(self, global_state, client_states, weights=None):
        return outer_loop_update(global_state, client_states, weights)