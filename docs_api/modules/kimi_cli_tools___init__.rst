kimi_cli.tools.__init__
=======================

.. module:: kimi_cli.tools.__init__

Source: :file:`src/kimi_cli/tools/__init__.py`

Classes
-------

.. _class-SkipThisTool:

SkipThisTool
^^^^^^^^^^^^

Raised when a tool decides to skip itself from the loading process.


Functions
---------

.. _kimi_cli.tools.__init__.extract_key_argument:

extract_key_argument
^^^^^^^^^^^^^^^^^^^^

**Line:** 43

**Description:**

    Extract Key Argument.
    
    Args:
    json\_content: Description.
    tool\_name: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``json_content`` (*str | streamingjson.Lexer*)
    - ``tool_name`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`cast <func-cast>`
    - :ref:`complete_json <func-complete_json>`
    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`join <func-join>`
    - :ref:`_normalize_path <func-_normalize_path>`
    - :ref:`shorten_middle <func-shorten_middle>`
    - :ref:`loads <func-loads>`
    - :ref:`str <func-str>`

**Called by:**

    - ``kimi_cli.acp.session._ToolCallState.get_title``
    - ``kimi_cli.ui.shell.visualize._ToolCallBlock.__init__``
    - ``kimi_cli.ui.shell.visualize._ToolCallBlock._compose``
    - ``kimi_cli.ui.shell.visualize._ToolCallBlock.append_args_part``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_normalize_path`` - Line 28
