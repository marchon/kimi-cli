kimi_cli.soul.agent
===================

.. module:: kimi_cli.soul.agent

Source: :file:`src/kimi_cli/soul/agent.py`

Classes
-------

.. _class-Agent:

Agent
^^^^^

The loaded agent.


.. _class-BuiltinSystemPromptArgs:

BuiltinSystemPromptArgs
^^^^^^^^^^^^^^^^^^^^^^^

Builtin system prompt arguments.


.. _class-LaborMarket:

LaborMarket
^^^^^^^^^^^

LaborMarket class.


.. _class-Runtime:

Runtime
^^^^^^^

Agent runtime.


Functions
---------

.. _kimi_cli.soul.agent.load_agent:

load_agent
^^^^^^^^^^

**Line:** 244

**Description:**

    Load agent from specification file.

    Raises:
        FileNotFoundError: When the agent file is not found.
        AgentSpecError(KimiCLIException, ValueError): When the agent specification is inva

**Parameters:**

    - ``agent_file`` (*Path*)
    - ``runtime`` (*Runtime*)
    - ``mcp_configs``

**Returns:** ``Agent``

**Calls:**

    - :ref:`Agent <func-Agent>`
    - :ref:`KimiToolset <func-KimiToolset>`
    - :ref:`MCPConfigError <func-MCPConfigError>`
    - :ref:`add_fixed_subagent <func-add_fixed_subagent>`
    - :ref:`append <func-append>`
    - :ref:`copy_for_fixed_subagent <func-copy_for_fixed_subagent>`
    - :ref:`debug <func-debug>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - ... and 6 more

**Called by:**

    - ``kimi_cli.app.KimiCLI.create``
    - ``kimi_cli.soul.agent.load_agent``


.. _kimi_cli.soul.agent.load_agents_md:

load_agents_md
^^^^^^^^^^^^^^

**Line:** 78

**Description:**

    Load Agents Md.
    
    Args:
    work\_dir: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`info <func-info>`
    - :ref:`is_file <func-is_file>`
    - :ref:`read_text <func-read_text>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.soul.agent.Runtime.create``
    - ``kimi_cli.soul.slash.init``


Methods
-------

- ``LaborMarket.add_dynamic_subagent`` - Line 74
- ``LaborMarket.add_fixed_subagent`` - Line 69
- ``LaborMarket.subagents`` - Line 65
- ``Runtime.copy_for_dynamic_subagent`` - Line 177
- ``Runtime.copy_for_fixed_subagent`` - Line 162
- ``Runtime.create`` - Line 115

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_load_system_prompt`` - Line 207
