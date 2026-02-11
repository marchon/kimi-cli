Quickstart
==========

Installation
------------

Kimi Code CLI requires Python 3.12 or higher.

.. code-block:: bash

   pip install kimi-cli

Basic Usage
-----------

Command Line
~~~~~~~~~~~~

.. code-block:: bash

   # Start interactive shell
   kimi

   # Run a single command
   kimi -p "Your command here"

   # Continue previous session
   kimi -C

   # Use specific session
   kimi -S session-id

Python API
~~~~~~~~~~

.. code-block:: python

   import asyncio
   from kimi_cli.app import KimiCLI, enable_logging
   from kimi_cli.session import Session

   async def main():
       # Enable logging
       enable_logging(debug=False)
       
       # Create a session
       session = await Session.create()
       
       # Create CLI instance
       cli = await KimiCLI.create(session)
       
       # Run with shell UI
       await cli.run_shell()

   if __name__ == "__main__":
       asyncio.run(main())

Programmatic Usage
------------------

Running Without UI
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from kimi_cli.app import KimiCLI
   from kimi_cli.session import Session

   async def run_agent():
       session = await Session.create()
       cli = await KimiCLI.create(session)
       
       cancel_event = asyncio.Event()
       async for message in cli.run("Your prompt", cancel_event):
           # Process Wire messages
           print(message)

   asyncio.run(run_agent())

Configuration
-------------

Configuration File
~~~~~~~~~~~~~~~~~~

Create ``~/.kimi/config.toml``:

.. code-block:: toml

   default_model = "my-model"
   default_thinking = false
   default_yolo = false

   [models.my-model]
   provider = "my-provider"
   model = "kimi-k2.5"
   max_context_size = 100000

   [providers.my-provider]
   type = "kimi"
   base_url = "https://api.moonshot.cn/v1"
   api_key = "your-api-key"

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

- ``KIMI_API_KEY``: API key for authentication
- ``KIMI_BASE_URL``: Base URL for the API
- ``KIMI_MODEL_NAME``: Default model name

Next Steps
----------

- Read :doc:`architecture` to understand the codebase structure
- Browse :doc:`api/modules` for complete API reference
- See :doc:`cli_reference` for all CLI options
