kimi_cli.wire.types
===================

.. module:: kimi_cli.wire.types

Source: :file:`src/kimi_cli/wire/types.py`

Classes
-------

.. _class-ApprovalRequest:

ApprovalRequest
^^^^^^^^^^^^^^^

A request for user approval before proceeding with an action.


.. _class-ApprovalResponse:

ApprovalResponse
^^^^^^^^^^^^^^^^

Indicates that an approval request has been resolved.


.. _class-CompactionBegin:

CompactionBegin
^^^^^^^^^^^^^^^

Indicates that a compaction just began.
    This event must be sent during a step, which means, between \`StepBegin\` and the next
    \`StepBegin\` or \`StepInterrupted\`. And, there must be a \`CompactionEnd\` directly following
    this event.


.. _class-CompactionEnd:

CompactionEnd
^^^^^^^^^^^^^

Indicates that a compaction just ended.
    This event must be sent directly after a \`CompactionBegin\` event.


.. _class-StatusUpdate:

StatusUpdate
^^^^^^^^^^^^

An update on the current status of the soul.
    None fields indicate no change from the previous status.


.. _class-StepBegin:

StepBegin
^^^^^^^^^

Indicates the beginning of a new agent step.
    This event must be sent before any other event in the step.


.. _class-StepInterrupted:

StepInterrupted
^^^^^^^^^^^^^^^

Indicates the current step was interrupted, either by user intervention or an error.


.. _class-SubagentEvent:

SubagentEvent
^^^^^^^^^^^^^

An event from a subagent.


.. _class-ToolCallRequest:

ToolCallRequest
^^^^^^^^^^^^^^^

A tool call request routed to the Wire client for execution.


.. _class-TurnBegin:

TurnBegin
^^^^^^^^^

Indicates the beginning of a new agent turn.
    This event must be sent before any other event in the turn.


.. _class-TurnEnd:

TurnEnd
^^^^^^^

Indicates the end of the current agent turn.
    This event must be sent after all other events in the turn.
    If the turn is interrupted, this event may be omitted.


.. _class-WireMessageEnvelope:

WireMessageEnvelope
^^^^^^^^^^^^^^^^^^^

WireMessageEnvelope class.


Functions
---------

.. _kimi_cli.wire.types.is_event:

is_event
^^^^^^^^

**Line:** 333

**Description:**

    Check if the message is an Event.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[Event]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - ``kimi_cli.ui.shell.replay._build_replay_turns_from_wire``
    - ``kimi_cli.wire.jsonrpc.JSONRPCEventMessage._validate_params``
    - ``kimi_cli.wire.server.WireServer._handle_replay``
    - ``kimi_cli.wire.types.SubagentEvent._validate_event``


.. _kimi_cli.wire.types.is_request:

is_request
^^^^^^^^^^

**Line:** 337

**Description:**

    Check if the message is a Request.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[Request]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - ``kimi_cli.web.api.sessions._read_wire_lines``
    - ``kimi_cli.wire.jsonrpc.JSONRPCRequestMessage._validate_params``
    - ``kimi_cli.wire.server.WireServer._handle_replay``


.. _kimi_cli.wire.types.is_wire_message:

is_wire_message
^^^^^^^^^^^^^^^

**Line:** 341

**Description:**

    Check if the message is a WireMessage.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[WireMessage]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - ``kimi_cli.wire.__init__.WireSoulSide.flush``
    - ``kimi_cli.wire.types.SubagentEvent._validate_event``


Methods
-------

- ``ApprovalRequest.resolve`` - Line 182
- ``ApprovalRequest.resolved`` - Line 192
- ``ApprovalRequest.wait`` - Line 173
- ``ToolCallRequest.from_tool_call`` - Line 117
- ``ToolCallRequest.resolve`` - Line 133
- ``ToolCallRequest.resolved`` - Line 143
- ``ToolCallRequest.wait`` - Line 124
- ``WireMessageEnvelope.from_wire_message`` - Line 359
- ``WireMessageEnvelope.to_wire_message`` - Line 371
