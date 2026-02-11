kimi_cli.acp.convert
====================

.. module:: kimi_cli.acp.convert

Source: :file:`src/kimi_cli/acp/convert.py`

Functions
---------

.. _kimi_cli.acp.convert.acp_blocks_to_content_parts:

acp_blocks_to_content_parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 14

**Description:**

    Acp Blocks To Content Parts.
    
    Args:
    prompt: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``prompt`` (*list[ACPContentBlock]*)

**Returns:** ``list[ContentPart]``

**Calls:**

    - :ref:`ImageURLPart <func-ImageURLPart>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`append <func-append>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.acp.session.ACPSession.prompt``


.. _kimi_cli.acp.convert.display_block_to_acp_content:

display_block_to_acp_content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 41

**Description:**

    Display Block To Acp Content.
    
    Args:
    block: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``block`` (*DisplayBlock*)

**Returns:** ``acp.schema.FileEditToolCallContent | None``

**Calls:**

    - :ref:`FileEditToolCallContent <func-FileEditToolCallContent>`
    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - ``kimi_cli.acp.convert.tool_result_to_acp_content``
    - ``kimi_cli.acp.session.ACPSession._handle_approval_request``


.. _kimi_cli.acp.convert.tool_result_to_acp_content:

tool_result_to_acp_content
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 63

**Description:**

    Tool Result To Acp Content.
    
    Args:
    tool\_ret: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_ret`` (*ToolReturnValue*)

**Returns:** ``list[acp.schema.ContentToolCallContent | acp.schema.FileEditToolCallContent | acp.schema.TerminalToolCallContent]``

**Calls:**

    - :ref:`ContentToolCallContent <func-ContentToolCallContent>`
    - :ref:`TextContentBlock <func-TextContentBlock>`
    - :ref:`_to_text_block <func-_to_text_block>`
    - :ref:`append <func-append>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`display_block_to_acp_content <func-display_block_to_acp_content>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.acp.session.ACPSession._send_tool_result``

