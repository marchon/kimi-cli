kimi_cli.config
===============

.. module:: kimi_cli.config

Source: :file:`src/kimi_cli/config.py`

Classes
-------

.. _class-Config:

Config
^^^^^^

Main configuration structure.


.. _class-LLMModel:

LLMModel
^^^^^^^^

LLM model configuration.


.. _class-LLMProvider:

LLMProvider
^^^^^^^^^^^

LLM provider configuration.


.. _class-LoopControl:

LoopControl
^^^^^^^^^^^

Agent loop control configuration.


.. _class-MCPClientConfig:

MCPClientConfig
^^^^^^^^^^^^^^^

MCP client configuration.


.. _class-MCPConfig:

MCPConfig
^^^^^^^^^

MCP configuration.


.. _class-MoonshotFetchConfig:

MoonshotFetchConfig
^^^^^^^^^^^^^^^^^^^

Moonshot Fetch configuration.


.. _class-MoonshotSearchConfig:

MoonshotSearchConfig
^^^^^^^^^^^^^^^^^^^^

Moonshot Search configuration.


.. _class-OAuthRef:

OAuthRef
^^^^^^^^

Reference to OAuth credentials stored outside the config file.


.. _class-Services:

Services
^^^^^^^^

Services configuration.


Functions
---------

.. _kimi_cli.config.get_config_file:

get_config_file
^^^^^^^^^^^^^^^

**Line:** 21

**Description:**

    Get the configuration file path.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - ``kimi_cli.config.load_config``
    - ``kimi_cli.config.save_config``
    - ``kimi_cli.web.api.config.get_config_toml``
    - ``kimi_cli.web.api.config.update_config_toml``


.. _kimi_cli.config.get_default_config:

get_default_config
^^^^^^^^^^^^^^^^^^

**Line:** 163

**Description:**

    Get the default configuration.

**Returns:** ``Config``

**Calls:**

    - :ref:`Config <func-Config>`
    - :ref:`Services <func-Services>`

**Called by:**

    - ``kimi_cli.config.load_config``


.. _kimi_cli.config.load_config:

load_config
^^^^^^^^^^^

**Line:** 172

**Description:**

    Load configuration from config file.
    If the config file does not exist, create it with default configuration.

    Args:
        config\_file (Path | None): Path to the configuration file. If None,

**Parameters:**

    - ``config_file`` (*Path | None*) = ``None``

**Returns:** ``Config``

**Calls:**

    - :ref:`ConfigError <func-ConfigError>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`expanduser <func-expanduser>`
    - :ref:`_migrate_json_config_to_toml <func-_migrate_json_config_to_toml>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`get_default_config <func-get_default_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`loads <func-loads>`
    - :ref:`lower <func-lower>`
    - ... and 3 more

**Called by:**

    - ``kimi_cli.acp.server.ACPServer.set_session_model``
    - ``kimi_cli.app.KimiCLI.create``
    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.cli.__init__.login``
    - ``kimi_cli.cli.__init__.logout``
    - ``kimi_cli.ui.shell.setup._apply_setup_result``
    - ``kimi_cli.ui.shell.slash.model``
    - ``kimi_cli.web.api.config._build_global_config``
    - ``kimi_cli.web.api.config.update_global_config``
    - ``kimi_cli.web.api.sessions.generate_session_title``
    - ... and 1 more


.. _kimi_cli.config.load_config_from_string:

load_config_from_string
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 221

**Description:**

    Load configuration from a TOML or JSON string.

    Args:
        config\_string (str): TOML or JSON configuration text.

    Returns:
        Validated Config object.

    Raises:
        ConfigError:

**Parameters:**

    - ``config_string`` (*str*)

**Returns:** ``Config``

**Calls:**

    - :ref:`ConfigError <func-ConfigError>`
    - :ref:`loads <func-loads>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.web.api.config.update_config_toml``


.. _kimi_cli.config.save_config:

save_config
^^^^^^^^^^^

**Line:** 259

**Description:**

    Save configuration to config file.

    Args:
        config (Config): Config object to save.
        config\_file (Path | None): Path to the configuration file. If None, use default path.

**Parameters:**

    - ``config`` (*Config*)
    - ``config_file`` (*Path | None*) = ``None``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`dumps <func-dumps>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`lower <func-lower>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`model_dump <func-model_dump>`
    - :ref:`open <func-open>`
    - :ref:`write <func-write>`

**Called by:**

    - ``kimi_cli.acp.server.ACPServer.set_session_model``
    - ``kimi_cli.auth.oauth.OAuthManager._migrate_oauth_storage``
    - ``kimi_cli.auth.oauth.login_kimi_code``
    - ``kimi_cli.auth.oauth.logout_kimi_code``
    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.config._migrate_json_config_to_toml``
    - ``kimi_cli.config.load_config``
    - ``kimi_cli.ui.shell.oauth.logout``
    - ``kimi_cli.ui.shell.setup._apply_setup_result``
    - ``kimi_cli.ui.shell.slash.model``
    - ... and 1 more


Methods
-------

- ``Config.validate_model`` - Line 155
- ``LLMProvider.dump_secret`` - Line 54
- ``MoonshotFetchConfig.dump_secret`` - Line 100
- ``MoonshotSearchConfig.dump_secret`` - Line 116

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_migrate_json_config_to_toml`` - Line 292
