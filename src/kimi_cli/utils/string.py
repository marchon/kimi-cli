from __future__ import annotations
import random
import re
import string

def random_string(length: int = 8) -> str:
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

# Internal Function Index:
#
#   [func] _NEWLINE_RE




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


_NEWLINE_RE = re.compile(r"[\r\n]+")

def shorten_middle(text: str, width: int, remove_newline: bool = True) -> str:
    """Shorten the text by inserting ellipsis in the middle."""
    if len(text) <= width:
        return text
    if remove_newline:
        text = _NEWLINE_RE.sub(" ", text)
    return text[: width // 2] + "..." + text[-width // 2 :]
