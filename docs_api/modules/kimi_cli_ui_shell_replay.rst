kimi_cli.ui.shell.replay
========================

.. module:: kimi_cli.ui.shell.replay

Source: :file:`src/kimi_cli/ui/shell/replay.py`

Functions
---------

.. _kimi_cli.ui.shell.replay.replay_recent_history:

replay_recent_history
^^^^^^^^^^^^^^^^^^^^^

**Line:** 79

**Description:**

    Replay the most recent user-initiated turns from the provided message history or wire file.

**Parameters:**

    - ``history`` (*Sequence[Message]*)
    - ``wire_file`` (*WireFile | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`Wire <func-Wire>`
    - :ref:`create_task <func-create_task>`
    - :ref:`getuser <func-getuser>`
    - :ref:`_build_replay_turns_from_history <func-_build_replay_turns_from_history>`
    - :ref:`_build_replay_turns_from_wire <func-_build_replay_turns_from_wire>`
    - :ref:`_find_replay_start <func-_find_replay_start>`
    - :ref:`visualize <func-visualize>`
    - :ref:`message_stringify <func-message_stringify>`
    - :ref:`print <func-print>`
    - ... and 5 more

**Called by:**

    - ``kimi_cli.ui.shell.__init__.Shell.run``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_build_replay_turns_from_history`` - Line 196
- ``_build_replay_turns_from_wire`` - Line 114
- ``_find_replay_start`` - Line 180
- ``_is_clear_command_input`` - Line 51
- ``_is_user_message`` - Line 165
