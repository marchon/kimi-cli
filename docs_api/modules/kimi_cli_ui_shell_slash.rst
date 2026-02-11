kimi_cli.ui.shell.slash
=======================

.. module:: kimi_cli.ui.shell.slash

Source: :file:`src/kimi_cli/ui/shell/slash.py`

Functions
---------

.. _kimi_cli.ui.shell.slash.changelog:

changelog
^^^^^^^^^

**Line:** 263

**Description:**

    Show release notes

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`items <func-items>`
    - :ref:`lower <func-lower>`
    - :ref:`pager <func-pager>`
    - :ref:`print <func-print>`
    - :ref:`startswith <func-startswith>`


.. _kimi_cli.ui.shell.slash.clear:

clear
^^^^^

**Line:** 305

**Description:**

    Clear the context

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Reload <func-Reload>`
    - :ref:`command <func-command>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`run_soul_command <func-run_soul_command>`

**Called by:**

    - ``kimi_cli.cli.mcp.mcp_reset_auth``
    - ``kimi_cli.skill.flow.d2._iter_top_level_statements``
    - ``kimi_cli.soul.context.Context.clear``
    - ``kimi_cli.soul.context.Context.revert_to``
    - ``kimi_cli.ui.print.visualize.FinalOnlyJsonPrinter.feed``
    - ``kimi_cli.ui.print.visualize.FinalOnlyJsonPrinter.flush``
    - ``kimi_cli.ui.print.visualize.FinalOnlyTextPrinter.feed``
    - ``kimi_cli.ui.print.visualize.FinalOnlyTextPrinter.flush``
    - ``kimi_cli.ui.print.visualize.JsonPrinter.flush``
    - ``kimi_cli.ui.shell.keyboard.KeyboardListener._resume_sync``
    - ... and 12 more


.. _kimi_cli.ui.shell.slash.exit:

exit
^^^^

**Line:** 44

**Description:**

    Exit the application

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`command <func-command>`

**Called by:**

    - ``kimi_cli.web.runner.worker.main``


.. _kimi_cli.ui.shell.slash.feedback:

feedback
^^^^^^^^

**Line:** 294

**Description:**

    Submit feedback to make Kimi Code CLI better

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`open <func-open>`
    - :ref:`print <func-print>`


.. _kimi_cli.ui.shell.slash.help:

help
^^^^

**Line:** 63

**Description:**

    Show help information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`Text <func-Text>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`pager <func-pager>`
    - :ref:`print <func-print>`
    - :ref:`section <func-section>`
    - :ref:`slash_name <func-slash_name>`
    - ... and 3 more


.. _kimi_cli.ui.shell.slash.list_sessions:

list_sessions
^^^^^^^^^^^^^

**Line:** 314

**Description:**

    List sessions and resume optionally

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`ChoiceInput <func-ChoiceInput>`
    - :ref:`Reload <func-Reload>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`insert <func-insert>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`format_relative_time <func-format_relative_time>`
    - :ref:`list <func-list>`
    - :ref:`print <func-print>`
    - :ref:`prompt_async <func-prompt_async>`
    - ... and 1 more


.. _kimi_cli.ui.shell.slash.mcp:

mcp
^^^

**Line:** 366

**Description:**

    Show MCP servers and tools

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`append <func-append>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`len <func-len>`
    - :ref:`print <func-print>`
    - ... and 2 more


.. _kimi_cli.ui.shell.slash.model:

model
^^^^^

**Line:** 140

**Description:**

    Switch LLM model or thinking mode

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`ChoiceInput <func-ChoiceInput>`
    - :ref:`Reload <func-Reload>`
    - :ref:`append <func-append>`
    - :ref:`items <func-items>`
    - :ref:`get_platform_name_for_provider <func-get_platform_name_for_provider>`
    - :ref:`refresh_managed_models <func-refresh_managed_models>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`derive_model_capabilities <func-derive_model_capabilities>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - ... and 3 more


.. _kimi_cli.ui.shell.slash.version:

version
^^^^^^^

**Line:** 132

**Description:**

    Show version information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`print <func-print>`

**Called by:**

    - ``kimi_cli.auth.oauth._common_headers``
    - ``kimi_cli.utils.environment.Environment.detect``


.. _kimi_cli.ui.shell.slash.web:

web
^^^

**Line:** 358

**Description:**

    Open Kimi Code Web UI in browser

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`SwitchToWeb <func-SwitchToWeb>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_ensure_kimi_soul`` - Line 35
