kimi_cli.acp.mcp
================

.. module:: kimi_cli.acp.mcp

Source: :file:`src/kimi_cli/acp/mcp.py`

Functions
---------

.. _kimi_cli.acp.mcp.acp_mcp_servers_to_mcp_config:

acp_mcp_servers_to_mcp_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 9

**Description:**

    Acp Mcp Servers To Mcp Config.
    
    Args:
    mcp\_servers: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``mcp_servers`` (*list[MCPServer]*)

**Returns:** ``MCPConfig``

**Calls:**

    - :ref:`MCPConfig <func-MCPConfig>`
    - :ref:`MCPConfigError <func-MCPConfigError>`
    - :ref:`_convert_acp_mcp_server <func-_convert_acp_mcp_server>`
    - :ref:`model_validate <func-model_validate>`

**Called by:**

    - ``kimi_cli.acp.server.ACPServer.load_session``
    - ``kimi_cli.acp.server.ACPServer.new_session``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_convert_acp_mcp_server`` - Line 44
