kimi_cli.soul.toolset
=====================

.. module:: kimi_cli.soul.toolset

Source: :file:`src/kimi_cli/soul/toolset.py`

Classes
-------

.. _class-KimiToolset:

KimiToolset
^^^^^^^^^^^

KimiToolset class.


.. _class-MCPServerInfo:

MCPServerInfo
^^^^^^^^^^^^^

MCPServerInfo class.


.. _class-MCPTool:

MCPTool
^^^^^^^

MCPTool class.


.. _class-WireExternalTool:

WireExternalTool
^^^^^^^^^^^^^^^^

WireExternalTool class.


Functions
---------

.. _kimi_cli.soul.toolset.convert_mcp_tool_result:

convert_mcp_tool_result
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 451

**Description:**

    Convert MCP tool result to kosong tool return value.

    Raises:
        ValueError: If any content part has unsupported type or mime type.

**Parameters:**

    - ``result`` (*CallToolResult*)

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`ToolError <func-ToolError>`
    - :ref:`ToolOk <func-ToolOk>`
    - :ref:`append <func-append>`
    - :ref:`convert_mcp_content <func-convert_mcp_content>`

**Called by:**

    - ``kimi_cli.soul.toolset.MCPTool.__call__``


.. _kimi_cli.soul.toolset.get_current_tool_call_or_none:

get_current_tool_call_or_none
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 50

**Description:**

    Get the current tool call or None.
    Expect to be not None when called from a \`\_\_call\_\_\` method of a tool.

**Returns:** ``ToolCall | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - ``kimi_cli.acp.session.get_current_acp_tool_call_id_or_none``
    - ``kimi_cli.soul.approval.Approval.request``
    - ``kimi_cli.soul.toolset.WireExternalTool.__call__``
    - ``kimi_cli.tools.multiagent.task.Task._run_subagent``
    - ``kimi_cli.tools.web.fetch.FetchURL._fetch_with_service``
    - ``kimi_cli.tools.web.search.SearchWeb.__call__``


Methods
-------

- ``KimiToolset.add`` - Line 82
- ``KimiToolset.cleanup`` - Line 343
- ``KimiToolset.find`` - Line 89
- ``KimiToolset.handle`` - Line 102
- ``KimiToolset.load_mcp_tools`` - Line 208
- ``KimiToolset.load_tools`` - Line 157
- ``KimiToolset.mcp_servers`` - Line 153
- ``KimiToolset.register_external_tool`` - Line 131
- ``KimiToolset.tools`` - Line 99
- ``KimiToolset.wait_for_mcp_tools`` - Line 332
