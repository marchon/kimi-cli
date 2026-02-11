UI Reference
============

Overview
--------

Kimi Code CLI provides multiple user interface modes:

1. **Shell UI** - Interactive terminal UI (default)
2. **Print UI** - Non-interactive output mode
3. **ACP Server** - Agent Communication Protocol server
4. **Wire Mode** - Raw wire message interface

Shell UI
--------

The Shell UI provides an interactive terminal experience with:

- Rich text rendering with syntax highlighting
- Command history and autocompletion
- Slash command support
- Keyboard shortcuts
- Real-time streaming output

Usage
~~~~~

.. code-block:: bash

   # Start shell UI (default)
   kimi

   # With initial prompt
   kimi -p "Your prompt"

Keyboard Shortcuts
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Shortcut
     - Action
   * - ``Ctrl+C``
     - Cancel current operation
   * - ``Ctrl+D``
     - Exit (on empty prompt)
   * - ``Tab``
     - Autocomplete
   * - ``Up/Down``
     - Navigate command history
   * - ``Ctrl+L``
     - Clear screen

Slash Commands
~~~~~~~~~~~~~~

Built-in slash commands:

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - ``/help``
     - Show help message
   * - ``/login``
     - Login to Kimi
   * - ``/logout``
     - Logout from Kimi
   * - ``/exit``
     - Exit the shell
   * - ``/clear``
     - Clear the conversation
   * - ``/compact``
     - Compact the context
   * - ``/model``
     - Show/change model
   * - ``/session``
     - Session management
   * - ``/web``
     - Switch to web UI

Print UI
--------

The Print UI is designed for non-interactive usage and scripting:

Usage
~~~~~

.. code-block:: bash

   # Basic print mode
   kimi --print -p "Your prompt"

   # Quiet mode (final message only)
   kimi --quiet -p "Your prompt"

   # With input/output formats
   kimi --print --input-format text --output-format stream-json -p "Your prompt"

Options
~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Description
   * - ``--print``
     - Enable print mode
   * - ``--quiet``
     - Alias for ``--print --output-format text --final-message-only``
   * - ``--input-format``
     - Input format: ``text`` or ``stream-json``
   * - ``--output-format``
     - Output format: ``text`` or ``stream-json``
   * - ``--final-message-only``
     - Only output the final assistant message

ACP Server
----------

The Agent Communication Protocol (ACP) server allows IDE integrations:

Usage
~~~~~

.. code-block:: bash

   # Start ACP server
   kimi acp

   # Or with legacy flag
   kimi --acp

Features
~~~~~~~~

- JSON-RPC communication
- Tool exposure for external clients
- Session management
- Approval handling

Wire Mode
---------

Wire mode provides direct access to wire messages:

Usage
~~~~~

.. code-block:: bash

   # Start wire server
   kimi --wire

Wire Messages
~~~~~~~~~~~~~

See :doc:`api/kimi_cli.wire.types` for message types.

Web UI
------

A web-based graphical interface:

Usage
~~~~~

.. code-block:: bash

   # Start web UI
   kimi web

   # Or switch from shell
   /web

Features
~~~~~~~~

- Browser-based interface
- Session synchronization
- Rich content rendering
- File upload support

Python API
----------

Creating UI Instances
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from kimi_cli.app import KimiCLI
   from kimi_cli.session import Session

   async def run_uis():
       session = await Session.create()
       cli = await KimiCLI.create(session)

       # Shell UI
       await cli.run_shell()

       # Print UI
       await cli.run_print(
           input_format="text",
           output_format="text",
           command="Your prompt"
       )

       # ACP server
       await cli.run_acp()

       # Wire mode
       await cli.run_wire_stdio()

Custom UI Development
~~~~~~~~~~~~~~~~~~~~~

To create a custom UI using the Wire protocol:

.. code-block:: python

   from kimi_cli.app import KimiCLI
   from kimi_cli.session import Session
   from kimi_cli.wire import Wire

   async def custom_ui():
       session = await Session.create()
       cli = await KimiCLI.create(session)

       cancel_event = asyncio.Event()
       async for message in cli.run("Prompt", cancel_event):
           # Handle different message types
           match message:
               case TextPart():
                   print(message.text, end="")
               case ToolResult():
                   print(f"Tool result: {message}")
               case ApprovalRequest():
                   # Handle approval
                   message.resolve("approve")
