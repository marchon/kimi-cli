kimi_cli.ui.shell.oauth
=======================

.. module:: kimi_cli.ui.shell.oauth

Source: :file:`src/kimi_cli/ui/shell/oauth.py`

Functions
---------

.. _kimi_cli.ui.shell.oauth.login:

login
^^^^^

**Line:** 106

**Description:**

    Login or setup a platform.

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`_login_kimi_code <func-_login_kimi_code>`
    - :ref:`select_platform <func-select_platform>`
    - :ref:`setup_platform <func-setup_platform>`
    - :ref:`clear <func-clear>`
    - :ref:`sleep <func-sleep>`


.. _kimi_cli.ui.shell.oauth.logout:

logout
^^^^^^

**Line:** 125

**Description:**

    Logout from the current platform.

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`items <func-items>`
    - :ref:`logout_kimi_code <func-logout_kimi_code>`
    - :ref:`is_managed_provider_key <func-is_managed_provider_key>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`
    - :ref:`save_config <func-save_config>`
    - :ref:`_current_model_key <func-_current_model_key>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`clear <func-clear>`
    - :ref:`list <func-list>`
    - ... and 2 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_current_model_key`` - Line 87
- ``_ensure_kimi_soul`` - Line 35
- ``_login_kimi_code`` - Line 50
