kimi_cli.skill.flow.mermaid
===========================

.. module:: kimi_cli.skill.flow.mermaid

Source: :file:`src/kimi_cli/skill/flow/mermaid.py`

Functions
---------

.. _kimi_cli.skill.flow.mermaid.parse_mermaid_flowchart:

parse_mermaid_flowchart
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 79

**Description:**

    Parse Mermaid Flowchart.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``Flow``

**Calls:**

    - :ref:`Flow <func-Flow>`
    - :ref:`FlowEdge <func-FlowEdge>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`items <func-items>`
    - :ref:`_add_node <func-_add_node>`
    - :ref:`_infer_decision_nodes <func-_infer_decision_nodes>`
    - :ref:`_is_style_line <func-_is_style_line>`
    - :ref:`_strip_comment <func-_strip_comment>`
    - :ref:`_strip_style_tokens <func-_strip_style_tokens>`
    - ... and 7 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_add_node`` - Line 251
- ``_infer_decision_nodes`` - Line 398
- ``_is_style_line`` - Line 321
- ``_line_error`` - Line 294
- ``_normalize_edge_line`` - Line 375
- ``_parse_label`` - Line 186
- ``_parse_node_token`` - Line 160
- ``_skip_ws`` - Line 236
- ``_strip_comment`` - Line 307
- ``_strip_style_tokens`` - Line 346
- ``_try_parse_edge_line`` - Line 124
- ``_try_parse_node_line`` - Line 358
