kimi_cli.utils.clipboard
========================

.. module:: kimi_cli.utils.clipboard

Source: :file:`src/kimi_cli/utils/clipboard.py`

Functions
---------

.. _kimi_cli.utils.clipboard.grab_image_from_clipboard:

grab_image_from_clipboard
^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 114

**Description:**

    Read an image from the clipboard if possible.

**Returns:** ``Image.Image | None``

**Calls:**

    - :ref:`grabclipboard <func-grabclipboard>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_open_first_image <func-_open_first_image>`
    - :ref:`_read_clipboard_file_paths_macos_native <func-_read_clipboard_file_paths_macos_native>`

**Called by:**

    - ``kimi_cli.ui.shell.prompt.CustomPromptSession._try_paste_image``


.. _kimi_cli.utils.clipboard.is_clipboard_available:

is_clipboard_available
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 11

**Description:**

    Check if the Pyperclip clipboard is available.

**Returns:** ``bool``

**Calls:**

    - :ref:`paste <func-paste>`

**Called by:**

    - ``kimi_cli.ui.shell.prompt.CustomPromptSession.__init__``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_open_first_image`` - Line 89
- ``_read_clipboard_file_paths_macos_native`` - Line 35
