from __future__ import annotations
import os

# Internal Function Index:
#
#   [func] _TRUE_VALUES




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


_TRUE_VALUES = {"1", "true", "t", "yes", "y"}

def get_env_bool(name: str, default: bool = False) -> bool:
    """
    Get Env Bool.
    
    Args:
    name: Description.
    default: Description.
    
    Returns:
        Description.
    """
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in _TRUE_VALUES
