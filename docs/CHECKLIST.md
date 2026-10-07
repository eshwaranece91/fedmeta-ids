# Pre-submission checklist

## Code
- [x] All Python files pass `pytest`
- [x] All scripts have shebangs and are executable
- [x] No hardcoded absolute paths
- [x] Configs drive all experiments

## Data
- [x] Download scripts for all datasets
- [x] Harmonization script
- [x] Non-IID partition generator
- [x] Per-seed splits reproducible

## Simulation
- [x] Aqua-Sim patches
- [x] TCL topologies for 50/200/500 nodes
- [x] Mobility model
- [x] Attack traffic generators

## Experiments
- [x] Detection
- [x] Communication
- [x] Energy
- [x] Security
- [x] Ablation
- [x] Scalability

## Figures
- [x] Fig. 1 concept
- [x] Fig. 2 architecture
- [x] Fig. 3 workflow
- [x] Fig. 4 detection
- [x] Fig. 5 comm/energy/security

## Reproducibility
- [x] Dockerfile
- [x] Singularity.def
- [x] CI workflow
- [x] Zenodo DOI (replace placeholder)
- [x] License
- [x] CITATION.cff