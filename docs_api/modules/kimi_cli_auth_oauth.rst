kimi_cli.auth.oauth
===================

.. module:: kimi_cli.auth.oauth

Source: :file:`src/kimi_cli/auth/oauth.py`

Classes
-------

.. _class-DeviceAuthorization:

DeviceAuthorization
^^^^^^^^^^^^^^^^^^^

DeviceAuthorization class.


.. _class-OAuthDeviceExpired:

OAuthDeviceExpired
^^^^^^^^^^^^^^^^^^

Device authorization expired.


.. _class-OAuthError:

OAuthError
^^^^^^^^^^

OAuth flow error.


.. _class-OAuthEvent:

OAuthEvent
^^^^^^^^^^

OAuthEvent class.


.. _class-OAuthManager:

OAuthManager
^^^^^^^^^^^^

OAuthManager class.


.. _class-OAuthToken:

OAuthToken
^^^^^^^^^^

OAuthToken class.


.. _class-OAuthUnauthorized:

OAuthUnauthorized
^^^^^^^^^^^^^^^^^

OAuth credentials rejected.


Functions
---------

.. _kimi_cli.auth.oauth.delete_tokens:

delete_tokens
^^^^^^^^^^^^^

**Line:** 434

**Description:**

    Delete Tokens.
    
    Args:
    ref: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)

**Returns:** ``None``

**Calls:**

    - :ref:`_delete_from_file <func-_delete_from_file>`
    - :ref:`_delete_from_keyring <func-_delete_from_keyring>`

**Called by:**

    - ``kimi_cli.auth.oauth.OAuthManager._refresh_tokens``
    - ``kimi_cli.auth.oauth.logout_kimi_code``


.. _kimi_cli.auth.oauth.get_device_id:

get_device_id
^^^^^^^^^^^^^

**Line:** 231

**Description:**

    Get Device Id.

**Returns:** ``str``

**Calls:**

    - :ref:`exists <func-exists>`
    - :ref:`_device_id_path <func-_device_id_path>`
    - :ref:`_ensure_private_file <func-_ensure_private_file>`
    - :ref:`read_text <func-read_text>`
    - :ref:`strip <func-strip>`
    - :ref:`uuid4 <func-uuid4>`
    - :ref:`write_text <func-write_text>`

**Called by:**

    - ``kimi_cli.auth.oauth._common_headers``


.. _kimi_cli.auth.oauth.load_tokens:

load_tokens
^^^^^^^^^^^

**Line:** 390

**Description:**

    Load Tokens.
    
    Args:
    ref: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)

**Returns:** ``OAuthToken | None``

