# Qwangler — Wrangle Music Queues (Playlists)

A TUI-based music queue manager built with **Textual** and **Rich**.

## Quick Start

```bash
uv pip install -e ".[dev]"
uv run qwangler      # run the CLI
uv run python -m pytest  # run tests
```

## Project Structure

```
Qwangler/
├── qwangler/           # main application code
│   └── cli.py          # CLI entry point + core logic
├── tests/              # test suite
│   ├── __init__.py
│   ├── conftest.py     # shared fixtures
│   ├── test_media_tree.py
│   └── test_playlist_app.py
├── pyproject.toml      # build & dependency config
├── README.md           # this file
├── .gitignore          # git ignore rules
└── .ruff.toml          # ruff lint configuration
```

## Development Tools

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management and environment control.

- **Package manager**: `uv pip` — fast, lockfile-aware Python package installer (replaces `pip`)  
- **Linter**: `ruff` — fast Python linter/formatter
- **Type checker**: `ty` (mypy-compatible)
- **Test runner**: `pytest`

Run all development commands with `uv run <command>` to ensure you're using the correct environment and dependencies.

## Running the Project

```bash
# Install in development mode with dev dependencies
uv pip install -e ".[dev]"

# Run tests (use uv run to ensure correct environment)
uv run python -m pytest -v

# Lint and format
ruff check .
ruff format --check .
```

## Contributing

1. Fork or clone the repo
2. Create a feature branch (`git checkout -b feature/something`)
3. Write tests first, then implement
4. Run `ruff check . && ruff format .` to ensure style compliance
5. Submit a PR

#

---
