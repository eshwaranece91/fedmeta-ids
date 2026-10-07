#!/usr/bin/env bash
# Master experiment runner.
set -euo pipefail

CONFIG="configs/sim_small.yaml"
SEEDS="0"
SMOKE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --config) CONFIG="$2"; shift 2 ;;
    --seed)   SEEDS="$2"; shift 2 ;;
    --seeds)  SEEDS="$2"; shift 2 ;;
    --smoke)  SMOKE=1; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

echo "=== FedMeta-IDS experiment runner ==="
echo "config: $CONFIG"
echo "seeds:  $SEEDS"
echo "smoke:  $SMOKE"

# Expand seed range
if [[ "$SEEDS" == *-* ]]; then
  START="${SEEDS%-*}"
  END="${SEEDS#*-}"
  SEED_LIST=$(seq "$START" "$END")
else
  SEED_LIST="$SEEDS"
fi

mkdir -p results/detection results/communication results/energy \
         results/security results/ablation results/scalability

for S in $SEED_LIST; do
  echo "--- seed $S ---"
  python experiments/run_detection.py     --config "$CONFIG" --seed "$S"
  python experiments/run_communication.py --config "$CONFIG" --seed "$S"
  python experiments/run_energy.py        --config "$CONFIG" --seed "$S"
  python experiments/run_security.py      --config "$CONFIG" --seed "$S"
  if [[ "$SMOKE" -eq 0 ]]; then
    python experiments/run_ablation.py    --config "$CONFIG" --seed "$S"
    python experiments/run_scalability.py --config "$CONFIG" --seed "$S"
  fi
done

echo "=== Done. Results in results/ ==="