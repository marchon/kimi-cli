kimi_cli.cli.info
=================

.. module:: kimi_cli.cli.info

Source: :file:`src/kimi_cli/cli/info.py`

Classes
-------

.. _class-InfoData:

InfoData
^^^^^^^^

InfoData class.


Functions
---------

.. _kimi_cli.cli.info.info:

info
^^^^

**Line:** 76

**Description:**

    Show version and protocol information.

**Parameters:**

    - ``json_output`` = ``False``

**Calls:**

    - :ref:`Option <func-Option>`
    - :ref:`callback <func-callback>`
    - :ref:`_emit_info <func-_emit_info>`

**Called by:**

    - ``kimi_cli.acp.__init__.acp_main``
    - ``kimi_cli.acp.server.ACPServer.cancel``
    - ``kimi_cli.acp.server.ACPServer.initialize``
    - ``kimi_cli.acp.server.ACPServer.list_sessions``
    - ``kimi_cli.acp.server.ACPServer.load_session``
    - ``kimi_cli.acp.server.ACPServer.new_session``
    - ``kimi_cli.acp.server.ACPServer.on_connect``
    - ``kimi_cli.acp.server.ACPServer.prompt``
    - ``kimi_cli.acp.server.ACPServer.set_session_model``
    - ``kimi_cli.acp.session.ACPSession.prompt``
    - ... and 30 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_collect_info`` - Line 35
- ``_emit_info`` - Line 49
