set windows-shell := ["powershell", "-Command"]

# Install dependencies from uv.lock
install:
    uv sync

# Show available recipes
default:
    @just --list

# Run the application
run:
    uv run python main.py

# Run tests
test:
    uv run pytest

# Format code
fmt:
    uv run ruff format .

# Lint code
lint:
    uv run ruff check .

# Type-check code
typecheck:
    uv run mypy .

# Run all checks
check: fmt lint typecheck test
