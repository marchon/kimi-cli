kimi_cli.soul.__init__
======================

.. module:: kimi_cli.soul.__init__

Source: :file:`src/kimi_cli/soul/__init__.py`

Classes
-------

.. _class-LLMNotSet:

LLMNotSet
^^^^^^^^^

Raised when the LLM is not set.


.. _class-LLMNotSupported:

LLMNotSupported
^^^^^^^^^^^^^^^

Raised when the LLM does not have required capabilities.


.. _class-MaxStepsReached:

MaxStepsReached
^^^^^^^^^^^^^^^

Raised when the maximum number of steps is reached.


.. _class-RunCancelled:

RunCancelled
^^^^^^^^^^^^

The run was cancelled by the cancel event.


.. _class-Soul:

Soul
^^^^

Soul class.


.. _class-StatusSnapshot:

StatusSnapshot
^^^^^^^^^^^^^^

StatusSnapshot class.


Functions
---------

.. _kimi_cli.soul.__init__.get_wire_or_none:

get_wire_or_none
^^^^^^^^^^^^^^^^

**Line:** 135

**Description:**

    Get the current wire or None.
    Expect to be not None when called from anywhere in the agent loop.

**Returns:** ``Wire | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - ``kimi_cli.soul.__init__.wire_send``
    - ``kimi_cli.soul.toolset.WireExternalTool.__call__``
    - ``kimi_cli.tools.multiagent.task.Task._run_subagent``


.. _kimi_cli.soul.__init__.run_soul:

run_soul
^^^^^^^^

**Line:** 152

**Description:**

    Run the soul with the given user input, connecting it to the UI loop with a \`Wire\`.

    \`cancel\_event\` is a outside handle that can be used to cancel the run. When the
    event is set, the run will 

**Parameters:**

    - ``soul`` (*Soul*)
    - ``user_input`` (*str | list[ContentPart]*)
    - ``ui_loop_fn`` (*UILoopFn*)
    - ``cancel_event`` (*asyncio.Event*)
    - ``wire_file`` (*WireFile | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`Wire <func-Wire>`
    - :ref:`cancel <func-cancel>`
    - :ref:`create_task <func-create_task>`
    - :ref:`debug <func-debug>`
    - :ref:`done <func-done>`
    - :ref:`is_set <func-is_set>`
    - :ref:`join <func-join>`
    - :ref:`reset <func-reset>`
    - :ref:`result <func-result>`
    - :ref:`run <func-run>`
    - ... and 6 more

**Called by:**

    - ``kimi_cli.app.KimiCLI.run``
    - ``kimi_cli.tools.multiagent.task.Task._run_subagent``
    - ``kimi_cli.ui.print.__init__.Print.run``
    - ``kimi_cli.ui.shell.__init__.Shell.run_soul_command``
    - ``kimi_cli.wire.server.WireServer._handle_prompt``


.. _kimi_cli.soul.__init__.wire_send:

wire_send
^^^^^^^^^

**Line:** 142

**Description:**

    Send a wire message to the current wire.
    Take this as \`print\` and \`input\` for souls.
    Souls should always use this function to send wire messages.

**Parameters:**

    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`get_wire_or_none <func-get_wire_or_none>`
    - :ref:`send <func-send>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.FlowRunner._flow_turn``
    - ``kimi_cli.soul.kimisoul.KimiSoul._agent_loop``
    - ``kimi_cli.soul.kimisoul.KimiSoul._make_skill_runner``
    - ``kimi_cli.soul.kimisoul.KimiSoul._step``
    - ``kimi_cli.soul.kimisoul.KimiSoul.compact_context``
    - ``kimi_cli.soul.kimisoul.KimiSoul.run``
    - ``kimi_cli.soul.slash.clear``
    - ``kimi_cli.soul.slash.compact``
    - ``kimi_cli.soul.slash.yolo``


Methods
-------

- ``Soul.available_slash_commands`` - Line 85
- ``Soul.model_capabilities`` - Line 67
- ``Soul.model_name`` - Line 62
- ``Soul.name`` - Line 57
- ``Soul.run`` - Line 89
- ``Soul.status`` - Line 80
- ``Soul.thinking`` - Line 72
