kimi_cli.web.runner.process
===========================

.. module:: kimi_cli.web.runner.process

Source: :file:`src/kimi_cli/web/runner/process.py`

Classes
-------

.. _class-KimiCLIRunner:

KimiCLIRunner
^^^^^^^^^^^^^

Manages multiple session processes.


.. _class-RestartWorkersSummary:

RestartWorkersSummary
^^^^^^^^^^^^^^^^^^^^^

Summary of a restart\_running\_workers operation.


.. _class-SessionProcess:

SessionProcess
^^^^^^^^^^^^^^

Manages a single session's KimiCLI subprocess.

    Handles:
    - Starting/stopping the subprocess
    - Reading from stdout (wire messages from KimiCLI)
    - Writing to stdin (user input to KimiCLI)
    - Broadcasting messages to connected WebSockets

    Concurrency model:
    - \`SessionProcess\`
...


Methods
-------

- ``KimiCLIRunner.detach_websocket`` - Line 697
- ``KimiCLIRunner.get_or_create_session`` - Line 686
- ``KimiCLIRunner.get_session`` - Line 693
- ``KimiCLIRunner.restart_running_workers`` - Line 704
- ``KimiCLIRunner.start`` - Line 669
- ``KimiCLIRunner.stop`` - Line 673
- ``SessionProcess.add_websocket_and_begin_replay`` - Line 564
- ``SessionProcess.end_replay`` - Line 573
- ``SessionProcess.is_alive`` - Line 107
- ``SessionProcess.is_busy`` - Line 118
- ``SessionProcess.is_running`` - Line 113
- ``SessionProcess.remove_websocket`` - Line 620
- ``SessionProcess.restart_worker`` - Line 262
- ``SessionProcess.send_message`` - Line 629
- ``SessionProcess.send_status_snapshot`` - Line 132
- ``SessionProcess.start`` - Line 177
- ``SessionProcess.status`` - Line 123
- ``SessionProcess.stop`` - Line 226
- ``SessionProcess.stop_worker`` - Line 231
- ``SessionProcess.websocket_count`` - Line 128
