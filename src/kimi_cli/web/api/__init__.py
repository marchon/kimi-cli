from kimi_cli.web.api import config, open_in, sessions

"""API routes."""

config_router = config.router

open_in_router = open_in.router

sessions_router = sessions.router

work_dirs_router = sessions.work_dirs_router

# Internal Function Index:
#
#   [func] __all__




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


__all__ = [
    "config_router",
    "open_in_router",
    "sessions_router",
    "work_dirs_router",
]
