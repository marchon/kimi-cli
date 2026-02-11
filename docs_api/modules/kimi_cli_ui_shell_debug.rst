kimi_cli.ui.shell.debug
=======================

.. module:: kimi_cli.ui.shell.debug

Source: :file:`src/kimi_cli/ui/shell/debug.py`

Functions
---------

.. _kimi_cli.ui.shell.debug.debug:

debug
^^^^^

**Line:** 158

**Description:**

    Debug the context

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Group <func-Group>`
    - :ref:`Panel <func-Panel>`
    - :ref:`Rule <func-Rule>`
    - :ref:`Text <func-Text>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_format_message <func-_format_message>`
    - :ref:`len <func-len>`
    - :ref:`pager <func-pager>`
    - ... and 1 more

**Called by:**

    - ``kimi_cli.acp.session.ACPSession._handle_approval_request``
    - ``kimi_cli.acp.session.ACPSession._send_tool_call``
    - ``kimi_cli.acp.session.ACPSession._send_tool_call_part``
    - ``kimi_cli.acp.session.ACPSession._send_tool_result``
    - ``kimi_cli.config.load_config``
    - ``kimi_cli.config.save_config``
    - ``kimi_cli.metadata.load_metadata``
    - ``kimi_cli.metadata.save_metadata``
    - ``kimi_cli.session.Session.continue_``
    - ``kimi_cli.session.Session.create``
    - ... and 37 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_format_content_part`` - Line 43
- ``_format_message`` - Line 104
- ``_format_tool_call`` - Line 81
