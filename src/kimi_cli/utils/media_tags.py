from __future__ import annotations
from collections.abc import Mapping
from html import escape
from kimi_cli.wire.types import ContentPart, TextPart

# Internal Function Index:
#
#   [func] _format_tag




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


def _format_tag(tag: str, attrs: Mapping[str, str | None] | None = None) -> str:
    """
     Format Tag.
    
    Args:
    tag: Description.
    attrs: Description.
    
    Returns:
        Description.
    """
    if not attrs:
        return f"<{tag}>"
    rendered: list[str] = []
    for key, value in sorted(attrs.items()):
        if not value:
            continue
        rendered.append(f'{key}="{escape(str(value), quote=True)}"')
    if not rendered:
        return f"<{tag}>"
    return f"<{tag} " + " ".join(rendered) + ">"

def wrap_media_part(
    part: ContentPart, *, tag: str, attrs: Mapping[str, str | None] | None = None
) -> list[ContentPart]:
    """
    Wrap Media Part.
    
    Args:
    part: Description.
    tag: Description.
    attrs: Description.
    
    Returns:
        Description.
    """
    return [
        TextPart(text=_format_tag(tag, attrs)),
        part,
        TextPart(text=f"</{tag}>"),
    ]
