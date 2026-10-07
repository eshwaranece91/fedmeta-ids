#include <cmath>

double acoustic_transmission_energy_mj(double size_bytes,
                                       double bandwidth_kbps,
                                       double power_w) {
    double bits = size_bytes * 8.0;
    double tx_s = bits / (bandwidth_kbps * 1000.0);
    return power_w * tx_s * 1000.0;
}

double acoustic_transmission_time_ms(double size_bytes,
                                     double bandwidth_kbps,
                                     double delay_ms) {
    double bits = size_bytes * 8.0;
    double tx_ms = (bits / (bandwidth_kbps * 1000.0)) * 1000.0;
    return tx_ms + delay_ms;
}