kimi_cli.wire.file
==================

.. module:: kimi_cli.wire.file

Source: :file:`src/kimi_cli/wire/file.py`

Classes
-------

.. _class-WireFile:

WireFile
^^^^^^^^

WireFile class.


.. _class-WireFileMetadata:

WireFileMetadata
^^^^^^^^^^^^^^^^

Metadata header stored as the first line in wire.jsonl.


.. _class-WireMessageRecord:

WireMessageRecord
^^^^^^^^^^^^^^^^^

The persisted record of a \`WireMessage\`.


Functions
---------

.. _kimi_cli.wire.file.parse_wire_file_line:

parse_wire_file_line
^^^^^^^^^^^^^^^^^^^^

**Line:** 72

**Description:**

    Parse a wire file line into metadata or a message record.

**Parameters:**

    - ``line`` (*str*)

**Returns:** ``WireFileMetadata | WireMessageRecord``

**Calls:**

    - :ref:`parse_wire_file_metadata <func-parse_wire_file_metadata>`
    - :ref:`model_validate_json <func-model_validate_json>`

**Called by:**

    - ``kimi_cli.wire.file.WireFile.iter_records``


.. _kimi_cli.wire.file.parse_wire_file_metadata:

parse_wire_file_metadata
^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 65

**Description:**

    Parse a wire file metadata line; return None if the line is not metadata.

**Parameters:**

    - ``line`` (*str*)

**Returns:** ``WireFileMetadata | None``

**Calls:**

    - :ref:`model_validate_json <func-model_validate_json>`

**Called by:**

    - ``kimi_cli.wire.file.WireFile.is_empty``
    - ``kimi_cli.wire.file._load_protocol_version``
    - ``kimi_cli.wire.file.parse_wire_file_line``


Methods
-------

- ``WireFile.append_message`` - Line 140
- ``WireFile.append_record`` - Line 147
- ``WireFile.is_empty`` - Line 101
- ``WireFile.iter_records`` - Line 118
- ``WireFile.version`` - Line 98
- ``WireMessageRecord.from_wire_message`` - Line 31
- ``WireMessageRecord.to_wire_message`` - Line 34

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_dump_line`` - Line 53
- ``_load_protocol_version`` - Line 156
