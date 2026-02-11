kimi_cli.soul
=============

Agent runtime and core loop implementation.

.. automodule:: kimi_cli.soul
   :members:
   :undoc-members:
   :show-inheritance:

Submodules
----------

.. toctree::
   :maxdepth: 1

   kimi_cli.soul.kimisoul
   kimi_cli.soul.agent
   kimi_cli.soul.toolset
   kimi_cli.soul.context
   kimi_cli.soul.approval
   kimi_cli.soul.compaction
   kimi_cli.soul.slash
   kimi_cli.soul.message
   kimi_cli.soul.denwarenji

kimi_cli.soul.kimisoul
----------------------

Main agent loop implementation.

.. automodule:: kimi_cli.soul.kimisoul
   :members:
   :undoc-members:
   :show-inheritance:

Key Classes
~~~~~~~~~~~

.. autoclass:: kimi_cli.soul.kimisoul.KimiSoul
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.kimisoul.FlowRunner
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.kimisoul.StepOutcome
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.kimisoul.TurnOutcome
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.agent
-------------------

Agent runtime and labor market.

.. automodule:: kimi_cli.soul.agent
   :members:
   :undoc-members:
   :show-inheritance:

Key Classes
~~~~~~~~~~~

.. autoclass:: kimi_cli.soul.agent.Runtime
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.agent.Agent
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.agent.LaborMarket
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.agent.BuiltinSystemPromptArgs
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions
~~~~~~~~~~~~~

.. autofunction:: kimi_cli.soul.agent.load_agent

kimi_cli.soul.toolset
---------------------

Tool loading and execution.

.. automodule:: kimi_cli.soul.toolset
   :members:
   :undoc-members:
   :show-inheritance:

Key Classes
~~~~~~~~~~~

.. autoclass:: kimi_cli.soul.toolset.KimiToolset
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.toolset.MCPServerInfo
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.toolset.MCPTool
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.soul.toolset.WireExternalTool
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions
~~~~~~~~~~~~~

.. autofunction:: kimi_cli.soul.toolset.get_current_tool_call_or_none
.. autofunction:: kimi_cli.soul.toolset.convert_mcp_tool_result

kimi_cli.soul.context
---------------------

Conversation context management.

.. automodule:: kimi_cli.soul.context
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.approval
----------------------

User approval system.

.. automodule:: kimi_cli.soul.approval
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.compaction
------------------------

Context compaction.

.. automodule:: kimi_cli.soul.compaction
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.slash
-------------------

Slash command handling.

.. automodule:: kimi_cli.soul.slash
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.message
---------------------

Message utilities.

.. automodule:: kimi_cli.soul.message
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.soul.denwarenji
------------------------

D-Mail (time travel messaging) system.

.. automodule:: kimi_cli.soul.denwarenji
   :members:
   :undoc-members:
   :show-inheritance:
