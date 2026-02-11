"""
Sphinx configuration for Kimi Code CLI API documentation.
"""

import os
import sys
from pathlib import Path

# Add src directory to path for autodoc
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Project information
project = "Kimi Code CLI"
copyright = "2025, Moonshot AI"
author = "Moonshot AI"
version = "1.12.0"
release = "1.12.0"

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__, __call__, __enter__, __exit__",
    "undoc-members": True,
    "exclude-members": "__weakref__, __dict__, __module__",
    "show-inheritance": True,
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
autoclass_content = "both"

# Autosummary settings
autosummary_generate = True
autosummary_imported_members = True

# Napoleon settings (Google/NumPy docstring support)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pydantic": ("https://docs.pydantic.dev/latest", None),
    "typer": ("https://typer.tiangolo.com", None),
    "rich": ("https://rich.readthedocs.io/en/stable", None),
}

# Templates and static files
templates_path = ["_templates"]
html_static_path = ["_static"]

# Source settings
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#2980B9",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

html_context = {
    "display_github": True,
    "github_user": "moonshot-ai",
    "github_repo": "kimi-cli",
    "github_version": "main",
    "conf_py_path": "/docs_api/",
}

# Todo settings
todo_include_todos = True

# Coverage settings
coverage_show_missing_items = True

# Pygments style
pygments_style = "sphinx"

# Keep warnings
keep_warnings = True

# Nitpicky mode for checking references
nitpicky = False
