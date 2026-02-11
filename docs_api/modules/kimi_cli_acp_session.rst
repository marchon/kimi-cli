kimi_cli.acp.session
====================

.. module:: kimi_cli.acp.session

Source: :file:`src/kimi_cli/acp/session.py`

Classes
-------

.. _class-ACPSession:

ACPSession
^^^^^^^^^^

ACPSession class.


Functions
---------

.. _kimi_cli.acp.session.get_current_acp_tool_call_id_or_none:

get_current_acp_tool_call_id_or_none
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 101

**Description:**

    See \`\_ToolCallState.acp\_tool\_call\_id\`.

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`get_current_tool_call_or_none <func-get_current_tool_call_or_none>`

**Called by:**

    - ``kimi_cli.acp.tools.Terminal.__call__``


.. _kimi_cli.acp.session.register_terminal_tool_call_id:

register_terminal_tool_call_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 75

**Description:**

    Register Terminal Tool Call Id.
    
    Args:
    tool\_call\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_call_id`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`get <func-get>`


.. _kimi_cli.acp.session.should_hide_terminal_output:

should_hide_terminal_output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 62

**Description:**

    Should Hide Terminal Output.
    
    Args:
    tool\_call\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_call_id`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - ``kimi_cli.acp.session.ACPSession._send_tool_result``


Methods
-------

- ``ACPSession.cancel`` - Line 243
- ``ACPSession.cli`` - Line 169
- ``ACPSession.id`` - Line 164
- ``ACPSession.prompt`` - Line 173
- ``_ToolCallState.acp_tool_call_id`` - Line 124
- ``_ToolCallState.append_args_part`` - Line 133
- ``_ToolCallState.get_title`` - Line 138
