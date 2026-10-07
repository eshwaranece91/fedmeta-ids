# Data directory

This directory holds dataset download and harmonization scripts.

Raw datasets are **not shipped** in the repository. Run the download scripts
to fetch them from their original sources.

| Dataset | Script | Size | License |
|---|---|---|---|
| CIC-IDS-2017 | `download_cicids2017.sh` | ~500 MB | CC-BY |
| AIDPS Lab Underwater | `download_aidps.sh` | ~50 MB | IEEE DataPort terms |
| CICIoT2023 | `download_ciciot2023.sh` | ~1.2 GB | CC-BY |

After downloading, run:

```bash
python data/harmonize.py --out data/harmonized/
python data/dirichlet_partition.py --dataset aidps --alpha 0.5 --nodes 500 --seed 0