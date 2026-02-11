kimi_cli.web.runner.messages
============================

.. module:: kimi_cli.web.runner.messages

Source: :file:`src/kimi_cli/web/runner/messages.py`

Classes
-------

.. _class-JSONRPCHistoryCompleteMessage:

JSONRPCHistoryCompleteMessage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sent after history replay, before environment is ready.


.. _class-JSONRPCSessionStatusMessage:

JSONRPCSessionStatusMessage
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Session status update message.


Functions
---------

.. _kimi_cli.web.runner.messages.new_history_complete_message:

new_history_complete_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 43

**Description:**

    Create a new history complete message.

**Returns:** ``JSONRPCHistoryCompleteMessage``

**Calls:**

    - :ref:`JSONRPCHistoryCompleteMessage <func-JSONRPCHistoryCompleteMessage>`
    - :ref:`str <func-str>`
    - :ref:`uuid4 <func-uuid4>`

**Called by:**

    - ``kimi_cli.web.runner.messages.send_history_complete``


.. _kimi_cli.web.runner.messages.new_session_status_message:

new_session_status_message
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 47

**Description:**

    Create a new session status message.

**Parameters:**

    - ``status`` (*SessionStatus*)

**Returns:** ``JSONRPCSessionStatusMessage``

**Calls:**

    - :ref:`JSONRPCSessionStatusMessage <func-JSONRPCSessionStatusMessage>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``
    - ``kimi_cli.web.runner.process.SessionProcess._emit_status``
    - ``kimi_cli.web.runner.process.SessionProcess.send_status_snapshot``


.. _kimi_cli.web.runner.messages.send_history_complete:

send_history_complete
^^^^^^^^^^^^^^^^^^^^^

**Line:** 51

**Description:**

    Send history complete message to a WebSocket.

    Returns:
        True if message was sent successfully, False if the send fails or the WebSocket is not
        connected.

**Parameters:**

    - ``ws`` (*WebSocket*)

**Returns:** ``bool``

**Calls:**

    - :ref:`new_history_complete_message <func-new_history_complete_message>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`send_text <func-send_text>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``

