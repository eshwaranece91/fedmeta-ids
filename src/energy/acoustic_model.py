"""Acoustic channel models."""


def acoustic_transmission_time(size_bytes, bandwidth_kbps=10.0, delay_ms=300.0):
    """Return total transmission time in ms."""
    bits = size_bytes * 8
    tx_ms = (bits / (bandwidth_kbps * 1000)) * 1000
    return tx_ms + delay_ms


def acoustic_energy(size_bytes, bandwidth_kbps=10.0, power_w=2.0):
    """Return transmission energy in mJ."""
    bits = size_bytes * 8
    tx_s = bits / (bandwidth_kbps * 1000)
    return power_w * tx_s * 1000