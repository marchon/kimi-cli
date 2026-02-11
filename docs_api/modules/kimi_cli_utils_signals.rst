kimi_cli.utils.signals
======================

.. module:: kimi_cli.utils.signals

Source: :file:`src/kimi_cli/utils/signals.py`

Functions
---------

.. _kimi_cli.utils.signals.install_sigint_handler:

install_sigint_handler
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 7

**Description:**

    Install a SIGINT handler that works on Unix and Windows.

    On Unix event loops, prefer \`loop.add\_signal\_handler\`.
    On Windows (or other platforms) where it is not implemented, fall back to
    \`

**Parameters:**

    - ``loop`` (*asyncio.AbstractEventLoop*)
    - ``handler``

**Calls:**

    - :ref:`add_signal_handler <func-add_signal_handler>`
    - :ref:`getsignal <func-getsignal>`
    - :ref:`handler <func-handler>`
    - :ref:`remove_signal_handler <func-remove_signal_handler>`
    - :ref:`signal <func-signal>`
    - :ref:`suppress <func-suppress>`

**Called by:**

    - ``kimi_cli.ui.print.__init__.Print.run``
    - ``kimi_cli.ui.shell.__init__.Shell._run_shell_command``
    - ``kimi_cli.ui.shell.__init__.Shell.run_soul_command``
    - ``kimi_cli.wire.server.WireServer.serve``

