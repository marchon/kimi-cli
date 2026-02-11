kimi_cli.agentspec
==================

.. module:: kimi_cli.agentspec

Source: :file:`src/kimi_cli/agentspec.py`

Classes
-------

.. _class-AgentSpec:

AgentSpec
^^^^^^^^^

Agent specification.


.. _class-Inherit:

Inherit
^^^^^^^

Marker class for inheritance in agent spec.


.. _class-ResolvedAgentSpec:

ResolvedAgentSpec
^^^^^^^^^^^^^^^^^

Resolved agent specification.


.. _class-SubagentSpec:

SubagentSpec
^^^^^^^^^^^^

Subagent specification.


Functions
---------

.. _kimi_cli.agentspec.get_agents_dir:

get_agents_dir
^^^^^^^^^^^^^^

**Line:** 11

**Description:**

    Get Agents Dir.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`


.. _kimi_cli.agentspec.load_agent_spec:

load_agent_spec
^^^^^^^^^^^^^^^

**Line:** 133

**Description:**

    Load agent specification from file.

    Raises:
        FileNotFoundError: If the agent spec file is not found.
        AgentSpecError: If the agent spec is not valid.

**Parameters:**

    - ``agent_file`` (*Path*)

**Returns:** ``ResolvedAgentSpec``

**Calls:**

    - :ref:`AgentSpecError <func-AgentSpecError>`
    - :ref:`ResolvedAgentSpec <func-ResolvedAgentSpec>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_load_agent_spec <func-_load_agent_spec>`

**Called by:**

    - ``kimi_cli.soul.agent.load_agent``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_load_agent_spec`` - Line 79
