kimi_cli.soul.message
=====================

.. module:: kimi_cli.soul.message

Source: :file:`src/kimi_cli/soul/message.py`

Functions
---------

.. _kimi_cli.soul.message.check_message:

check_message
^^^^^^^^^^^^^

**Line:** 90

**Description:**

    Check the message content, return the missing model capabilities.

**Parameters:**

    - ``message`` (*Message*)
    - ``model_capabilities`` (*set[ModelCapability]*)

**Returns:** ``set[ModelCapability]``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul._grow_context``
    - ``kimi_cli.soul.kimisoul.KimiSoul._turn``


.. _kimi_cli.soul.message.system:

system
^^^^^^

**Line:** 53

**Description:**

    System.
    
    Args:
    message: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``message`` (*str*)

**Returns:** ``ContentPart``

**Calls:**

    - :ref:`TextPart <func-TextPart>`

**Called by:**

    - ``kimi_cli.auth.oauth._device_model``
    - ``kimi_cli.soul.compaction.SimpleCompaction.compact``
    - ``kimi_cli.soul.context.Context.checkpoint``
    - ``kimi_cli.soul.kimisoul.KimiSoul._step``
    - ``kimi_cli.soul.message.tool_result_to_message``
    - ``kimi_cli.soul.slash.init``
    - ``kimi_cli.tools.file.grep_local._detect_target``
    - ``kimi_cli.tools.file.grep_local._rg_binary_name``
    - ``kimi_cli.ui.shell.update._detect_target``
    - ``kimi_cli.utils.environment.Environment.detect``


.. _kimi_cli.soul.message.tool_result_to_message:

tool_result_to_message
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 65

**Description:**

    Convert a tool result to a message.

**Parameters:**

    - ``tool_result`` (*ToolResult*)

**Returns:** ``Message``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`append <func-append>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_output_to_content_parts <func-_output_to_content_parts>`
    - :ref:`system <func-system>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul._grow_context``
    - ``kimi_cli.ui.print.visualize.JsonPrinter.flush``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_output_to_content_parts`` - Line 30
