kimi_cli.utils.rich.__init__
============================

.. module:: kimi_cli.utils.rich.__init__

Source: :file:`src/kimi_cli/utils/rich/__init__.py`

Functions
---------

.. _kimi_cli.utils.rich.__init__.enable_character_wrap:

enable_character_wrap
^^^^^^^^^^^^^^^^^^^^^

**Line:** 26

**Description:**

    Switch Rich's wrapping logic to break on every character.

    Rich's default behavior tries to preserve whole words; we override the
    internal regex so markdown rendering can fold text at any colu

**Returns:** ``None``


.. _kimi_cli.utils.rich.__init__.restore_word_wrap:

restore_word_wrap
^^^^^^^^^^^^^^^^^

**Line:** 40

**Description:**

    Restore Rich's default word-based wrapping.

**Returns:** ``None``

