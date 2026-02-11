kimi_cli.soul.slash
===================

.. module:: kimi_cli.soul.slash

Source: :file:`src/kimi_cli/soul/slash.py`

Functions
---------

.. _kimi_cli.soul.slash.clear:

clear
^^^^^

**Line:** 31

**Description:**

    Clear the context

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`command <func-command>`
    - :ref:`info <func-info>`
    - :ref:`clear <func-clear>`
    - :ref:`wire_send <func-wire_send>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul.compact_context``
    - ``kimi_cli.soul.slash.clear``


.. _kimi_cli.soul.slash.compact:

compact
^^^^^^^

**Line:** 39

**Description:**

    Compact the context

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`compact_context <func-compact_context>`
    - :ref:`info <func-info>`
    - :ref:`wire_send <func-wire_send>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul.compact_context``


.. _kimi_cli.soul.slash.init:

init
^^^^

**Line:** 51

**Description:**

    Analyze the codebase and generate an \`AGENTS.md\` file

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Context <func-Context>`
    - :ref:`KimiSoul <func-KimiSoul>`
    - :ref:`Message <func-Message>`
    - :ref:`Path <func-Path>`
    - :ref:`TemporaryDirectory <func-TemporaryDirectory>`
    - :ref:`append_message <func-append_message>`
    - :ref:`load_agents_md <func-load_agents_md>`
    - :ref:`system <func-system>`
    - :ref:`run <func-run>`


.. _kimi_cli.soul.slash.yolo:

yolo
^^^^

**Line:** 69

**Description:**

    Toggle YOLO mode (auto-approve all actions)

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`TextPart <func-TextPart>`
    - :ref:`is_yolo <func-is_yolo>`
    - :ref:`set_yolo <func-set_yolo>`
    - :ref:`wire_send <func-wire_send>`

