from __future__ import annotations
from rich.console import Console
from rich.theme import Theme

# Internal Function Index:
#
#   [func] _NEUTRAL_MARKDOWN_THEME




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


_NEUTRAL_MARKDOWN_THEME = Theme(
    {
        "markdown.paragraph": "none",
        "markdown.block_quote": "none",
        "markdown.hr": "none",
        "markdown.item": "none",
        "markdown.item.bullet": "none",
        "markdown.item.number": "none",
        "markdown.link": "none",
        "markdown.link_url": "none",
        "markdown.h1": "none",
        "markdown.h1.border": "none",
        "markdown.h2": "none",
        "markdown.h3": "none",
        "markdown.h4": "none",
        "markdown.h5": "none",
        "markdown.h6": "none",
        "markdown.em": "none",
        "markdown.strong": "none",
        "markdown.s": "none",
        "status.spinner": "none",
    },
    inherit=True,
)

console = Console(highlight=False, theme=_NEUTRAL_MARKDOWN_THEME)
