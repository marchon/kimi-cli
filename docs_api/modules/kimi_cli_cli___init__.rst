kimi_cli.cli.__init__
=====================

.. module:: kimi_cli.cli.__init__

Source: :file:`src/kimi_cli/cli/__init__.py`

Classes
-------

.. _class-Reload:

Reload
^^^^^^

Reload configuration.


.. _class-SwitchToWeb:

SwitchToWeb
^^^^^^^^^^^

Switch to web interface.


Functions
---------

.. _kimi_cli.cli.__init__.acp:

acp
^^^

**Line:** 35

**Description:**

    Run Kimi Code CLI ACP server.

**Calls:**

    - :ref:`acp_main <func-acp_main>`
    - :ref:`command <func-command>`


.. _kimi_cli.cli.__init__.kimi:

kimi
^^^^

**Line:** 197

**Description:**

    Kimi, your next CLI agent.

**Parameters:**

    - ``ctx`` (*typer.Context*)
    - ``version`` = ``False``
    - ``verbose`` = ``False``
    - ``debug`` = ``False``
    - ``local_work_dir`` = ``None``
    - ``session_id`` = ``None``
    - ``continue_`` = ``False``
    - ``config_string`` = ``None``
    - ``config_file`` = ``None``
    - ``model_name`` = ``None``
    - ``thinking`` = ``None``
    - ``yolo`` = ``False``
    - ``prompt`` = ``None``
    - ``print_mode`` = ``False``
    - ``acp_mode`` = ``False``
    - ``wire_mode`` = ``False``
    - ``input_format`` = ``None``
    - ``output_format`` = ``None``
    - ``final_message_only`` = ``False``
    - ``quiet`` = ``False``
    - ``agent`` = ``None``
    - ``agent_file`` = ``None``
    - ``mcp_config_file`` = ``None``
    - ``mcp_config`` = ``None``
    - ``local_skills_dir`` = ``None``
    - ``max_steps_per_turn`` = ``None``
    - ``max_retries_per_step`` = ``None``
    - ``max_ralph_iterations`` = ``None``

**Calls:**

    - :ref:`BadParameter <func-BadParameter>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`Reload <func-Reload>`
    - :ref:`_emit_fatal_error <func-_emit_fatal_error>`
    - :ref:`_post_run <func-_post_run>`
    - :ref:`_reload_loop <func-_reload_loop>`
    - :ref:`_run <func-_run>`
    - :ref:`append <func-append>`
    - :ref:`callback <func-callback>`
    - ... and 42 more


.. _kimi_cli.cli.__init__.login:

login
^^^^^

**Line:** 85

**Description:**

    Login to your Kimi account.

**Parameters:**

    - ``json`` (*bool*)

**Returns:** ``None``

**Calls:**

    - :ref:`Console <func-Console>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`_run <func-_run>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`login_kimi_code <func-login_kimi_code>`
    - :ref:`load_config <func-load_config>`
    - :ref:`print <func-print>`
    - :ref:`run <func-run>`
    - ... and 3 more


.. _kimi_cli.cli.__init__.logout:

logout
^^^^^^

**Line:** 44

**Description:**

    Logout from your Kimi account.

**Parameters:**

    - ``json`` (*bool*)

**Returns:** ``None``

**Calls:**

    - :ref:`Console <func-Console>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`_run <func-_run>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`logout_kimi_code <func-logout_kimi_code>`
    - :ref:`load_config <func-load_config>`
    - :ref:`print <func-print>`
    - :ref:`run <func-run>`


.. _kimi_cli.cli.__init__.term:

term
^^^^

**Line:** 143

**Description:**

    Run Toad TUI backed by Kimi Code CLI ACP server.

**Parameters:**

    - ``ctx`` (*typer.Context*)

**Returns:** ``None``

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`run_term <func-run_term>`


.. _kimi_cli.cli.__init__.web_worker:

web_worker
^^^^^^^^^^

**Line:** 765

**Description:**

    Run web worker subprocess (internal).

**Parameters:**

    - ``session_id`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`BadParameter <func-BadParameter>`
    - :ref:`UUID <func-UUID>`
    - :ref:`command <func-command>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`run_worker <func-run_worker>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_version_callback`` - Line 168
