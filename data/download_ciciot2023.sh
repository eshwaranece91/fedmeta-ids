#!/usr/bin/env bash
# Download CICIoT2023 from the MDPI Sensors mirror.
set -euo pipefail

OUT_DIR="data/raw/ciciot2023"
mkdir -p "$OUT_DIR"

echo "CICIoT2023 is distributed via the University of New Brunswick."
echo "Visit: https://www.unb.ca/cic/datasets/iotdataset-2023.html"
echo "Place the CSV files in: $OUT_DIR"