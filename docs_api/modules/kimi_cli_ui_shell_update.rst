kimi_cli.ui.shell.update
========================

.. module:: kimi_cli.ui.shell.update

Source: :file:`src/kimi_cli/ui/shell/update.py`

Classes
-------

.. _class-UpdateResult:

UpdateResult
^^^^^^^^^^^^

UpdateResult class.


Functions
---------

.. _kimi_cli.ui.shell.update.do_update:

do_update
^^^^^^^^^

**Line:** 118

**Description:**

    Do Update.
    
    Args:
    print: Description.
    check\_only: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``print`` (*bool*) = ``True``
    - ``check_only`` (*bool*) = ``False``

**Returns:** ``UpdateResult``

**Calls:**

    - :ref:`_do_update <func-_do_update>`

**Called by:**

    - ``kimi_cli.ui.shell.__init__.Shell._auto_update``


.. _kimi_cli.ui.shell.update.semver_tuple:

semver_tuple
^^^^^^^^^^^^

**Line:** 26

**Description:**

    Semver Tuple.
    
    Args:
    version: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``version`` (*str*)

**Calls:**

    - :ref:`group <func-group>`
    - :ref:`int <func-int>`
    - :ref:`match <func-match>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.ui.shell.__init__._print_welcome_info``
    - ``kimi_cli.ui.shell.update._do_update``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_detect_target`` - Line 75
- ``_do_update`` - Line 132
- ``_get_latest_version`` - Line 99
