"""Per-detection energy model."""
from .acoustic_model import acoustic_energy


def energy_per_detection(model_params, quantize_bits=8, update_bytes=None):
    """Compute energy per detection in mJ.

    model_params: number of model parameters
    quantize_bits: bits per parameter after quantization
    update_bytes: optional explicit update size in bytes
    """
    if update_bytes is None:
        update_bytes = (model_params * quantize_bits) / 8
    return acoustic_energy(update_bytes)