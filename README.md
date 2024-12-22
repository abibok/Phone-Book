
# Python Project Makefile Guide

This document provides instructions on how to use the provided Makefile for managing your Python project.

## Makefile Targets

### `make venv`
Creates a virtual environment named `venv` in the current directory.

### `make install`
Installs dependencies listed in the `requirements.txt` file into the virtual environment.

### `make run`
Runs the `main.py` script using the virtual environment.

### `make test`
Runs the tests in the `tests` directory using `pytest`.

### `make lint`
Runs `flake8` to lint the code in the `src` directory.

### `make clean`
Removes the `venv` directory and all `.pyc` files.

## Example Usage

```bash
# Create the virtual environment and install dependencies
make venv install

# Run the main script
make run

# Run tests and lint the code
make test lint

# Clean up the environment
make clean
```

## Prerequisites

- Python 3.6 or later must be installed on your system.
- `make` utility must be available.

## Notes

- Always activate the virtual environment before running commands manually:
  ```bash
  source venv/bin/activate
  ```
- Ensure all dependencies are listed in `requirements.txt` for successful installation.

## License

This project is open-source and available under the MIT License.
