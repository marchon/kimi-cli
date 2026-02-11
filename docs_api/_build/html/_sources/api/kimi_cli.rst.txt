kimi_cli
========

Main application module.

.. automodule:: kimi_cli
   :members:
   :undoc-members:
   :show-inheritance:

Submodules
----------

.. toctree::
   :maxdepth: 1

   kimi_cli.app
   kimi_cli.config
   kimi_cli.session
   kimi_cli.llm
   kimi_cli.agentspec
   kimi_cli.metadata
   kimi_cli.share
   kimi_cli.constant
   kimi_cli.exception

kimi_cli.app
------------

Main application entry point.

.. automodule:: kimi_cli.app
   :members:
   :undoc-members:
   :show-inheritance:

Key Classes
~~~~~~~~~~~

.. autoclass:: kimi_cli.app.KimiCLI
   :members:
   :undoc-members:
   :show-inheritance:

Key Functions
~~~~~~~~~~~~~

.. autofunction:: kimi_cli.app.enable_logging

kimi_cli.config
---------------

Configuration management.

.. automodule:: kimi_cli.config
   :members:
   :undoc-members:
   :show-inheritance:

Configuration Classes
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: kimi_cli.config.Config
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.config.LLMModel
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.config.LLMProvider
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.config.LoopControl
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.config.Services
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: kimi_cli.config.MCPConfig
   :members:
   :undoc-members:
   :show-inheritance:

Configuration Functions
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: kimi_cli.config.load_config
.. autofunction:: kimi_cli.config.save_config
.. autofunction:: kimi_cli.config.get_config_file
.. autofunction:: kimi_cli.config.get_default_config
.. autofunction:: kimi_cli.config.load_config_from_string

kimi_cli.session
----------------

Session management.

.. automodule:: kimi_cli.session
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.llm
------------

LLM provider management.

.. automodule:: kimi_cli.llm
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.agentspec
------------------

Agent specification loading.

.. automodule:: kimi_cli.agentspec
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.metadata
-----------------

Metadata management.

.. automodule:: kimi_cli.metadata
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.share
--------------

Share directory utilities.

.. automodule:: kimi_cli.share
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.constant
-----------------

Constants and version info.

.. automodule:: kimi_cli.constant
   :members:
   :undoc-members:
   :show-inheritance:

kimi_cli.exception
------------------

Exception classes.

.. automodule:: kimi_cli.exception
   :members:
   :undoc-members:
   :show-inheritance:
