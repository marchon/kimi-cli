kimi_cli.web.app
================

.. module:: kimi_cli.web.app

Source: :file:`src/kimi_cli/web/app.py`

Functions
---------

.. _kimi_cli.web.app.create_app:

create_app
^^^^^^^^^^

**Line:** 215

**Description:**

    Create the FastAPI application for Kimi CLI web UI.

**Parameters:**

    - ``session_token`` (*str | None*) = ``None``
    - ``allowed_origins`` (*list[str] | None*) = ``None``
    - ``enforce_origin`` (*bool | None*) = ``None``
    - ``restrict_sensitive_apis`` (*bool | None*) = ``None``
    - ``max_public_path_depth`` (*int | None*) = ``None``
    - ``lan_only`` (*bool | None*) = ``None``

**Returns:** ``FastAPI``

**Calls:**

    - :ref:`FastAPI <func-FastAPI>`
    - :ref:`KimiCLIRunner <func-KimiCLIRunner>`
    - :ref:`StaticFiles <func-StaticFiles>`
    - :ref:`add_middleware <func-add_middleware>`
    - :ref:`cast <func-cast>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`get_scalar_api_reference <func-get_scalar_api_reference>`
    - :ref:`getcwd <func-getcwd>`
    - :ref:`include_router <func-include_router>`
    - ... and 7 more


.. _kimi_cli.web.app.find_available_port:

find_available_port
^^^^^^^^^^^^^^^^^^^

**Line:** 98

**Description:**

    Find an available port starting from start\_port.

    Args:
        host: Host address to bind to
        start\_port: Starting port number (1-65535)
        max\_attempts: Maximum number of ports to tr

**Parameters:**

    - ``host`` (*str*)
    - ``start_port`` (*int*)
    - ``max_attempts`` (*int*) = ``MAX_PORT_ATTEMPTS``

**Returns:** ``int``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`ValueError <func-ValueError>`
    - :ref:`bind <func-bind>`
    - :ref:`_get_address_family <func-_get_address_family>`
    - :ref:`range <func-range>`
    - :ref:`setsockopt <func-setsockopt>`
    - :ref:`socket <func-socket>`

**Called by:**

    - ``kimi_cli.web.app.run_web_server``


.. _kimi_cli.web.app.run_web_server:

run_web_server
^^^^^^^^^^^^^^

**Line:** 325

**Description:**

    Run the web server.

**Parameters:**

    - ``host`` (*str*) = ``'127.0.0.1'``
    - ``port`` (*int*) = ``DEFAULT_PORT``
    - ``reload`` (*bool*) = ``False``
    - ``open_browser`` (*bool*) = ``True``
    - ``auth_token`` (*str | None*) = ``None``
    - ``allowed_origins`` (*str | None*) = ``None``
    - ``dangerously_omit_auth`` (*bool*) = ``False``
    - ``restrict_sensitive_apis`` (*bool | None*) = ``None``
    - ``lan_only`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`Thread <func-Thread>`
    - :ref:`append <func-append>`
    - :ref:`center <func-center>`
    - :ref:`extend <func-extend>`
    - :ref:`input <func-input>`
    - :ref:`isatty <func-isatty>`
    - :ref:`join <func-join>`
    - :ref:`_get_network_addresses <func-_get_network_addresses>`
    - :ref:`_get_private_addresses <func-_get_private_addresses>`
    - ... and 19 more

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.cli.web.web``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_get_address_family`` - Line 88
- ``_get_network_addresses`` - Line 167
- ``_get_private_addresses`` - Line 163
- ``_is_local_host`` - Line 135
- ``_load_env_flag`` - Line 147
