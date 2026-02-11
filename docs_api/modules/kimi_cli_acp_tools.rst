kimi_cli.acp.tools
==================

.. module:: kimi_cli.acp.tools

Source: :file:`src/kimi_cli/acp/tools.py`

Classes
-------

.. _class-HideOutputDisplayBlock:

HideOutputDisplayBlock
^^^^^^^^^^^^^^^^^^^^^^

A special DisplayBlock that indicates output should be hidden in ACP clients.


.. _class-Terminal:

Terminal
^^^^^^^^

Terminal class.


Functions
---------

.. _kimi_cli.acp.tools.replace_tools:

replace_tools
^^^^^^^^^^^^^

**Line:** 20

**Description:**

    Replace Tools.
    
    Args:
    client\_capabilities: Description.
    acp\_conn: Description.
    acp\_session\_id: Description.
    toolset: Description.
    runtime: Description.
    
    Returns:
  

**Parameters:**

    - ``client_capabilities`` (*acp.schema.ClientCapabilities*)
    - ``acp_conn`` (*acp.Client*)
    - ``acp_session_id`` (*str*)
    - ``toolset`` (*KimiToolset*)
    - ``runtime`` (*Runtime*)

**Returns:** ``None``

**Calls:**

    - :ref:`Terminal <func-Terminal>`
    - :ref:`add <func-add>`
    - :ref:`find <func-find>`
    - :ref:`get_current_kaos <func-get_current_kaos>`

**Called by:**

    - ``kimi_cli.acp.server.ACPServer.load_session``
    - ``kimi_cli.acp.server.ACPServer.new_session``

