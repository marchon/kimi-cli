from __future__ import annotations
import ssl
import aiohttp
import certifi

# Internal Function Index:
#
#   [func] _ssl_context




# ==============================================================================
# INTERNAL API
# ==============================================================================

# The following functions and classes are for internal use only and may change
# without notice. They are organized alphabetically for easier navigation.


_ssl_context = ssl.create_default_context(cafile=certifi.where())

def new_client_session() -> aiohttp.ClientSession:
    """
    New Client Session.
    """
    return aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=_ssl_context))
