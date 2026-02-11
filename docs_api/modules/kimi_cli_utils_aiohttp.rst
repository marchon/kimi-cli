kimi_cli.utils.aiohttp
======================

.. module:: kimi_cli.utils.aiohttp

Source: :file:`src/kimi_cli/utils/aiohttp.py`

Functions
---------

.. _kimi_cli.utils.aiohttp.new_client_session:

new_client_session
^^^^^^^^^^^^^^^^^^

**Line:** 23

**Description:**

    New Client Session.

**Returns:** ``aiohttp.ClientSession``

**Calls:**

    - :ref:`ClientSession <func-ClientSession>`
    - :ref:`TCPConnector <func-TCPConnector>`

**Called by:**

    - ``kimi_cli.auth.oauth._request_device_token``
    - ``kimi_cli.auth.oauth.refresh_token``
    - ``kimi_cli.auth.oauth.request_device_authorization``
    - ``kimi_cli.auth.platforms.list_models``
    - ``kimi_cli.tools.file.grep_local._download_and_install_rg``
    - ``kimi_cli.tools.web.fetch.FetchURL._fetch_with_service``
    - ``kimi_cli.tools.web.fetch.FetchURL.fetch_with_http_get``
    - ``kimi_cli.tools.web.search.SearchWeb.__call__``
    - ``kimi_cli.ui.shell.update._do_update``
    - ``kimi_cli.ui.shell.usage._fetch_usage``

