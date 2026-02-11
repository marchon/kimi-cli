kimi_cli.skill.flow.__init__
============================

.. module:: kimi_cli.skill.flow.__init__

Source: :file:`src/kimi_cli/skill/flow/__init__.py`

Classes
-------

.. _class-Flow:

Flow
^^^^

Flow class.


.. _class-FlowEdge:

FlowEdge
^^^^^^^^

FlowEdge class.


.. _class-FlowError:

FlowError
^^^^^^^^^

Base error for flow parsing/validation.


.. _class-FlowNode:

FlowNode
^^^^^^^^

FlowNode class.


.. _class-FlowParseError:

FlowParseError
^^^^^^^^^^^^^^

Raised when prompt flow parsing fails.


.. _class-FlowValidationError:

FlowValidationError
^^^^^^^^^^^^^^^^^^^

Raised when a flowchart fails validation.


Functions
---------

.. _kimi_cli.skill.flow.__init__.parse_choice:

parse_choice
^^^^^^^^^^^^

**Line:** 118

**Description:**

    Parse Choice.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`findall <func-findall>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.FlowRunner._execute_flow_node``


.. _kimi_cli.skill.flow.__init__.validate_flow:

validate_flow
^^^^^^^^^^^^^

**Line:** 46

**Description:**

    Validate Flow.
    
    Args:
    nodes: Description.
    outgoing: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``nodes``
    - ``outgoing``

**Calls:**

    - :ref:`FlowValidationError <func-FlowValidationError>`
    - :ref:`add <func-add>`
    - :ref:`append <func-append>`
    - :ref:`get <func-get>`
    - :ref:`len <func-len>`
    - :ref:`pop <func-pop>`
    - :ref:`set <func-set>`
    - :ref:`strip <func-strip>`
    - :ref:`values <func-values>`

**Called by:**

    - ``kimi_cli.skill.flow.d2.parse_d2_flowchart``
    - ``kimi_cli.skill.flow.mermaid.parse_mermaid_flowchart``

