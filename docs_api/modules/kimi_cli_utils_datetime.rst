kimi_cli.utils.datetime
=======================

.. module:: kimi_cli.utils.datetime

Source: :file:`src/kimi_cli/utils/datetime.py`

Functions
---------

.. _kimi_cli.utils.datetime.format_duration:

format_duration
^^^^^^^^^^^^^^^

**Line:** 3

**Description:**

    Format a duration in seconds using short units.

**Parameters:**

    - ``seconds`` (*int*)

**Returns:** ``str``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`divmod <func-divmod>`
    - :ref:`join <func-join>`
    - :ref:`timedelta <func-timedelta>`

**Called by:**

    - ``kimi_cli.ui.shell.usage._format_reset_time``
    - ``kimi_cli.ui.shell.usage._reset_hint``


.. _kimi_cli.utils.datetime.format_relative_time:

format_relative_time
^^^^^^^^^^^^^^^^^^^^

**Line:** 20

**Description:**

    Format a timestamp as a relative time string.

**Parameters:**

    - ``timestamp`` (*float*)

**Returns:** ``str``

**Calls:**

    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`int <func-int>`
    - :ref:`now <func-now>`
    - :ref:`strftime <func-strftime>`
    - :ref:`timedelta <func-timedelta>`
    - :ref:`total_seconds <func-total_seconds>`

**Called by:**

    - ``kimi_cli.ui.shell.slash.list_sessions``

