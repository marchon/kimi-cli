kimi_cli.utils.typing
=====================

.. module:: kimi_cli.utils.typing

Source: :file:`src/kimi_cli/utils/typing.py`

Functions
---------

.. _kimi_cli.utils.typing.flatten_union:

flatten_union
^^^^^^^^^^^^^

**Line:** 4

**Description:**

    If \`tp\` is a \`UnionType\`, return its flattened arguments as a tuple.
    Otherwise, return a tuple with \`tp\` as the only element.

**Parameters:**

    - ``tp`` (*Any*)

**Calls:**

    - :ref:`extend <func-extend>`
    - :ref:`get_args <func-get_args>`
    - :ref:`get_origin <func-get_origin>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`flatten_union <func-flatten_union>`
    - :ref:`tuple <func-tuple>`

**Called by:**

    - ``kimi_cli.utils.typing.flatten_union``

