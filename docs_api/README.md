# Kimi Code CLI API Documentation

This directory contains the Sphinx-generated API documentation for Kimi Code CLI.

## Building the Documentation

### Prerequisites

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv pip install -r requirements.txt
```

### Build HTML Documentation

```bash
cd docs_api
make html
```

On Windows:

```bash
cd docs_api
make.bat html
```

### View the Documentation

After building, open `_build/html/index.html` in your browser:

```bash
open _build/html/index.html  # macOS
xdg-open _build/html/index.html  # Linux
```

### Live Reload (Development)

```bash
make livehtml
```

This starts a development server that automatically rebuilds when files change.

## Documentation Structure

- `index.rst` - Main documentation entry point
- `quickstart.rst` - Quick start guide
- `architecture.rst` - Architecture overview
- `ui_reference.rst` - UI options reference
- `cli_reference.rst` - CLI commands reference
- `api/` - API reference for all modules

## Adding Documentation

To add documentation for a new module:

1. Create a new `.rst` file in `api/`
2. Add the module to `api/modules.rst`
3. Run `make html` to build

## Documentation Standards

- Use Google-style docstrings
- Include type hints
- Document all public APIs
- Keep internal APIs in a separate section

## Generating API Docs Automatically

To regenerate API documentation from source code:

```bash
sphinx-apidoc -o api ../src/kimi_cli --force --module-first
```

Note: This will overwrite existing files, so review changes before committing.
