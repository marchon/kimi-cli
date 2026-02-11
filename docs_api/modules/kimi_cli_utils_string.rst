kimi_cli.utils.string
=====================

.. module:: kimi_cli.utils.string

Source: :file:`src/kimi_cli/utils/string.py`

Functions
---------

.. _kimi_cli.utils.string.random_string:

random_string
^^^^^^^^^^^^^

**Line:** 6

**Description:**

    Generate a random string of fixed length.

**Parameters:**

    - ``length`` (*int*) = ``8``

**Returns:** ``str``

**Calls:**

    - :ref:`choice <func-choice>`
    - :ref:`join <func-join>`
    - :ref:`range <func-range>`

**Called by:**

    - ``kimi_cli.ui.shell.prompt.AttachmentCache._reserve_id``


.. _kimi_cli.utils.string.shorten_middle:

shorten_middle
^^^^^^^^^^^^^^

**Line:** 28

**Description:**

    Shorten the text by inserting ellipsis in the middle.

**Parameters:**

    - ``text`` (*str*)
    - ``width`` (*int*)
    - ``remove_newline`` (*bool*) = ``True``

**Returns:** ``str``

**Calls:**

    - :ref:`len <func-len>`
    - :ref:`sub <func-sub>`

**Called by:**

    - ``kimi_cli.tools.__init__.extract_key_argument``

