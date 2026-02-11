kimi_cli.web.runner.worker
==========================

.. module:: kimi_cli.web.runner.worker

Source: :file:`src/kimi_cli/web/runner/worker.py`

Functions
---------

.. _kimi_cli.web.runner.worker.main:

main
^^^^

**Line:** 59

**Description:**

    Entry point for the worker subprocess.

**Returns:** ``None``

**Calls:**

    - :ref:`UUID <func-UUID>`
    - :ref:`exit <func-exit>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`run_worker <func-run_worker>`
    - :ref:`len <func-len>`
    - :ref:`print <func-print>`


.. _kimi_cli.web.runner.worker.run_worker:

run_worker
^^^^^^^^^^

**Line:** 22

**Description:**

    Run the KimiCLI worker for a session.

**Parameters:**

    - ``session_id`` (*UUID*)

**Returns:** ``None``

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`create <func-create>`
    - :ref:`exists <func-exists>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`loads <func-loads>`
    - :ref:`read_text <func-read_text>`
    - :ref:`run_wire_stdio <func-run_wire_stdio>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.cli.__init__.web_worker``
    - ``kimi_cli.web.runner.worker.main``

