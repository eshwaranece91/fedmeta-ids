.PHONY: help install test smoke full clean docker

help:
	@echo "Targets:"
	@echo "  install   Install Python dependencies"
	@echo "  test      Run unit tests"
	@echo "  smoke     Run a quick end-to-end smoke test"
	@echo "  full      Run the full 30-seed reproduction"
	@echo "  docker    Build the Docker image"
	@echo "  clean     Remove generated results and caches"

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v

smoke:
	bash experiments/run_all.sh --config configs/sim_small.yaml --seed 0 --smoke

full:
	bash experiments/run_all.sh --seeds 0-29

docker:
	docker build -t fedmeta-ids:latest .

clean:
	rm -rf results/raw results/detection results/communication results/energy results/security results/ablation results/scalability
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete