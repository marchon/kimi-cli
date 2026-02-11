kimi_cli.utils.changelog
========================

.. module:: kimi_cli.utils.changelog

Source: :file:`src/kimi_cli/utils/changelog.py`

Classes
-------

.. _class-ReleaseEntry:

ReleaseEntry
^^^^^^^^^^^^

ReleaseEntry class.


Functions
---------

.. _kimi_cli.utils.changelog.format_release_notes:

format_release_notes
^^^^^^^^^^^^^^^^^^^^

**Line:** 5

**Description:**

    Format Release Notes.
    
    Args:
    changelog: Description.
    include\_lib\_changes: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``changelog``
    - ``include_lib_changes`` (*bool*)

**Returns:** ``str``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`items <func-items>`
    - :ref:`join <func-join>`
    - :ref:`lower <func-lower>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip <func-strip>`


.. _kimi_cli.utils.changelog.parse_changelog:

parse_changelog
^^^^^^^^^^^^^^^

**Line:** 36

**Description:**

    Parse a subset of Keep a Changelog-style markdown into a map:
    version -> (description, entries)

    Parsing rules:
    - Versions are denoted by level-2 headings starting with '## ['
      Exampl

**Parameters:**

    - ``md_text`` (*str*)

**Calls:**

    - :ref:`ReleaseEntry <func-ReleaseEntry>`
    - :ref:`append <func-append>`
    - :ref:`commit <func-commit>`
    - :ref:`find <func-find>`
    - :ref:`join <func-join>`
    - :ref:`lstrip <func-lstrip>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`startswith <func-startswith>`

