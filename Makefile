# Define variables
PYTHON := python3
PIP := $(PYTHON) -m pip

.PHONY: all init install test lint format clean help

# Default target
all: help

# Initialize the project by installing dependencies
init:
	$(PIP) install --upgrade pip setuptools
	$(PIP) install -r requirements.txt

# Install dependencies
install:
	$(PIP) install -r requirements.txt

# Run tests
test:
	pytest tests/

# Lint the code
lint:
	flake8 src/

# Format the code
format:
	black src/ tests/

# Clean up generated files
clean:
	rm -rf __pycache__ .pytest_cache *.pyc *.pyo
	find . -type d -name "__pycache__" -exec rm -r {} +

# Show available targets
help:
	@echo "Available targets:"
	@echo "  init         - Set up the project (install dependencies)"
	@echo "  install      - Install dependencies from requ
