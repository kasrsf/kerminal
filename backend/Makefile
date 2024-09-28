IMAGE_NAME := kerminal
IMAGE_TAG := latest
VENV_NAME := .venv

.PHONY: ensure-uv
ensure-uv:
	@command -v uv >/dev/null 2>&1 || { echo ">> uv is not installed. Installing uv..."; pip install uv; }


.PHONY: venv
venv: ensure-uv
	@if [ ! -d "$(VENV_NAME)" ]; then \
		echo "Creating virtual environment..."; \
		uv venv $(VENV_NAME); \
	else \
		echo "Virtual environment already exists."; \
	fi

.PHONY: setup
setup: venv
	uv pip install -e ".[dev]"

.PHONY: test
test: setup
	uv run pytest tests

.PHONY: format
format: setup
	uv run ruff format src tests

.PHONY: lint
lint: setup
	uv run ruff check --fix src tests

.PHONY: run-api
run-api: setup
	uv run python -m kerminal.api.main

.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf build dist *.egg-info

.PHONY: quality
quality: format lint test

.PHONY: all
all: install quality

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  setup           - Install project dependencies including dev packages"
	@echo "  test            - Run tests"
	@echo "  format          - Format code using ruff"
	@echo "  lint            - Lint code using ruff"
	@echo "  docker-build    - Build Docker image"
	@echo "  clean           - Clean up generated files"
	@echo "  quality         - Run formatter, linter, and tests"
	@echo "  all             - Install dependencies and run quality checks"
	@echo "  help            - Show this help message"
