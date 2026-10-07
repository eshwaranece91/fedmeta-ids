#!/usr/bin/env bash
# Run an Aqua-Sim simulation for FedMeta-IDS.
set -euo pipefail

CONFIG="${1:-configs/sim_small.yaml}"
SEED="${2:-0}"

echo "Running simulation with config=$CONFIG seed=$SEED"
mkdir -p results/raw

# Parse config (simple grep-based; replace with yq for production)
NODES=$(grep -E '^\s*nodes:' "$CONFIG" | awk '{print $2}')
EDGE=$(grep -E '^\s*edge_gateways:' "$CONFIG" | awk '{print $2}')

echo "  nodes=$NODES  edge_gateways=$EDGE  seed=$SEED"

# Select TCL topology
case "$NODES" in
  50)  TCL="sim/tcl/topology_small.tcl" ;;
  200) TCL="sim/tcl/topology_medium.tcl" ;;
  500) TCL="sim/tcl/topology_large.tcl" ;;
  *)   echo "Unknown node count: $NODES"; exit 1 ;;
esac

echo "  topology=$TCL"
ns "$TCL" -seed "$SEED" || echo "WARNING: ns not found; skipping actual simulation."