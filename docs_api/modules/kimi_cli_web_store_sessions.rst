kimi_cli.web.store.sessions
===========================

.. module:: kimi_cli.web.store.sessions

Source: :file:`src/kimi_cli/web/store/sessions.py`

Classes
-------

.. _class-JointSession:

JointSession
^^^^^^^^^^^^

Combined session model with both web UI and kimi-cli session data.


.. _class-SessionIndexEntry:

SessionIndexEntry
^^^^^^^^^^^^^^^^^

SessionIndexEntry class.


.. _class-SessionMetadata:

SessionMetadata
^^^^^^^^^^^^^^^

Session metadata stored in metadata.json.


Functions
---------

.. _kimi_cli.web.store.sessions.invalidate_sessions_cache:

invalidate_sessions_cache
^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 37

**Description:**

    Clear the sessions cache.

    Call this after any mutation (create/update/delete).
    This ensures the next read sees fresh data.

**Returns:** ``None``

**Called by:**

    - ``kimi_cli.web.api.sessions.create_session``
    - ``kimi_cli.web.api.sessions.delete_session``
    - ``kimi_cli.web.api.sessions.fork_session``
    - ``kimi_cli.web.api.sessions.generate_session_title``
    - ``kimi_cli.web.api.sessions.update_session``
    - ``kimi_cli.web.store.sessions.run_auto_archive``


.. _kimi_cli.web.store.sessions.load_all_sessions:

load_all_sessions
^^^^^^^^^^^^^^^^^

**Line:** 420

**Description:**

    Load all sessions from all work directories.

**Returns:** ``list[JointSession]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`_build_joint_session <func-_build_joint_session>`
    - :ref:`_ensure_title <func-_ensure_title>`
    - :ref:`_load_sessions_index_cached <func-_load_sessions_index_cached>`
    - :ref:`sort <func-sort>`

**Called by:**

    - ``kimi_cli.web.store.sessions.load_all_sessions_cached``


.. _kimi_cli.web.store.sessions.load_all_sessions_cached:

load_all_sessions_cached
^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 432

**Description:**

    Cached version of load\_all\_sessions().

    Returns cached data if:
    - Cache exists AND
    - Cache is younger than CACHE\_TTL

    Otherwise, refreshes from disk and updates cache.

**Returns:** ``list[JointSession]``

**Calls:**

    - :ref:`load_all_sessions <func-load_all_sessions>`
    - :ref:`time <func-time>`


.. _kimi_cli.web.store.sessions.load_session_by_id:

load_session_by_id
^^^^^^^^^^^^^^^^^^

**Line:** 504

**Description:**

    Load a session by ID.

    This function first checks the cache/disk scan, then falls back to
    directly constructing the session from metadata if not found (handles
    newly created sessions with 

**Parameters:**

    - ``id`` (*UUID*)

**Returns:** ``JointSession | None``

**Calls:**

    - :ref:`SessionIndexEntry <func-SessionIndexEntry>`
    - :ref:`exists <func-exists>`
    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`_build_joint_session <func-_build_joint_session>`
    - :ref:`_ensure_title <func-_ensure_title>`
    - :ref:`load_session_metadata <func-load_session_metadata>`
    - :ref:`stat <func-stat>`
    - :ref:`str <func-str>`

**Called by:**

    - ``kimi_cli.web.api.sessions.get_editable_session``
    - ``kimi_cli.web.api.sessions.get_session``
    - ``kimi_cli.web.api.sessions.get_session_file``
    - ``kimi_cli.web.api.sessions.get_session_git_diff``
    - ``kimi_cli.web.api.sessions.get_session_upload_file``
    - ``kimi_cli.web.api.sessions.update_session``
    - ``kimi_cli.web.runner.process.SessionProcess._encode_uploaded_files``
    - ``kimi_cli.web.runner.worker.run_worker``


.. _kimi_cli.web.store.sessions.load_session_metadata:

load_session_metadata
^^^^^^^^^^^^^^^^^^^^^

**Line:** 121

**Description:**

    Load session metadata from metadata.json, or create default if not exists.

**Parameters:**

    - ``session_dir`` (*Path*)
    - ``session_id`` (*str*)

**Returns:** ``SessionMetadata``

**Calls:**

    - :ref:`SessionMetadata <func-SessionMetadata>`
    - :ref:`exists <func-exists>`
    - :ref:`loads <func-loads>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`read_text <func-read_text>`

**Called by:**

    - ``kimi_cli.web.api.sessions.fork_session``
    - ``kimi_cli.web.api.sessions.generate_session_title``
    - ``kimi_cli.web.api.sessions.update_session``
    - ``kimi_cli.web.store.sessions._build_sessions_index``
    - ``kimi_cli.web.store.sessions._ensure_title``
    - ``kimi_cli.web.store.sessions.load_session_by_id``


.. _kimi_cli.web.store.sessions.load_sessions_page:

load_sessions_page
^^^^^^^^^^^^^^^^^^

**Line:** 451

**Description:**

    Load a paginated list of sessions, optionally filtered by query and archived status.

    Args:
        limit: Maximum number of sessions to return.
        offset: Number of sessions to skip.
       

**Parameters:**

    - ``limit`` (*int*) = ``100``
    - ``offset`` (*int*) = ``0``
    - ``query`` (*str | None*) = ``None``
    - ``archived`` (*bool | None*) = ``None``

**Returns:** ``list[JointSession]``

**Calls:**

    - :ref:`_build_joint_session <func-_build_joint_session>`
    - :ref:`_ensure_title <func-_ensure_title>`
    - :ref:`_load_sessions_index_cached <func-_load_sessions_index_cached>`
    - :ref:`list <func-list>`
    - :ref:`lower <func-lower>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.list_sessions``


.. _kimi_cli.web.store.sessions.run_auto_archive:

run_auto_archive
^^^^^^^^^^^^^^^^

**Line:** 365

**Description:**

    Run auto-archive on old sessions.

    This function is designed to be called periodically (e.g., on app startup,
    or via a background task) rather than on every read operation.

    Returns:
     

**Returns:** ``int``

**Calls:**

    - :ref:`_build_sessions_index <func-_build_sessions_index>`
    - :ref:`_should_auto_archive <func-_should_auto_archive>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`save_session_metadata <func-save_session_metadata>`
    - :ref:`model_copy <func-model_copy>`
    - :ref:`time <func-time>`


.. _kimi_cli.web.store.sessions.save_session_metadata:

save_session_metadata
^^^^^^^^^^^^^^^^^^^^^

**Line:** 136

**Description:**

    Save session metadata to metadata.json.

**Parameters:**

    - ``session_dir`` (*Path*)
    - ``metadata`` (*SessionMetadata*)

**Returns:** ``None``

**Calls:**

    - :ref:`dumps <func-dumps>`
    - :ref:`exists <func-exists>`
    - :ref:`model_dump <func-model_dump>`
    - :ref:`write_text <func-write_text>`

**Called by:**

    - ``kimi_cli.web.api.sessions.fork_session``
    - ``kimi_cli.web.api.sessions.generate_session_title``
    - ``kimi_cli.web.api.sessions.update_session``
    - ``kimi_cli.web.store.sessions._ensure_title``
    - ``kimi_cli.web.store.sessions.run_auto_archive``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_build_joint_session`` - Line 286
- ``_build_kimi_session`` - Line 264
- ``_build_sessions_index`` - Line 325
- ``_derive_title_from_wire`` - Line 151
- ``_ensure_title`` - Line 218
- ``_iter_session_dirs`` - Line 191
- ``_load_sessions_index_cached`` - Line 406
- ``_should_auto_archive`` - Line 310
