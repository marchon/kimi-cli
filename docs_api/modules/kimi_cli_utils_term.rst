kimi_cli.utils.term
===================

.. module:: kimi_cli.utils.term

Source: :file:`src/kimi_cli/utils/term.py`

Functions
---------

.. _kimi_cli.utils.term.ensure_new_line:

ensure_new_line
^^^^^^^^^^^^^^^

**Line:** 166

**Description:**

    Ensure the next prompt starts at column 0 regardless of prior command output.

**Returns:** ``None``

**Calls:**

    - :ref:`isatty <func-isatty>`
    - :ref:`_cursor_column_unix <func-_cursor_column_unix>`
    - :ref:`_cursor_column_windows <func-_cursor_column_windows>`
    - :ref:`_write_newline <func-_write_newline>`

**Called by:**

    - ``kimi_cli.ui.shell.__init__.Shell.run``


.. _kimi_cli.utils.term.ensure_tty_sane:

ensure_tty_sane
^^^^^^^^^^^^^^^

**Line:** 68

**Description:**

    Restore basic tty settings so Ctrl-C works after raw-mode operations.

**Returns:** ``None``

**Calls:**

    - :ref:`fileno <func-fileno>`
    - :ref:`isatty <func-isatty>`
    - :ref:`suppress <func-suppress>`
    - :ref:`tcgetattr <func-tcgetattr>`
    - :ref:`tcsetattr <func-tcsetattr>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.ui.shell.__init__.Shell.run``


.. _kimi_cli.utils.term.get_cursor_row:

get_cursor_row
^^^^^^^^^^^^^^

**Line:** 133

**Description:**

    Get the current cursor row (1-indexed).

**Returns:** ``int | None``

**Calls:**

    - :ref:`isatty <func-isatty>`
    - :ref:`_cursor_position_unix <func-_cursor_position_unix>`
    - :ref:`_cursor_position_windows <func-_cursor_position_windows>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_cursor_column_unix`` - Line 145
- ``_cursor_column_windows`` - Line 152
- ``_cursor_position_unix`` - Line 27
- ``_cursor_position_windows`` - Line 92
- ``_write_newline`` - Line 159
