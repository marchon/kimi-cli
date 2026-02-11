kimi_cli.ui.shell.keyboard
==========================

.. module:: kimi_cli.ui.shell.keyboard

Source: :file:`src/kimi_cli/ui/shell/keyboard.py`

Classes
-------

.. _class-KeyEvent:

KeyEvent
^^^^^^^^

KeyEvent class.


.. _class-KeyboardListener:

KeyboardListener
^^^^^^^^^^^^^^^^

KeyboardListener class.


Functions
---------

.. _kimi_cli.ui.shell.keyboard.listen_for_keyboard:

listen_for_keyboard
^^^^^^^^^^^^^^^^^^^

**Line:** 110

**Description:**

    Listen For Keyboard.

**Returns:** ``AsyncGenerator[KeyEvent]``

**Calls:**

    - :ref:`KeyboardListener <func-KeyboardListener>`
    - :ref:`get <func-get>`
    - :ref:`start <func-start>`
    - :ref:`stop <func-stop>`


Methods
-------

- ``KeyboardListener.get`` - Line 107
- ``KeyboardListener.pause`` - Line 96
- ``KeyboardListener.resume`` - Line 104
- ``KeyboardListener.start`` - Line 68
- ``KeyboardListener.stop`` - Line 86

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_listen_for_keyboard_thread`` - Line 123
- ``_listen_for_keyboard_unix`` - Line 146
- ``_listen_for_keyboard_windows`` - Line 244
