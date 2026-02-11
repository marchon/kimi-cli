kimi_cli.tools.utils
====================

.. module:: kimi_cli.tools.utils

Source: :file:`src/kimi_cli/tools/utils.py`

Classes
-------

.. _class-ToolRejectedError:

ToolRejectedError
^^^^^^^^^^^^^^^^^

ToolRejectedError class.


.. _class-ToolResultBuilder:

ToolResultBuilder
^^^^^^^^^^^^^^^^^

Builder for tool results with character and line limits.


Functions
---------

.. _kimi_cli.tools.utils.load_desc:

load_desc
^^^^^^^^^

**Line:** 50

**Description:**

    Load a tool description from a file, rendered via Jinja2.

**Parameters:**

    - ``path`` (*Path*)
    - ``context`` = ``None``

**Returns:** ``str``

**Calls:**

    - :ref:`Environment <func-Environment>`
    - :ref:`from_string <func-from_string>`
    - :ref:`read_text <func-read_text>`
    - :ref:`render <func-render>`

**Called by:**

    - ``kimi_cli.tools.file.read.ReadFile.__init__``
    - ``kimi_cli.tools.file.read_media.ReadMediaFile.__init__``
    - ``kimi_cli.tools.multiagent.task.Task.__init__``
    - ``kimi_cli.tools.shell.__init__.Shell.__init__``


.. _kimi_cli.tools.utils.truncate_line:

truncate_line
^^^^^^^^^^^^^

**Line:** 64

**Description:**

    Truncate a line if it exceeds \`max\_length\`, preserving the beginning and the line break.
    The output may be longer than \`max\_length\` if it is too short to fit the marker.

**Parameters:**

    - ``line`` (*str*)
    - ``max_length`` (*int*)
    - ``marker`` (*str*) = ``'...'``

**Returns:** ``str``

**Calls:**

    - :ref:`group <func-group>`
    - :ref:`len <func-len>`
    - :ref:`max <func-max>`
    - :ref:`search <func-search>`

**Called by:**

    - ``kimi_cli.tools.file.read.ReadFile.__call__``
    - ``kimi_cli.tools.utils.ToolResultBuilder.write``


Methods
-------

- ``ToolResultBuilder.display`` - Line 155
- ``ToolResultBuilder.error`` - Line 186
- ``ToolResultBuilder.extras`` - Line 159
- ``ToolResultBuilder.is_full`` - Line 102
- ``ToolResultBuilder.n_chars`` - Line 107
- ``ToolResultBuilder.n_lines`` - Line 112
- ``ToolResultBuilder.ok`` - Line 165
- ``ToolResultBuilder.write`` - Line 116
