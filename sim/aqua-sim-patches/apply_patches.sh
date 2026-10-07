#!/usr/bin/env bash
# Apply FedMeta-IDS patches to an Aqua-Sim / NS-2 tree.
set -euo pipefail

AQUA_SIM_DIR="${AQUA_SIM_DIR:-/opt/aqua-sim}"
PATCH_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Applying FedMeta-IDS patches from $PATCH_DIR ..."

if [[ ! -d "$AQUA_SIM_DIR" ]]; then
  echo "WARNING: AQUA_SIM_DIR=$AQUA_SIM_DIR not found; skipping patch."
  exit 0
fi

cp "$PATCH_DIR/fedmeta_agent.cc" "$AQUA_SIM_DIR/"
cp "$PATCH_DIR/fedmeta_agent.h" "$AQUA_SIM_DIR/"
cp "$PATCH_DIR/acoustic_energy.cc" "$AQUA_SIM_DIR/"

echo "Patches copied. Rebuild Aqua-Sim to activate."