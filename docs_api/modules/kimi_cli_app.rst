kimi_cli.app
============

.. module:: kimi_cli.app

Source: :file:`src/kimi_cli/app.py`

Classes
-------

.. _class-KimiCLI:

KimiCLI
^^^^^^^

KimiCLI class.


Functions
---------

.. _kimi_cli.app.enable_logging:

enable_logging
^^^^^^^^^^^^^^

**Line:** 31

**Description:**

    Enable Logging.
    
    Args:
    debug: Description.
    redirect\_stderr: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``debug`` (*bool*) = ``False``
    - ``redirect_stderr`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`enable <func-enable>`
    - :ref:`get_share_dir <func-get_share_dir>`
    - :ref:`redirect_stderr_to_logger <func-redirect_stderr_to_logger>`
    - :ref:`remove <func-remove>`

**Called by:**

    - ``kimi_cli.acp.__init__.acp_main``
    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.cli.__init__.web_worker``
    - ``kimi_cli.web.runner.worker.main``


Methods
-------

- ``KimiCLI.create`` - Line 64
- ``KimiCLI.run`` - Line 210
- ``KimiCLI.run_acp`` - Line 358
- ``KimiCLI.run_print`` - Line 337
- ``KimiCLI.run_shell`` - Line 259
- ``KimiCLI.run_wire_stdio`` - Line 366
- ``KimiCLI.session`` - Line 194
- ``KimiCLI.soul`` - Line 189
