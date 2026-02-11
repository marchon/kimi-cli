kimi_cli.utils.frontmatter
==========================

.. module:: kimi_cli.utils.frontmatter

Source: :file:`src/kimi_cli/utils/frontmatter.py`

Functions
---------

.. _kimi_cli.utils.frontmatter.parse_frontmatter:

parse_frontmatter
^^^^^^^^^^^^^^^^^

**Line:** 6

**Description:**

    Parse YAML frontmatter from a text blob.

    Raises:
        ValueError: If the frontmatter YAML is invalid.

**Parameters:**

    - ``text`` (*str*)

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`append <func-append>`
    - :ref:`cast <func-cast>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`join <func-join>`
    - :ref:`safe_load <func-safe_load>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.skill.__init__.parse_skill_text``
    - ``kimi_cli.utils.frontmatter.read_frontmatter``


.. _kimi_cli.utils.frontmatter.read_frontmatter:

read_frontmatter
^^^^^^^^^^^^^^^^

**Line:** 39

**Description:**

    Read the YAML frontmatter at the start of a file.

    Args:
        path: Path to an existing file that may contain frontmatter.

**Parameters:**

    - ``path`` (*Path*)

**Calls:**

    - :ref:`parse_frontmatter <func-parse_frontmatter>`
    - :ref:`read_text <func-read_text>`

