# FedMeta-IDS

[![CI](https://github.com/fedmeta-ids/fedmeta-ids/actions/workflows/ci.yml/badge.svg)](https://github.com/fedmeta-ids/fedmeta-ids/actions/workflows/ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Federated Meta-Learning for Rapid Adaptation of In-Network Intrusion Detection in Heterogeneous Underwater IoT: Architecture and Case Study**

Jaganathan Logeshwaran, Rafik Hamza

---

## Overview

FedMeta-IDS is a federated meta-learning framework for rapid-adaptation intrusion
detection in heterogeneous underwater IoT. It couples decentralized meta-learning
with lightweight on-node detection so that raw traffic never leaves the node and
only compact model updates traverse the acoustic channel.

Key results (reproducible from this artifact):
- 93% F1 within 5 adaptation steps
- 54% communication overhead reduction vs. FedAvg
- 41% energy-per-detection reduction vs. FedAvg
- 12% attack success rate under moderate Byzantine poisoning

---

## Repository layout
