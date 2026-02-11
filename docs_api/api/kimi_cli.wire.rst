kimi_cli.wire
=============

Wire communication protocol between soul and UI.

.. automodule:: kimi_cli.wire
   :members:
   :undoc-members:
   :show-inheritance:

Core Wire Components
--------------------

.. autoclass:: kimi_cli.wire.Wire
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.WireSoulSide
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.WireUISide
   :members:
   :undoc-members:
   :show-inheritance:

Message Types
-------------

.. automodule:: kimi_cli.wire.types
   :members:
   :undoc-members:
   :show-inheritance:

Events
~~~~~~

.. autoclass:: kimi_cli.wire.types.TurnBegin
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.TurnEnd
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.StepBegin
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.StepInterrupted
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.CompactionBegin
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.CompactionEnd
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.StatusUpdate
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.SubagentEvent
   :members:
   :undoc-members:
   :show-inheritance:

Requests
~~~~~~~~

.. autoclass:: kimi_cli.wire.types.ApprovalRequest
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.ApprovalResponse
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.wire.types.ToolCallRequest
   :members:
   :undoc-members:
   :show-inheritance:

Type Helpers
~~~~~~~~~~~~

.. autofunction:: kimi_cli.wire.types.is_event
.. autofunction:: kimi_cli.wire.types.is_request
.. autofunction:: kimi_cli.wire.types.is_wire_message

Supporting Modules
------------------

.. automodule:: kimi_cli.wire.file
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: kimi_cli.wire.protocol
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: kimi_cli.wire.serde
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: kimi_cli.wire.server
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: kimi_cli.wire.jsonrpc
   :members:
   :undoc-members:
   :show-inheritance:
