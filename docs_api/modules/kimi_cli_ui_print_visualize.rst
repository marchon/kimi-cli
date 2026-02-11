kimi_cli.ui.print.visualize
===========================

.. module:: kimi_cli.ui.print.visualize

Source: :file:`src/kimi_cli/ui/print/visualize.py`

Classes
-------

.. _class-FinalOnlyJsonPrinter:

FinalOnlyJsonPrinter
^^^^^^^^^^^^^^^^^^^^

FinalOnlyJsonPrinter class.


.. _class-FinalOnlyTextPrinter:

FinalOnlyTextPrinter
^^^^^^^^^^^^^^^^^^^^

FinalOnlyTextPrinter class.


.. _class-JsonPrinter:

JsonPrinter
^^^^^^^^^^^

JsonPrinter class.


.. _class-Printer:

Printer
^^^^^^^

Printer class.


.. _class-TextPrinter:

TextPrinter
^^^^^^^^^^^

TextPrinter class.


Functions
---------

.. _kimi_cli.ui.print.visualize.visualize:

visualize
^^^^^^^^^

**Line:** 185

**Description:**

    Visualize.
    
    Args:
    output\_format: Description.
    final\_only: Description.
    wire: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``output_format`` (*OutputFormat*)
    - ``final_only`` (*bool*)
    - ``wire`` (*Wire*)

**Returns:** ``None``

**Calls:**

    - :ref:`FinalOnlyJsonPrinter <func-FinalOnlyJsonPrinter>`
    - :ref:`FinalOnlyTextPrinter <func-FinalOnlyTextPrinter>`
    - :ref:`TextPrinter <func-TextPrinter>`
    - :ref:`feed <func-feed>`
    - :ref:`flush <func-flush>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`receive <func-receive>`
    - :ref:`ui_side <func-ui_side>`


Methods
-------

- ``FinalOnlyJsonPrinter.feed`` - Line 166
- ``FinalOnlyJsonPrinter.flush`` - Line 175
- ``FinalOnlyTextPrinter.feed`` - Line 141
- ``FinalOnlyTextPrinter.flush`` - Line 150
- ``JsonPrinter.feed`` - Line 81
- ``JsonPrinter.flush`` - Line 106
- ``Printer.feed`` - Line 23
- ``Printer.flush`` - Line 24
- ``TextPrinter.feed`` - Line 59
- ``TextPrinter.flush`` - Line 62

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_merge_content`` - Line 41
