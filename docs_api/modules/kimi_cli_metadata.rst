kimi_cli.metadata
=================

.. module:: kimi_cli.metadata

Source: :file:`src/kimi_cli/metadata.py`

Classes
-------

.. _class-Metadata:

Metadata
^^^^^^^^

Kimi metadata structure.


.. _class-WorkDirMeta:

WorkDirMeta
^^^^^^^^^^^

Metadata for a work directory.


Functions
---------

.. _kimi_cli.metadata.get_metadata_file:

get_metadata_file
^^^^^^^^^^^^^^^^^

**Line:** 12

**Description:**

    Get Metadata File.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - ``kimi_cli.metadata.load_metadata``
    - ``kimi_cli.metadata.save_metadata``


.. _kimi_cli.metadata.load_metadata:

load_metadata
^^^^^^^^^^^^^

**Line:** 75

**Description:**

    Load Metadata.

**Returns:** ``Metadata``

**Calls:**

    - :ref:`Metadata <func-Metadata>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`get_metadata_file <func-get_metadata_file>`
    - :ref:`load <func-load>`
    - :ref:`open <func-open>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.session.Session.continue_``
    - ``kimi_cli.session.Session.create``
    - ``kimi_cli.session.Session.find``
    - ``kimi_cli.session.Session.list``
    - ``kimi_cli.web.api.sessions._get_work_dirs_sync``
    - ``kimi_cli.web.api.sessions._update_last_session_id``
    - ``kimi_cli.web.api.sessions.delete_session``
    - ``kimi_cli.web.store.sessions._build_sessions_index``
    - ``kimi_cli.web.store.sessions.load_session_by_id``


.. _kimi_cli.metadata.save_metadata:

save_metadata
^^^^^^^^^^^^^

**Line:** 18

**Description:**

    Save Metadata.
    
    Args:
    metadata: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``metadata`` (*Metadata*)

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`get_metadata_file <func-get_metadata_file>`
    - :ref:`model_dump <func-model_dump>`
    - :ref:`open <func-open>`

**Called by:**

    - ``kimi_cli.cli.__init__.kimi``
    - ``kimi_cli.session.Session.create``
    - ``kimi_cli.web.api.sessions._update_last_session_id``
    - ``kimi_cli.web.api.sessions.delete_session``


Methods
-------

- ``Metadata.get_work_dir_meta`` - Line 62
- ``Metadata.new_work_dir_meta`` - Line 69
- ``WorkDirMeta.sessions_dir`` - Line 46
