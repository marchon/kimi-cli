kimi_cli.share
==============

.. module:: kimi_cli.share

Source: :file:`src/kimi_cli/share.py`

Functions
---------

.. _kimi_cli.share.get_share_dir:

get_share_dir
^^^^^^^^^^^^^

**Line:** 5

**Description:**

    Get the share directory path.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`
    - :ref:`getenv <func-getenv>`
    - :ref:`home <func-home>`
    - :ref:`mkdir <func-mkdir>`

**Called by:**

    - ``kimi_cli.app.enable_logging``
    - ``kimi_cli.auth.oauth._credentials_dir``
    - ``kimi_cli.auth.oauth._device_id_path``
    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.cli.mcp.get_global_mcp_config_file``
    - ``kimi_cli.config._migrate_json_config_to_toml``
    - ``kimi_cli.config.get_config_file``
    - ``kimi_cli.metadata.WorkDirMeta.sessions_dir``
    - ``kimi_cli.metadata.get_metadata_file``
    - ``kimi_cli.tools.file.grep_local._download_and_install_rg``
    - ... and 2 more

