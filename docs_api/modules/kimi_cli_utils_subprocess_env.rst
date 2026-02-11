kimi_cli.utils.subprocess_env
=============================

.. module:: kimi_cli.utils.subprocess_env

Source: :file:`src/kimi_cli/utils/subprocess_env.py`

Functions
---------

.. _kimi_cli.utils.subprocess_env.get_clean_env:

get_clean_env
^^^^^^^^^^^^^

**Line:** 35

**Description:**

    Get a clean environment suitable for spawning subprocesses.

    In a PyInstaller-frozen application on Linux, this function restores
    the original library path environment variables, preventing su

**Parameters:**

    - ``base_env`` = ``None``

**Calls:**

    - :ref:`dict <func-dict>`
    - :ref:`getattr <func-getattr>`

**Called by:**

    - ``kimi_cli.tools.shell.__init__.Shell._run_shell_command``
    - ``kimi_cli.ui.shell.__init__.Shell._run_shell_command``
    - ``kimi_cli.web.api.sessions.get_session_git_diff``
    - ``kimi_cli.web.runner.process.SessionProcess.start``

