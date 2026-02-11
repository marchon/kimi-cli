kimi_cli.web.auth
=================

.. module:: kimi_cli.web.auth

Source: :file:`src/kimi_cli/web/auth.py`

Classes
-------

.. _class-AuthMiddleware:

AuthMiddleware
^^^^^^^^^^^^^^

Bearer token auth, origin checks, and LAN-only mode for API routes.


Functions
---------

.. _kimi_cli.web.auth.extract_token_from_request:

extract_token_from_request
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 125

**Description:**

    Get auth token from Authorization header or query (GET-only).

**Parameters:**

    - ``request`` (*Request*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`parse_bearer_token <func-parse_bearer_token>`
    - :ref:`upper <func-upper>`

**Called by:**

    - ``kimi_cli.web.auth.AuthMiddleware.dispatch``


.. _kimi_cli.web.auth.get_client_ip:

get_client_ip
^^^^^^^^^^^^^

**Line:** 15

**Description:**

    Extract client IP from request.

    Args:
        request: The incoming request
        trust\_proxy: If True, trust X-Forwarded-For header (only enable behind trusted proxy)

**Parameters:**

    - ``request`` (*Request*)
    - ``trust_proxy`` (*bool*) = ``False``

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`split <func-split>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.auth.AuthMiddleware.dispatch``


.. _kimi_cli.web.auth.is_origin_allowed:

is_origin_allowed
^^^^^^^^^^^^^^^^^

**Line:** 98

**Description:**

    Check if an origin is allowed.

    Args:
        origin: The origin to check
        allowed\_origins: List of allowed origins.
                        - None: use default localhost regex
            

**Parameters:**

    - ``origin`` (*str*)
    - ``allowed_origins`` (*Iterable[str] | None*)

**Returns:** ``bool``

**Calls:**

    - :ref:`bool <func-bool>`
    - :ref:`list <func-list>`
    - :ref:`match <func-match>`
    - :ref:`rstrip <func-rstrip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``
    - ``kimi_cli.web.auth.AuthMiddleware.dispatch``


.. _kimi_cli.web.auth.is_private_ip:

is_private_ip
^^^^^^^^^^^^^

**Line:** 30

**Description:**

    Check if an IP address is in a private range (RFC 1918 + localhost).

    Supports both IPv4 and IPv6 addresses.

**Parameters:**

    - ``ip`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`ip_address <func-ip_address>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``
    - ``kimi_cli.web.app._get_private_addresses``
    - ``kimi_cli.web.auth.AuthMiddleware.dispatch``


.. _kimi_cli.web.auth.normalize_allowed_origins:

normalize_allowed_origins
^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 87

**Description:**

    Parse comma-separated origins into a normalized list.

**Parameters:**

    - ``value`` (*str | None*)

**Returns:** ``list[str]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`split <func-split>`

**Called by:**

    - ``kimi_cli.web.app.create_app``
    - ``kimi_cli.web.app.run_web_server``


.. _kimi_cli.web.auth.parse_bearer_token:

parse_bearer_token
^^^^^^^^^^^^^^^^^^

**Line:** 77

**Description:**

    Extract bearer token from Authorization header.

**Parameters:**

    - ``value`` (*str | None*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`lower <func-lower>`
    - :ref:`partition <func-partition>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.auth.extract_token_from_request``


.. _kimi_cli.web.auth.timing_safe_compare:

timing_safe_compare
^^^^^^^^^^^^^^^^^^^

**Line:** 46

**Description:**

    Timing-safe string comparison.

**Parameters:**

    - ``a`` (*str*)
    - ``b`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`compare_digest <func-compare_digest>`
    - :ref:`encode <func-encode>`

**Called by:**

    - ``kimi_cli.web.auth.verify_token``


.. _kimi_cli.web.auth.verify_token:

verify_token
^^^^^^^^^^^^

**Line:** 136

**Description:**

    Verify token using timing-safe comparison.

**Parameters:**

    - ``provided`` (*str | None*)
    - ``expected`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`timing_safe_compare <func-timing_safe_compare>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``
    - ``kimi_cli.web.auth.AuthMiddleware.dispatch``


Methods
-------

- ``AuthMiddleware.dispatch`` - Line 159
