FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    tcl8.6 tk8.6 tcl8.6-dev tk8.6-dev \
    python3.10 python3-pip python3.10-venv \
    git wget curl unzip ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY sim/aqua-sim-patches /opt/aqua-sim-patches
RUN bash /opt/aqua-sim-patches/apply_patches.sh || true

COPY . .

CMD ["bash", "experiments/run_all.sh", "--config", "configs/sim_small.yaml", "--seed", "0"]