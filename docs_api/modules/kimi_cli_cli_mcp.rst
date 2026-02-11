kimi_cli.cli.mcp
================

.. module:: kimi_cli.cli.mcp

Source: :file:`src/kimi_cli/cli/mcp.py`

Functions
---------

.. _kimi_cli.cli.mcp.get_global_mcp_config_file:

get_global_mcp_config_file
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 8

**Description:**

    Get the global MCP config file path.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.cli.mcp._load_mcp_config``
    - ``kimi_cli.cli.mcp._save_mcp_config``
    - ``kimi_cli.cli.mcp.mcp_add``
    - ``kimi_cli.cli.mcp.mcp_list``
    - ``kimi_cli.cli.mcp.mcp_remove``
    - ``kimi_cli.web.runner.worker.run_worker``


.. _kimi_cli.cli.mcp.mcp_add:

mcp_add
^^^^^^^

**Line:** 109

**Description:**

    Add an MCP server.

**Parameters:**

    - ``name``
    - ``server_args`` = ``None``
    - ``transport`` = ``'stdio'``
    - ``env`` = ``None``
    - ``header`` = ``None``
    - ``auth`` = ``None``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`_parse_key_value_pairs <func-_parse_key_value_pairs>`
    - :ref:`_save_mcp_config <func-_save_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`len <func-len>`
    - ... and 1 more


.. _kimi_cli.cli.mcp.mcp_auth:

mcp_auth
^^^^^^^^

**Line:** 265

**Description:**

    Authorize with an OAuth-enabled MCP server.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Client <func-Client>`
    - :ref:`Exit <func-Exit>`
    - :ref:`_auth <func-_auth>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`len <func-len>`
    - :ref:`list_tools <func-list_tools>`
    - :ref:`run <func-run>`
    - ... and 1 more


.. _kimi_cli.cli.mcp.mcp_list:

mcp_list
^^^^^^^^

**Line:** 237

**Description:**

    List all MCP servers.

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`items <func-items>`
    - :ref:`join <func-join>`
    - :ref:`_has_oauth_tokens <func-_has_oauth_tokens>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`rstrip <func-rstrip>`


.. _kimi_cli.cli.mcp.mcp_remove:

mcp_remove
^^^^^^^^^^

**Line:** 207

**Description:**

    Remove an MCP server.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`_save_mcp_config <func-_save_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`


.. _kimi_cli.cli.mcp.mcp_reset_auth:

mcp_reset_auth
^^^^^^^^^^^^^^

**Line:** 298

**Description:**

    Reset OAuth authorization for an MCP server (clear cached tokens).

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Exit <func-Exit>`
    - :ref:`FileTokenStorage <func-FileTokenStorage>`
    - :ref:`clear <func-clear>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`type <func-type>`


.. _kimi_cli.cli.mcp.mcp_test:

mcp_test
^^^^^^^^

**Line:** 321

**Description:**

    Test connection to an MCP server and list available tools.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Client <func-Client>`
    - :ref:`Exit <func-Exit>`
    - :ref:`_test <func-_test>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`len <func-len>`
    - :ref:`list_tools <func-list_tools>`
    - :ref:`run <func-run>`
    - ... and 1 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_get_mcp_server`` - Line 81
- ``_has_oauth_tokens`` - Line 220
- ``_load_mcp_config`` - Line 56
- ``_parse_key_value_pairs`` - Line 35
- ``_save_mcp_config`` - Line 76
