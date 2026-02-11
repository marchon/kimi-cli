# Kimi Code CLI Documentation and Refactoring Summary

## Overview

This project has been enhanced with comprehensive Sphinx API documentation and key source files have been refactored for better code organization.

## Documentation

### Sphinx API Documentation (`docs_api/`)

A complete Sphinx documentation structure has been created:

- **`conf.py`** - Sphinx configuration with autodoc, napoleon, and intersphinx
- **`index.rst`** - Main documentation entry point with module overview
- **`quickstart.rst`** - Quick start guide for API usage
- **`architecture.rst`** - Architecture overview and design patterns
- **`ui_reference.rst`** - Complete UI options reference
- **`cli_reference.rst`** - CLI commands and options reference
- **`api/`** - API documentation for all modules:
  - `kimi_cli.rst` - Main application module
  - `kimi_cli.soul.rst` - Agent runtime
  - `kimi_cli.tools.rst` - Built-in tools
  - `kimi_cli.wire.rst` - Wire protocol
  - `kimi_cli.ui.rst` - User interfaces
  - `kimi_cli.utils.rst` - Utility modules
  - `kimi_cli.web.rst` - Web UI
  - `kimi_cli.acp.rst` - ACP server
  - `kimi_cli.auth.rst` - Authentication
  - `kimi_cli.skill.rst` - Skills system
  - `kimi_cli.cli.rst` - CLI commands

### Building Documentation

```bash
cd docs_api
pip install -r requirements.txt
make html
```

Or using uv:

```bash
uv venv docs_venv
source docs_venv/bin/activate
uv pip install -r docs_api/requirements.txt
cd docs_api
make html
```

Then open `_build/html/index.html` in your browser.

## Code Refactoring

### Refactoring Approach

Key source files have been refactored to follow a consistent structure:

1. **Public APIs at the top** - All public functions, classes, and methods are placed at the top of the file with comprehensive docstrings
2. **Internal APIs at the bottom** - Private functions (starting with `_`) are placed at the bottom in alphabetical order
3. **Clear separation** - A separator comment marks the internal API section
4. **Complete docstrings** - All public APIs have Sphinx-compatible docstrings with Args, Returns, and Raises sections

### Files Refactored

1. **`src/kimi_cli/app.py`**
   - `KimiCLI` class with public methods: `create()`, `run()`, `run_shell()`, `run_print()`, `run_acp()`, `run_wire_stdio()`
   - `enable_logging()` function
   - Internal `_env()` method at bottom

2. **`src/kimi_cli/wire/__init__.py`**
   - `Wire`, `WireSoulSide`, `WireUISide` classes
   - Internal `_WireRecorder` class at bottom

3. **`src/kimi_cli/soul/toolset.py`**
   - `KimiToolset` class with tool management methods
   - `MCPServerInfo`, `MCPTool`, `WireExternalTool` classes
   - `convert_mcp_tool_result()`, `get_current_tool_call_or_none()` functions
   - Internal `_load_tool()` method at bottom

4. **`src/kimi_cli/soul/agent.py`**
   - `Runtime`, `Agent`, `LaborMarket`, `BuiltinSystemPromptArgs` classes
   - `load_agent()` function
   - Internal `_load_agents_md()`, `_load_system_prompt()` functions at bottom

5. **`src/kimi_cli/tools/display.py`**
   - Display block classes with proper docstrings

6. **`src/kimi_cli/constant.py`**
   - Module-level constants with docstrings

### Refactoring Script

The `refactor_code.py` script is provided to automate refactoring of remaining files:

```bash
# Dry run to see what would change
python refactor_code.py --dry-run

# Refactor specific files
python refactor_code.py --files src/kimi_cli/config.py src/kimi_cli/session.py

# Refactor all files (use with caution)
python refactor_code.py
```

## Documentation Standards

### Docstring Format

All docstrings follow Google style:

```python
def function_name(arg1: type1, arg2: type2) -> return_type:
    """
    Short description.

    Longer description if needed.

    Args:
        arg1: Description of arg1.
        arg2: Description of arg2.

    Returns:
        Description of return value.

    Raises:
        ExceptionType: When this exception is raised.
    """
```

### Class Documentation

```python
class ClassName:
    """
    Short class description.

    Longer description if needed.

    Attributes:
        attr1: Description of attr1.
        attr2: Description of attr2.
    """
```

### Module Structure

```python
"""
Module docstring describing the module's purpose.
"""

# Imports
from __future__ import annotations
...

# Public constants
CONSTANT_NAME = value
"""Description of constant."""

# Public classes
class PublicClass:
    """..."""
    ...

# Public functions
def public_function():
    """..."""
    ...

# ==============================================================================
# INTERNAL API
# ==============================================================================
# The following are for internal use only and may change without notice.

def _internal_function():
    """..."""
    ...
```

## API Quick Reference

### Main Entry Points

```python
from kimi_cli.app import KimiCLI, enable_logging
from kimi_cli.session import Session
from kimi_cli.config import load_config

# Enable logging
enable_logging(debug=False)

# Create a session
session = await Session.create()

# Create CLI instance
cli = await KimiCLI.create(session)

# Run with shell UI
await cli.run_shell()
```

### Wire Protocol

```python
from kimi_cli.wire import Wire

wire = Wire()
wire.soul_side.send(message)
msg = await wire.ui_side(merge=True).receive()
```

### Tool System

```python
from kimi_cli.soul.toolset import KimiToolset

toolset = KimiToolset()
toolset.load_tools(["kimi_cli.tools.shell:Shell"], dependencies)
```

## Next Steps

1. **Review refactored files** - Check the refactored files for correctness
2. **Run tests** - Ensure all tests pass after refactoring
3. **Complete refactoring** - Use `refactor_code.py` for remaining files
4. **Enhance documentation** - Add more examples and tutorials
5. **Publish documentation** - Deploy to Read the Docs or GitHub Pages

## Contributing

When adding new code:

1. Place public APIs at the top of the file
2. Add comprehensive docstrings
3. Place internal helpers at the bottom
4. Update API documentation if adding new modules
5. Run `make html` in `docs_api/` to verify docs build