**Calls:**

    - :ref:`_delete_from_keyring <func-_delete_from_keyring>`
    - :ref:`_load_from_file <func-_load_from_file>`
    - :ref:`_load_from_keyring <func-_load_from_keyring>`
    - :ref:`_save_to_file <func-_save_to_file>`
    - :ref:`suppress <func-suppress>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.auth.oauth.OAuthManager._load_initial_tokens``
    - ``kimi_cli.auth.oauth.OAuthManager._migrate_oauth_storage``
    - ``kimi_cli.auth.oauth.OAuthManager._refresh_tokens``
    - ``kimi_cli.auth.oauth.OAuthManager.ensure_fresh``
    - ``kimi_cli.auth.oauth.OAuthManager.resolve_api_key``
    - ``kimi_cli.auth.platforms.refresh_managed_models``


.. _kimi_cli.auth.oauth.login_kimi_code:

login_kimi_code
^^^^^^^^^^^^^^^

**Line:** 617

**Description:**

    Login Kimi Code.
    
    Args:
    config: Description.
    open\_browser: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)
    - ``open_browser`` (*bool*) = ``True``

**Returns:** ``AsyncIterator[OAuthEvent]``

**Calls:**

    - :ref:`OAuthDeviceExpired <func-OAuthDeviceExpired>`
    - :ref:`OAuthEvent <func-OAuthEvent>`
    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`error <func-error>`
    - :ref:`from_response <func-from_response>`
    - :ref:`get <func-get>`
    - :ref:`_apply_kimi_code_config <func-_apply_kimi_code_config>`
    - :ref:`_request_device_token <func-_request_device_token>`
    - :ref:`_select_default_model_and_thinking <func-_select_default_model_and_thinking>`
    - :ref:`request_device_authorization <func-request_device_authorization>`
    - ... and 9 more

**Called by:**

    - ``kimi_cli.cli.__init__.login``
    - ``kimi_cli.ui.shell.oauth._login_kimi_code``


.. _kimi_cli.auth.oauth.logout_kimi_code:

logout_kimi_code
^^^^^^^^^^^^^^^^

**Line:** 732

**Description:**

    Logout Kimi Code.
    
    Args:
    config: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)

**Returns:** ``AsyncIterator[OAuthEvent]``

**Calls:**

    - :ref:`OAuthEvent <func-OAuthEvent>`
    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`items <func-items>`
    - :ref:`delete_tokens <func-delete_tokens>`
    - :ref:`managed_provider_key <func-managed_provider_key>`
    - :ref:`save_config <func-save_config>`
    - :ref:`list <func-list>`

**Called by:**

    - ``kimi_cli.cli.__init__.logout``
    - ``kimi_cli.ui.shell.oauth.logout``


.. _kimi_cli.auth.oauth.refresh_token:

refresh_token
^^^^^^^^^^^^^

**Line:** 507

**Description:**

    Refresh Token.
    
    Args:
    refresh\_token: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``refresh_token`` (*str*)

**Returns:** ``OAuthToken``

**Calls:**

    - :ref:`OAuthError <func-OAuthError>`
    - :ref:`OAuthUnauthorized <func-OAuthUnauthorized>`
    - :ref:`from_response <func-from_response>`
    - :ref:`get <func-get>`
    - :ref:`json <func-json>`
    - :ref:`_common_headers <func-_common_headers>`
    - :ref:`_oauth_host <func-_oauth_host>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`post <func-post>`
    - :ref:`rstrip <func-rstrip>`

**Called by:**

    - ``kimi_cli.auth.oauth.OAuthManager._refresh_tokens``


.. _kimi_cli.auth.oauth.request_device_authorization:

request_device_authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 448

**Description:**

    Request Device Authorization.

**Returns:** ``DeviceAuthorization``

**Calls:**

    - :ref:`DeviceAuthorization <func-DeviceAuthorization>`
    - :ref:`OAuthError <func-OAuthError>`
    - :ref:`get <func-get>`
    - :ref:`int <func-int>`
    - :ref:`json <func-json>`
    - :ref:`_common_headers <func-_common_headers>`
    - :ref:`_oauth_host <func-_oauth_host>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`post <func-post>`
    - :ref:`rstrip <func-rstrip>`
    - ... and 1 more

**Called by:**

    - ``kimi_cli.auth.oauth.login_kimi_code``


.. _kimi_cli.auth.oauth.save_tokens:

save_tokens
^^^^^^^^^^^

**Line:** 417

**Description:**

    Save Tokens.
    
    Args:
    ref: Description.
    token: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)
    - ``token`` (*OAuthToken*)

**Returns:** ``OAuthRef``

**Calls:**

    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`_save_to_file <func-_save_to_file>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.auth.oauth.OAuthManager._refresh_tokens``
    - ``kimi_cli.auth.oauth.login_kimi_code``


Methods
-------

- ``OAuthEvent.json`` - Line 134
- ``OAuthManager.common_headers`` - Line 839
- ``OAuthManager.ensure_fresh`` - Line 867
- ``OAuthManager.refreshing`` - Line 879
- ``OAuthManager.resolve_api_key`` - Line 842
- ``OAuthToken.from_dict`` - Line 172
- ``OAuthToken.from_response`` - Line 152
- ``OAuthToken.to_dict`` - Line 162

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_apply_kimi_code_config`` - Line 554
- ``_ascii_header_value`` - Line 243
- ``_common_headers`` - Line 261
- ``_credentials_dir`` - Line 277
- ``_credentials_path`` - Line 285
- ``_delete_from_file`` - Line 376
- ``_delete_from_keyring`` - Line 324
- ``_device_id_path`` - Line 109
- ``_device_model`` - Line 195
- ``_ensure_private_file`` - Line 182
- ``_load_from_file`` - Line 339
- ``_load_from_keyring`` - Line 298
- ``_oauth_host`` - Line 115
- ``_request_device_token`` - Line 473
- ``_save_to_file`` - Line 361
- ``_select_default_model_and_thinking`` - Line 537
