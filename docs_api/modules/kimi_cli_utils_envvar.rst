kimi_cli.utils.envvar
=====================

.. module:: kimi_cli.utils.envvar

Source: :file:`src/kimi_cli/utils/envvar.py`

Functions
---------

.. _kimi_cli.utils.envvar.get_env_bool:

get_env_bool
^^^^^^^^^^^^

**Line:** 21

**Description:**

    Get Env Bool.
    
    Args:
    name: Description.
    default: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``name`` (*str*)
    - ``default`` (*bool*) = ``False``

**Returns:** ``bool``

**Calls:**

    - :ref:`getenv <func-getenv>`
    - :ref:`lower <func-lower>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.ui.shell.__init__.Shell.run``

