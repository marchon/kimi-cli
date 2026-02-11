kimi_cli.auth.platforms
=======================

.. module:: kimi_cli.auth.platforms

Source: :file:`src/kimi_cli/auth/platforms.py`

Classes
-------

.. _class-ModelInfo:

ModelInfo
^^^^^^^^^

Model information returned from the API.


.. _class-Platform:

Platform
^^^^^^^^

Platform class.


Functions
---------

.. _kimi_cli.auth.platforms.get_platform_by_id:

get_platform_by_id
^^^^^^^^^^^^^^^^^^

**Line:** 104

**Description:**

    Get Platform By Id.
    
    Args:
    platform\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - ``kimi_cli.auth.oauth._apply_kimi_code_config``
    - ``kimi_cli.auth.oauth.login_kimi_code``
    - ``kimi_cli.auth.platforms.get_platform_name_for_provider``
    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.ui.shell.usage._usage_url``


.. _kimi_cli.auth.platforms.get_platform_by_name:

get_platform_by_name
^^^^^^^^^^^^^^^^^^^^

**Line:** 116

**Description:**

    Get Platform By Name.
    
    Args:
    name: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``name`` (*str*)

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - ``kimi_cli.ui.shell.setup.select_platform``


.. _kimi_cli.auth.platforms.get_platform_name_for_provider:

get_platform_name_for_provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 179

**Description:**

    Get Platform Name For Provider.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`get_platform_by_id <func-get_platform_by_id>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`

**Called by:**

    - ``kimi_cli.ui.shell.slash.model``


.. _kimi_cli.auth.platforms.is_managed_provider_key:

is_managed_provider_key
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 167

**Description:**

    Is Managed Provider Key.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`startswith <func-startswith>`

**Called by:**

    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.ui.shell.oauth.logout``


.. _kimi_cli.auth.platforms.list_models:

list_models
^^^^^^^^^^^

**Line:** 262

**Description:**

    List Models.
    
    Args:
    platform: Description.
    api\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform`` (*Platform*)
    - ``api_key`` (*str*)

**Returns:** ``list[ModelInfo]``

**Calls:**

    - :ref:`_list_models <func-_list_models>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`startswith <func-startswith>`
    - :ref:`tuple <func-tuple>`

**Called by:**

    - ``kimi_cli.auth.oauth.login_kimi_code``
    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.ui.shell.setup._setup_platform``


.. _kimi_cli.auth.platforms.managed_model_key:

managed_model_key
^^^^^^^^^^^^^^^^^

**Line:** 140

**Description:**

    Managed Model Key.
    
    Args:
    platform\_id: Description.
    model\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)
    - ``model_id`` (*str*)

**Returns:** ``str``

**Called by:**

    - ``kimi_cli.auth.oauth._apply_kimi_code_config``
    - ``kimi_cli.auth.platforms._apply_models``
    - ``kimi_cli.ui.shell.setup._apply_setup_result``


.. _kimi_cli.auth.platforms.managed_provider_key:

managed_provider_key
^^^^^^^^^^^^^^^^^^^^

**Line:** 128

**Description:**

    Managed Provider Key.
    
    Args:
    platform\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)

**Returns:** ``str``

**Called by:**

    - ``kimi_cli.auth.oauth.OAuthManager._apply_access_token``
    - ``kimi_cli.auth.oauth.OAuthManager._kimi_code_ref``
    - ``kimi_cli.auth.oauth._apply_kimi_code_config``
    - ``kimi_cli.auth.oauth.logout_kimi_code``
    - ``kimi_cli.ui.shell.setup._apply_setup_result``


.. _kimi_cli.auth.platforms.parse_managed_provider_key:

parse_managed_provider_key
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 153

**Description:**

    Parse Managed Provider Key.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`removeprefix <func-removeprefix>`
    - :ref:`startswith <func-startswith>`

**Called by:**

    - ``kimi_cli.auth.platforms.get_platform_name_for_provider``
    - ``kimi_cli.auth.platforms.refresh_managed_models``
    - ``kimi_cli.ui.shell.oauth.logout``
    - ``kimi_cli.ui.shell.usage._usage_url``


.. _kimi_cli.auth.platforms.refresh_managed_models:

refresh_managed_models
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 195

**Description:**

    Refresh Managed Models.
    
    Args:
    config: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`error <func-error>`
    - :ref:`get_secret_value <func-get_secret_value>`
    - :ref:`items <func-items>`
    - :ref:`load_tokens <func-load_tokens>`
    - :ref:`_apply_models <func-_apply_models>`
    - :ref:`get_platform_by_id <func-get_platform_by_id>`
    - :ref:`is_managed_provider_key <func-is_managed_provider_key>`
    - :ref:`list_models <func-list_models>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`
    - ... and 3 more

**Called by:**

    - ``kimi_cli.ui.shell.slash.model``


Methods
-------

- ``ModelInfo.capabilities`` - Line 24

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_apply_models`` - Line 332
- ``_kimi_code_base_url`` - Line 70
- ``_list_models`` - Line 284
