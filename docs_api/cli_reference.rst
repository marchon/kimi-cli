CLI Reference
=============

Main Command
------------

.. code-block:: text

   kimi [OPTIONS] [COMMAND]

Global Options
--------------

Meta Options
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Short
     - Description
   * - ``--version``
     - ``-V``
     - Show version and exit
   * - ``--verbose``
     -
     - Print verbose information
   * - ``--debug``
     -
     - Log debug information

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Short
     - Description
   * - ``--work-dir``
     - ``-w``
     - Working directory (default: current)
   * - ``--session``
     - ``-S``
     - Session ID to resume
   * - ``--continue``
     - ``-C``
     - Continue previous session
   * - ``--config``
     -
     - Config TOML/JSON string
   * - ``--config-file``
     -
     - Path to config file
   * - ``--model``
     - ``-m``
     - LLM model to use
   * - ``--thinking`` / ``--no-thinking``
     -
     - Enable/disable thinking mode

Run Mode Options
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Short
     - Description
   * - ``--yolo`` / ``--yes`` / ``-y``
     -
     - Auto-approve all actions
   * - ``--prompt`` / ``--command``
     - ``-p`` / ``-c``
     - User prompt
   * - ``--print``
     -
     - Non-interactive print mode
   * - ``--quiet``
     -
     - Final message only mode
   * - ``--acp``
     -
     - Run as ACP server
   * - ``--wire``
     -
     - Run as Wire server

Customization Options
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Description
   * - ``--agent``
     - Builtin agent: ``default`` or ``okabe``
   * - ``--agent-file``
     - Custom agent specification file
   * - ``--mcp-config-file``
     - MCP config file (can be repeated)
   * - ``--mcp-config``
     - MCP config JSON string
   * - ``--skills-dir``
     - Override skills directory

Loop Control Options
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Option
     - Description
   * - ``--max-steps-per-turn``
     - Maximum steps per turn (default: 100)
   * - ``--max-retries-per-step``
     - Maximum retries per step (default: 3)
   * - ``--max-ralph-iterations``
     - Ralph mode iterations (default: 0)

Subcommands
-----------

login
~~~~~

Login to your Kimi account.

.. code-block:: text

   kimi login [OPTIONS]

Options:

- ``--json``: Emit OAuth events as JSON lines

logout
~~~~~~

Logout from your Kimi account.

.. code-block:: text

   kimi logout [OPTIONS]

Options:

- ``--json``: Emit OAuth events as JSON lines

acp
~~~

Run Kimi Code CLI as an ACP server.

.. code-block:: text

   kimi acp

term
~~~~

Run Toad TUI backed by Kimi Code CLI ACP server.

.. code-block:: text

   kimi term [ARGS...]

info
~~~~

Display information about Kimi Code CLI.

.. code-block:: text

   kimi info [SUBCOMMAND]

Subcommands:

- ``models``: List available models
- ``providers``: List configured providers
- ``tools``: List available tools
- ``sessions``: List sessions

mcp
~~~

Manage MCP (Model Context Protocol) configurations.

.. code-block:: text

   kimi mcp [COMMAND]

Commands:

- ``list``: List MCP servers
- ``add``: Add MCP server
- ``remove``: Remove MCP server
- ``auth``: Authenticate with MCP server

web
~~~

Web UI commands.

.. code-block:: text

   kimi web [COMMAND]

Commands:

- ``start``: Start web UI server
- ``stop``: Stop web UI server

Examples
--------

Basic Usage
~~~~~~~~~~~

.. code-block:: bash

   # Start interactive shell
   kimi

   # Run a single command
   kimi -p "Explain this codebase"

   # Continue previous session
   kimi -C

Advanced Usage
~~~~~~~~~~~~~~

.. code-block:: bash

   # Use specific model with thinking enabled
   kimi -m my-model --thinking -p "Complex task"

   # Run with auto-approval
   kimi --yolo -p "Make changes to files"

   # Print mode with JSON output
   kimi --print --output-format stream-json -p "Task"

   # Custom agent spec
   kimi --agent-file ./my-agent.yaml

   # With MCP servers
   kimi --mcp-config-file ./mcp.json

Scripting Examples
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Pipe input to kimi
   echo "Analyze this" | kimi --quiet

   # Use with xargs
   find . -name "*.py" | xargs -I {} kimi --quiet -p "Review {}"

   # JSON output for processing
   kimi --print --output-format stream-json -p "List files" | jq ...
