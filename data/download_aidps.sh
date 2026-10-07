#!/usr/bin/env bash
# Download AIDPS Lab Underwater Dataset from IEEE DataPort.
# NOTE: IEEE DataPort requires authentication. Set IEEE_DATAPORT_TOKEN.
set -euo pipefail

OUT_DIR="data/raw/aidps"
mkdir -p "$OUT_DIR"

if [[ -z "${IEEE_DATAPORT_TOKEN:-}" ]]; then
  echo "ERROR: set IEEE_DATAPORT_TOKEN before running."
  echo "Obtain a token from https://ieee-dataport.org/user/login"
  exit 1
fi

DATASET_URL="https://ieee-dataport.org/open-access/aidps-adaptive-intrusion-detection-and-prevention-system-underwater-acoustic-sensor"

echo "Please download the AIDPS dataset manually from:"
echo "  $DATASET_URL"
echo "Then place the CSV files in: $OUT_DIR"