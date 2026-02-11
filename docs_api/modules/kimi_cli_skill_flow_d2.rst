kimi_cli.skill.flow.d2
======================

.. module:: kimi_cli.skill.flow.d2

Source: :file:`src/kimi_cli/skill/flow/d2.py`

Functions
---------

.. _kimi_cli.skill.flow.d2.parse_d2_flowchart:

parse_d2_flowchart
^^^^^^^^^^^^^^^^^^

**Line:** 90

**Description:**

    Parse D2 Flowchart.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``Flow``

**Calls:**

    - :ref:`Flow <func-Flow>`
    - :ref:`items <func-items>`
    - :ref:`_has_unquoted_token <func-_has_unquoted_token>`
    - :ref:`_infer_decision_nodes <func-_infer_decision_nodes>`
    - :ref:`_iter_top_level_statements <func-_iter_top_level_statements>`
    - :ref:`_normalize_markdown_blocks <func-_normalize_markdown_blocks>`
    - :ref:`_parse_edge_statement <func-_parse_edge_statement>`
    - :ref:`_parse_node_statement <func-_parse_node_statement>`
    - :ref:`setdefault <func-setdefault>`
    - :ref:`validate_flow <func-validate_flow>`


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_add_node`` - Line 595
- ``_dedent_block`` - Line 214
- ``_escape_quoted_line`` - Line 236
- ``_has_unquoted_token`` - Line 342
- ``_infer_decision_nodes`` - Line 645
- ``_is_property_path`` - Line 452
- ``_iter_top_level_statements`` - Line 248
- ``_line_error`` - Line 670
- ``_normalize_markdown_blocks`` - Line 119
- ``_parse_edge_statement`` - Line 356
- ``_parse_label`` - Line 470
- ``_parse_node_id`` - Line 430
- ``_parse_node_statement`` - Line 405
- ``_parse_quoted_label`` - Line 488
- ``_split_on_token`` - Line 523
- ``_split_unquoted_once`` - Line 564
- ``_strip_unquoted_comment`` - Line 184
