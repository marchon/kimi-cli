kimi_cli.utils.logging
======================

.. module:: kimi_cli.utils.logging

Source: :file:`src/kimi_cli/utils/logging.py`

Classes
-------

.. _class-StderrRedirector:

StderrRedirector
^^^^^^^^^^^^^^^^

StderrRedirector class.


Functions
---------

.. _kimi_cli.utils.logging.open_original_stderr:

open_original_stderr
^^^^^^^^^^^^^^^^^^^^

**Line:** 113

**Description:**

    Open Original Stderr.

**Returns:** ``Iterator[IO[bytes] | None]``

**Calls:**

    - :ref:`close <func-close>`
    - :ref:`open_original_stderr_handle <func-open_original_stderr_handle>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.ui.shell.__init__.Shell._run_shell_command``


.. _kimi_cli.utils.logging.redirect_stderr_to_logger:

redirect_stderr_to_logger
^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 97

**Description:**

    Redirect Stderr To Logger.
    
    Args:
    level: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``level`` (*str*) = ``'ERROR'``

**Returns:** ``None``

**Calls:**

    - :ref:`StderrRedirector <func-StderrRedirector>`
    - :ref:`install <func-install>`

**Called by:**

    - ``kimi_cli.app.enable_logging``
    - ``kimi_cli.cli.__init__.kimi``


.. _kimi_cli.utils.logging.restore_stderr:

restore_stderr
^^^^^^^^^^^^^^

**Line:** 128

**Description:**

    Restore Stderr.

**Returns:** ``None``

**Calls:**

    - :ref:`uninstall <func-uninstall>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``


Methods
-------

- ``StderrRedirector.install`` - Line 25
- ``StderrRedirector.open_original_stderr_handle`` - Line 90
- ``StderrRedirector.uninstall`` - Line 48
