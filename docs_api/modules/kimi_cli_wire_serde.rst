kimi_cli.wire.serde
===================

.. module:: kimi_cli.wire.serde

Source: :file:`src/kimi_cli/wire/serde.py`

Functions
---------

.. _kimi_cli.wire.serde.deserialize_wire_message:

deserialize_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 6

**Description:**

    Convert a jsonifiable dict into a \`WireMessage\`.

    Raises:
        ValueError: If the message type is unknown or the payload is invalid.

**Parameters:**

    - ``data``

**Returns:** ``WireMessage``

**Calls:**

    - :ref:`model_validate <func-model_validate>`
    - :ref:`to_wire_message <func-to_wire_message>`

**Called by:**

    - ``kimi_cli.web.api.sessions._read_wire_lines``
    - ``kimi_cli.web.runner.process.SessionProcess._read_loop``


.. _kimi_cli.wire.serde.serialize_wire_message:

serialize_wire_message
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 16

**Description:**

    Convert a \`WireMessage\` into a jsonifiable dict.

**Parameters:**

    - ``msg`` (*WireMessage*)

**Calls:**

    - :ref:`from_wire_message <func-from_wire_message>`
    - :ref:`model_dump <func-model_dump>`

**Called by:**

    - ``kimi_cli.wire.jsonrpc.JSONRPCEventMessage._serialize_params``
    - ``kimi_cli.wire.jsonrpc.JSONRPCRequestMessage._serialize_params``

