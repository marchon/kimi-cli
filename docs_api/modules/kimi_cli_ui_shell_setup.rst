kimi_cli.ui.shell.setup
=======================

.. module:: kimi_cli.ui.shell.setup

Source: :file:`src/kimi_cli/ui/shell/setup.py`

Functions
---------

.. _kimi_cli.ui.shell.setup.reload:

reload
^^^^^^

**Line:** 31

**Description:**

    Reload configuration

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)


.. _kimi_cli.ui.shell.setup.select_platform:

select_platform
^^^^^^^^^^^^^^^

**Line:** 111

**Description:**

    Select Platform.

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get_platform_by_name <func-get_platform_by_name>`
    - :ref:`_prompt_choice <func-_prompt_choice>`
    - :ref:`print <func-print>`

**Called by:**

    - ``kimi_cli.ui.shell.oauth.login``


.. _kimi_cli.ui.shell.setup.setup_platform:

setup_platform
^^^^^^^^^^^^^^

**Line:** 129

**Description:**

    Setup Platform.
    
    Args:
    platform: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform`` (*Platform*)

**Returns:** ``bool``

**Calls:**

    - :ref:`_apply_setup_result <func-_apply_setup_result>`
    - :ref:`_setup_platform <func-_setup_platform>`
    - :ref:`print <func-print>`

**Called by:**

    - ``kimi_cli.ui.shell.oauth.login``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_apply_setup_result`` - Line 212
- ``_prompt_choice`` - Line 56
- ``_prompt_text`` - Line 79
- ``_setup_platform`` - Line 148
