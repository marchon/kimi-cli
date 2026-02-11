Architecture
============

Overview
--------

Kimi Code CLI is built with a modular architecture that separates concerns into distinct layers:

.. code-block:: text

   +-------------------+  +-------------------+  +-------------------+
   |   Shell UI        |  |   Print UI        |  |   ACP Server      |
   +---------+---------+  +---------+---------+  +---------+---------+
             |                      |                      |
             +----------------------+----------------------+
                                    |
                            +-------v--------+
                            |     Wire       |
                            +-------+--------+
                                    |
                            +-------v--------+
                            |   KimiSoul     |
                            +-------+--------+
                                    |
              +---------------------+---------------------+
              |                     |                     |
       +------v------+     +--------v--------+   +-------v-------+
       |   Context   |     |   KimiToolset   |   |    Agent      |
       +-------------+     +-----------------+   +---------------+
                                    |
                         +----------v-----------+
                         |   Built-in Tools     |
                         |   MCP Tools          |
                         +----------------------+

Core Components
---------------

KimiCLI
~~~~~~~

The :class:`~kimi_cli.app.KimiCLI` class is the main entry point for programmatic usage.
It provides methods for running the agent in different modes:

- :meth:`~kimi_cli.app.KimiCLI.run_shell()`: Interactive shell UI
- :meth:`~kimi_cli.app.KimiCLI.run_print()`: Non-interactive print mode
- :meth:`~kimi_cli.app.KimiCLI.run_acp()`: ACP server mode
- :meth:`~kimi_cli.app.KimiCLI.run()`: Direct Wire message access

KimiSoul
~~~~~~~~

The :class:`~kimi_cli.soul.kimisoul.KimiSoul` class implements the core agent loop:

1. Receives user input
2. Handles slash commands
3. Manages conversation context
4. Calls LLM with tools
5. Executes tool calls
6. Handles context compaction

Runtime
~~~~~~~

The :class:`~kimi_cli.soul.agent.Runtime` class provides the execution environment:

- Configuration
- OAuth manager
- LLM instance
- Session
- Built-in system prompt arguments
- DenwaRenji (D-Mail system)
- Approval system
- Labor market (subagent registry)
- Environment detection
- Skills registry

Wire Protocol
~~~~~~~~~~~~~

The :class:`~kimi_cli.wire.Wire` class provides a channel for communication between
the soul and UI during execution:

- **WireSoulSide**: Used by the soul to send messages
- **WireUISide**: Used by UI to receive messages
- **Messages**: Events (TurnBegin, StepBegin, ToolResult, etc.) and Requests (ApprovalRequest, ToolCallRequest)

Tool System
~~~~~~~~~~~

Tools are loaded dynamically by :class:`~kimi_cli.soul.toolset.KimiToolset`:

1. Built-in tools loaded from import paths
2. MCP tools loaded from MCP server configurations
3. Tools receive dependencies via constructor injection

Data Flow
---------

1. **Initialization**
   - CLI parses arguments
   - Configuration is loaded
   - Session is created or restored
   - Runtime is initialized
   - Agent specification is loaded
   - Tools are loaded

2. **Execution Loop**
   - User input is received
   - Slash commands are handled
   - Message is added to context
   - LLM is called with system prompt and context
   - Tool calls are executed
   - Results are added to context
   - Loop continues until no tool calls

3. **Context Management**
   - Context stores conversation history
   - Checkpoints for D-Mail support
   - Token counting
   - Automatic compaction when approaching limits

Key Design Patterns
-------------------

Dependency Injection
~~~~~~~~~~~~~~~~~~~~

Tools receive their dependencies through constructor injection:

.. code-block:: python

   class MyTool:
       def __init__(self, runtime: Runtime, config: Config):
           self.runtime = runtime
           self.config = config

Async/Await
~~~~~~~~~~~

The entire codebase uses asyncio for concurrency:

- Tool execution
- MCP server communication
- UI event handling
- Context I/O

Type Safety
~~~~~~~~~~~

Heavy use of type hints throughout:

- Pydantic models for configuration and wire messages
- Type guards for message type checking
- Generic types for tools and wire messages
