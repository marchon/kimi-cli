kimi_cli.ui.shell.usage
=======================

.. module:: kimi_cli.ui.shell.usage

Source: :file:`src/kimi_cli/ui/shell/usage.py`

Classes
-------

.. _class-UsageRow:

UsageRow
^^^^^^^^

UsageRow class.


Functions
---------

.. _kimi_cli.ui.shell.usage.usage:

usage
^^^^^

**Line:** 166

**Description:**

    Display API usage and quota information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_build_usage_panel <func-_build_usage_panel>`
    - :ref:`_fetch_usage <func-_fetch_usage>`
    - :ref:`_parse_usage_payload <func-_parse_usage_payload>`
    - :ref:`_usage_url <func-_usage_url>`
    - :ref:`print <func-print>`
    - :ref:`resolve_api_key <func-resolve_api_key>`
    - :ref:`status <func-status>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_build_usage_panel`` - Line 310
- ``_fetch_usage`` - Line 206
- ``_format_reset_time`` - Line 60
- ``_format_row`` - Line 343
- ``_limit_label`` - Line 270
- ``_parse_usage_payload`` - Line 227
- ``_ratio_color`` - Line 373
- ``_reset_hint`` - Line 96
- ``_to_int`` - Line 81
- ``_to_usage_row`` - Line 117
- ``_usage_url`` - Line 144
