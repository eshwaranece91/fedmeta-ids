"""Alert formatting."""
from dataclasses import dataclass
from datetime import datetime


ATTACK_NAMES = {
    0: "BENIGN", 1: "DDoS", 2: "Wormhole",
    3: "Sinkhole", 4: "Blackhole", 5: "Eavesdropping",
}


@dataclass
class Alert:
    node_id: str
    attack_class: int
    confidence: float
    timestamp: str
    severity: str


def format_alert(node_id, attack_class, confidence):
    severity = "high" if attack_class != 0 and confidence > 0.8 else "medium"
    return Alert(
        node_id=node_id,
        attack_class=attack_class,
        confidence=confidence,
        timestamp=datetime.utcnow().isoformat(),
        severity=severity,
    )