kimi_cli.utils.diff
===================

.. module:: kimi_cli.utils.diff

Source: :file:`src/kimi_cli/utils/diff.py`

Functions
---------

.. _kimi_cli.utils.diff.build_diff_blocks:

build_diff_blocks
^^^^^^^^^^^^^^^^^

**Line:** 8

**Description:**

    Build diff display blocks grouped with small context windows.

**Parameters:**

    - ``path`` (*str*)
    - ``old_text`` (*str*)
    - ``new_text`` (*str*)

**Returns:** ``list[DiffDisplayBlock]``

**Calls:**

    - :ref:`DiffDisplayBlock <func-DiffDisplayBlock>`
    - :ref:`SequenceMatcher <func-SequenceMatcher>`
    - :ref:`append <func-append>`
    - :ref:`get_grouped_opcodes <func-get_grouped_opcodes>`
    - :ref:`join <func-join>`
    - :ref:`splitlines <func-splitlines>`

**Called by:**

    - ``kimi_cli.tools.file.replace.StrReplaceFile.__call__``
    - ``kimi_cli.tools.file.write.WriteFile.__call__``


.. _kimi_cli.utils.diff.format_unified_diff:

format_unified_diff
^^^^^^^^^^^^^^^^^^^

**Line:** 34

**Description:**

    Format a unified diff between old\_text and new\_text.

    Args:
        old\_text: The original text.
        new\_text: The new text.
        path: Optional file path for the diff header.
        inclu

**Parameters:**

    - ``old_text`` (*str*)
    - ``new_text`` (*str*)
    - ``path`` (*str*) = ``''``
    - ``include_file_header`` (*bool*) = ``True``

**Returns:** ``str``

**Calls:**

    - :ref:`endswith <func-endswith>`
    - :ref:`join <func-join>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`startswith <func-startswith>`
    - :ref:`unified_diff <func-unified_diff>`

**Called by:**

    - ``kimi_cli.ui.shell.visualize._ApprovalRequestPanel.__init__``

