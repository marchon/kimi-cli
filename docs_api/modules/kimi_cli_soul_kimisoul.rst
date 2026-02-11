kimi_cli.soul.kimisoul
======================

.. module:: kimi_cli.soul.kimisoul

Source: :file:`src/kimi_cli/soul/kimisoul.py`

Classes
-------

.. _class-BackToTheFuture:

BackToTheFuture
^^^^^^^^^^^^^^^

Raise when we need to revert the context to a previous checkpoint.
    The main agent loop should catch this exception and handle it.


.. _class-FlowRunner:

FlowRunner
^^^^^^^^^^

FlowRunner class.


.. _class-KimiSoul:

KimiSoul
^^^^^^^^

The soul of Kimi Code CLI.


.. _class-StepOutcome:

StepOutcome
^^^^^^^^^^^

StepOutcome class.


.. _class-TurnOutcome:

TurnOutcome
^^^^^^^^^^^

TurnOutcome class.


Methods
-------

- ``FlowRunner.ralph_loop`` - Line 555
- ``FlowRunner.run`` - Line 594
- ``KimiSoul.agent`` - Line 163
- ``KimiSoul.available_slash_commands`` - Line 188
- ``KimiSoul.compact_context`` - Line 489
- ``KimiSoul.context`` - Line 171
- ``KimiSoul.model_capabilities`` - Line 141
- ``KimiSoul.model_name`` - Line 137
- ``KimiSoul.name`` - Line 133
- ``KimiSoul.run`` - Line 191
- ``KimiSoul.runtime`` - Line 167
- ``KimiSoul.status`` - Line 156
- ``KimiSoul.thinking`` - Line 147
- ``KimiSoul.wire_file`` - Line 181
