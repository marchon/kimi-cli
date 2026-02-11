kimi_cli.web.api.config
=======================

.. module:: kimi_cli.web.api.config

Source: :file:`src/kimi_cli/web/api/config.py`

Classes
-------

.. _class-ConfigModel:

ConfigModel
^^^^^^^^^^^

Model configuration for frontend.


.. _class-ConfigToml:

ConfigToml
^^^^^^^^^^

Raw config.toml content.


.. _class-GlobalConfig:

GlobalConfig
^^^^^^^^^^^^

Global configuration snapshot for frontend.


.. _class-UpdateConfigTomlRequest:

UpdateConfigTomlRequest
^^^^^^^^^^^^^^^^^^^^^^^

Request to update config.toml.


.. _class-UpdateConfigTomlResponse:

UpdateConfigTomlResponse
^^^^^^^^^^^^^^^^^^^^^^^^

Response after updating config.toml.


.. _class-UpdateGlobalConfigRequest:

UpdateGlobalConfigRequest
^^^^^^^^^^^^^^^^^^^^^^^^^

Request to update global config.


.. _class-UpdateGlobalConfigResponse:

UpdateGlobalConfigResponse
^^^^^^^^^^^^^^^^^^^^^^^^^^

Response after updating global config.


Functions
---------

.. _kimi_cli.web.api.config.get_config_toml:

get_config_toml
^^^^^^^^^^^^^^^

**Line:** 115

**Description:**

    Get kimi-cli config.toml.

**Parameters:**

    - ``http_request`` (*Request*)

**Returns:** ``ConfigToml``

**Calls:**

    - :ref:`ConfigToml <func-ConfigToml>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`read_text <func-read_text>`
    - :ref:`str <func-str>`


.. _kimi_cli.web.api.config.get_global_config:

get_global_config
^^^^^^^^^^^^^^^^^

**Line:** 159

**Description:**

    Get global (kimi-cli) config snapshot.

**Returns:** ``GlobalConfig``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`_build_global_config <func-_build_global_config>`


.. _kimi_cli.web.api.config.update_config_toml:

update_config_toml
^^^^^^^^^^^^^^^^^^

**Line:** 92

**Description:**

    Update kimi-cli config.toml.

**Parameters:**

    - ``request`` (*UpdateConfigTomlRequest*)
    - ``http_request`` (*Request*)

**Returns:** ``UpdateConfigTomlResponse``

**Calls:**

    - :ref:`UpdateConfigTomlResponse <func-UpdateConfigTomlResponse>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`load_config_from_string <func-load_config_from_string>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`put <func-put>`
    - :ref:`str <func-str>`
    - :ref:`warning <func-warning>`
    - :ref:`write_text <func-write_text>`


.. _kimi_cli.web.api.config.update_global_config:

update_global_config
^^^^^^^^^^^^^^^^^^^^

**Line:** 164

**Description:**

    Update global (kimi-cli) default model/thinking.

**Parameters:**

    - ``request`` (*UpdateGlobalConfigRequest*)
    - ``http_request`` (*Request*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``UpdateGlobalConfigResponse``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`UpdateGlobalConfigResponse <func-UpdateGlobalConfigResponse>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`_build_global_config <func-_build_global_config>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`patch <func-patch>`
    - :ref:`restart_running_workers <func-restart_running_workers>`
    - :ref:`str <func-str>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_build_global_config`` - Line 127
- ``_ensure_sensitive_apis_allowed`` - Line 83
- ``_get_runner`` - Line 123
