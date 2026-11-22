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

## Configuration

Qwangler reads an optional TOML config file at:

```text
<user-config-dir>/redrum/config.toml
```

The config directory is determined by [`platformdirs`](https://pypi.org/project/platformdirs/) using the app name `redrum` and author `lbrc`. For example, on Linux this is typically:

```text
~/.config/redrum/config.toml
```

To print the exact path on your system:

```bash
uv run python -c "from platformdirs import PlatformDirs; print(PlatformDirs('redrum', 'lbrc').user_config_dir)"
```

If the config file does not exist, Qwangler uses built-in defaults. If it exists, values in the file override the defaults; any settings you omit keep their default values.

### Creating a config file

1. Create the config directory if needed (example for Linux):

   ```bash
   mkdir -p ~/.config/redrum
   ```

2. Create `config.toml` in that directory and add any settings you want to override.

### Available settings

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `music_path` | string (path) | Your user music directory (from `platformdirs`) | Root directory of your music library. Supports `~` expansion. |
| `playlist_path` | string (path) | `<music_path>/playlists` | Directory used for playlists. Supports `~` expansion. |
| `audio_suffixes` | array of strings | `[".mp3", ".flac"]` | File extensions treated as audio files. Include the leading dot and use lowercase extensions (e.g. `".mp3"`). |
| `playlist_suffixes` | array of strings | `[".m3u", ".m3u8"]` | File extensions treated as playlist files. Include the leading dot and use lowercase extensions. When saving, if the chosen filename extension is not in this list, Qwangler uses `.m3u`. |

### Example `config.toml`

```toml
# Paths can use ~ for your home directory
music_path = "~/Music"
playlist_path = "~/Music/playlists"

# File types recognized by Qwangler
audio_suffixes = [".mp3", ".flac", ".ogg", ".m4a"]
playlist_suffixes = [".m3u", ".m3u8"]
```

## Contributing

1. Fork or clone the repo
2. Create a feature branch (`git checkout -b feature/something`)
3. Write tests first, then implement
4. Run `ruff check . && ruff format .` to ensure style compliance
5. Submit a PR

#

---
