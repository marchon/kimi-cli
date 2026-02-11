kimi_cli.web.api.sessions
=========================

.. module:: kimi_cli.web.api.sessions

Source: :file:`src/kimi_cli/web/api/sessions.py`

Classes
-------

.. _class-CreateSessionRequest:

CreateSessionRequest
^^^^^^^^^^^^^^^^^^^^

Create session request.


.. _class-ForkSessionRequest:

ForkSessionRequest
^^^^^^^^^^^^^^^^^^

Fork session request.


.. _class-UploadSessionFileResponse:

UploadSessionFileResponse
^^^^^^^^^^^^^^^^^^^^^^^^^

Upload file response.


Functions
---------

.. _kimi_cli.web.api.sessions.create_session:

create_session
^^^^^^^^^^^^^^

**Line:** 535

**Description:**

    Create a new session.

**Parameters:**

    - ``request`` (*CreateSessionRequest | None*) = ``None``

**Returns:** ``Session``

**Calls:**

    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`Path <func-Path>`
    - :ref:`SessionStatus <func-SessionStatus>`
    - :ref:`UUID <func-UUID>`
    - :ref:`create <func-create>`
    - :ref:`exists <func-exists>`
    - :ref:`expanduser <func-expanduser>`
    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`home <func-home>`
    - :ref:`is_dir <func-is_dir>`
    - ... and 9 more


.. _kimi_cli.web.api.sessions.delete_session:

delete_session
^^^^^^^^^^^^^^

**Line:** 763

**Description:**

    Delete a session.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``None``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`delete <func-delete>`
    - :ref:`exists <func-exists>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`save_metadata <func-save_metadata>`
    - :ref:`get_editable_session <func-get_editable_session>`
    - :ref:`get_session <func-get_session>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`rmtree <func-rmtree>`
    - :ref:`stop <func-stop>`
    - ... and 1 more


.. _kimi_cli.web.api.sessions.extract_first_turn_from_wire:

extract_first_turn_from_wire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 828

**Description:**

    Extract the first turn's user message and assistant response from wire.jsonl.

    Returns:
        tuple[str, str] | None: (user\_message, assistant\_response) or None if not found

**Parameters:**

    - ``session_dir`` (*Path*)

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`append <func-append>`
    - :ref:`exists <func-exists>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`get <func-get>`
    - :ref:`join <func-join>`
    - :ref:`loads <func-loads>`
    - :ref:`open <func-open>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.generate_session_title``


.. _kimi_cli.web.api.sessions.fork_session:

fork_session
^^^^^^^^^^^^

**Line:** 993

**Description:**

    Fork a session, creating a new session with history up to the specified turn.

    The new session shares the same work\_dir as the original session.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``request`` (*ForkSessionRequest*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``Session``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`SessionMetadata <func-SessionMetadata>`
    - :ref:`SessionStatus <func-SessionStatus>`
    - :ref:`UUID <func-UUID>`
    - :ref:`add <func-add>`
    - :ref:`append <func-append>`
    - :ref:`copy2 <func-copy2>`
    - :ref:`create <func-create>`
    - :ref:`dumps <func-dumps>`
    - ... and 23 more


.. _kimi_cli.web.api.sessions.generate_session_title:

generate_session_title
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 1105

**Description:**

    Generate a concise session title using AI based on the first conversation turn.

    If request body is empty or parameters are missing, the backend will
    automatically read the first turn from wir

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``request`` (*GenerateTitleRequest | None*) = ``None``
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``GenerateTitleResponse``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`GenerateTitleResponse <func-GenerateTitleResponse>`
    - :ref:`Message <func-Message>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`generate <func-generate>`
    - :ref:`get <func-get>`
    - :ref:`join <func-join>`
    - :ref:`load_config <func-load_config>`
    - :ref:`create_llm <func-create_llm>`
    - :ref:`extract_first_turn_from_wire <func-extract_first_turn_from_wire>`
    - ... and 11 more


.. _kimi_cli.web.api.sessions.get_editable_session:

get_editable_session
^^^^^^^^^^^^^^^^^^^^

**Line:** 335

**Description:**

    Get a session and verify it's not busy.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``JointSession``

**Calls:**

    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`get_session <func-get_session>`
    - :ref:`load_session_by_id <func-load_session_by_id>`

**Called by:**

    - ``kimi_cli.web.api.sessions.delete_session``
    - ``kimi_cli.web.api.sessions.fork_session``
    - ``kimi_cli.web.api.sessions.generate_session_title``
    - ``kimi_cli.web.api.sessions.update_session``
    - ``kimi_cli.web.api.sessions.upload_session_file``


.. _kimi_cli.web.api.sessions.get_runner:

get_runner
^^^^^^^^^^

**Line:** 72

**Description:**

    Get the KimiCLIRunner from the FastAPI app state.

**Parameters:**

    - ``req`` (*Request*)

**Returns:** ``KimiCLIRunner``


.. _kimi_cli.web.api.sessions.get_runner_ws:

get_runner_ws
^^^^^^^^^^^^^

**Line:** 76

**Description:**

    Get the KimiCLIRunner from the FastAPI app state (for WebSocket routes).

**Parameters:**

    - ``ws`` (*WebSocket*)

**Returns:** ``KimiCLIRunner``


.. _kimi_cli.web.api.sessions.get_session:

get_session
^^^^^^^^^^^

**Line:** 522

**Description:**

    Get a session by ID.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``Session | None``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`get_session <func-get_session>`
    - :ref:`load_session_by_id <func-load_session_by_id>`

**Called by:**

    - ``kimi_cli.web.api.sessions.delete_session``
    - ``kimi_cli.web.api.sessions.get_editable_session``
    - ``kimi_cli.web.api.sessions.get_session``
    - ``kimi_cli.web.api.sessions.list_sessions``


.. _kimi_cli.web.api.sessions.get_session_file:

get_session_file
^^^^^^^^^^^^^^^^

**Line:** 678

**Description:**

    Get a file or list directory from session work directory.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``path`` (*str*)
    - ``request`` (*Request*)

**Returns:** ``Response``

**Calls:**

    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`Path <func-Path>`
    - :ref:`Response <func-Response>`
    - :ref:`append <func-append>`
    - :ref:`cast <func-cast>`
    - :ref:`dumps <func-dumps>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`getattr <func-getattr>`
    - :ref:`guess_type <func-guess_type>`
    - ... and 15 more


.. _kimi_cli.web.api.sessions.get_session_git_diff:

get_session_git_diff
^^^^^^^^^^^^^^^^^^^^

**Line:** 91

**Description:**

    get git diff stats for the session's work directory

**Parameters:**

    - ``session_id`` (*UUID*)

**Returns:** ``GitDiffStats``

**Calls:**

    - :ref:`GitDiffStats <func-GitDiffStats>`
    - :ref:`GitFileDiff <func-GitFileDiff>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`Path <func-Path>`
    - :ref:`append <func-append>`
    - :ref:`communicate <func-communicate>`
    - :ref:`create_subprocess_exec <func-create_subprocess_exec>`
    - :ref:`decode <func-decode>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - ... and 7 more


.. _kimi_cli.web.api.sessions.get_session_upload_file:

get_session_upload_file
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 632

**Description:**

    Get a file from a session's uploads directory.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``path`` (*str*)

**Returns:** ``Response``

**Calls:**

    - :ref:`FileResponse <func-FileResponse>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`guess_type <func-guess_type>`
    - :ref:`is_file <func-is_file>`
    - :ref:`is_relative_to <func-is_relative_to>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`quote <func-quote>`
    - :ref:`resolve <func-resolve>`


.. _kimi_cli.web.api.sessions.get_startup_dir:

get_startup_dir
^^^^^^^^^^^^^^^

**Line:** 252

**Description:**

    Get the directory where kimi web was started.

**Parameters:**

    - ``request`` (*Request*)

**Returns:** ``str``

**Calls:**

    - :ref:`get <func-get>`


.. _kimi_cli.web.api.sessions.get_work_dirs:

get_work_dirs
^^^^^^^^^^^^^

**Line:** 317

**Description:**

    Get a list of available work directories from metadata.

**Returns:** ``list[str]``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`to_thread <func-to_thread>`


.. _kimi_cli.web.api.sessions.invalidate_work_dirs_cache:

invalidate_work_dirs_cache
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 80

**Description:**

    Clear the work dirs cache.

**Returns:** ``None``

**Called by:**

    - ``kimi_cli.web.api.sessions.create_session``
    - ``kimi_cli.web.api.sessions.fork_session``


.. _kimi_cli.web.api.sessions.list_sessions:

list_sessions
^^^^^^^^^^^^^

**Line:** 487

**Description:**

    List sessions with optional pagination and search.

    Args:
        limit: Maximum number of sessions to return (default 100, max 500).
        offset: Number of sessions to skip (default 0).
      

**Parameters:**

    - ``runner`` (*KimiCLIRunner*)
    - ``limit`` (*int*) = ``100``
    - ``offset`` (*int*) = ``0``
    - ``q`` (*str | None*) = ``None``
    - ``archived`` (*bool | None*) = ``None``

**Returns:** ``list[Session]``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`cast <func-cast>`
    - :ref:`get_session <func-get_session>`
    - :ref:`load_sessions_page <func-load_sessions_page>`
    - :ref:`to_thread <func-to_thread>`


.. _kimi_cli.web.api.sessions.replay_history:

replay_history
^^^^^^^^^^^^^^

**Line:** 473

**Description:**

    Replay historical wire messages from wire.jsonl to a WebSocket.

**Parameters:**

    - ``ws`` (*WebSocket*)
    - ``session_dir`` (*Path*)

**Returns:** ``None``

**Calls:**

    - :ref:`send_text <func-send_text>`
    - :ref:`to_thread <func-to_thread>`

**Called by:**

    - ``kimi_cli.web.api.sessions.session_stream``


.. _kimi_cli.web.api.sessions.sanitize_filename:

sanitize_filename
^^^^^^^^^^^^^^^^^

**Line:** 243

**Description:**

    Remove potentially dangerous characters from filename.

**Parameters:**

    - ``filename`` (*str*)

**Returns:** ``str``

**Calls:**

    - :ref:`isalnum <func-isalnum>`
    - :ref:`join <func-join>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.upload_session_file``


.. _kimi_cli.web.api.sessions.session_stream:

session_stream
^^^^^^^^^^^^^^

**Line:** 1237

**Description:**

    WebSocket stream for a session.

    Flow:
    1. Accept the WebSocket connection
    2. If history exists, attach WebSocket in replay mode
    3. Replay history messages from wire.jsonl
    4. Start 

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``websocket`` (*WebSocket*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``None``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`JSONRPCErrorObject <func-JSONRPCErrorObject>`
    - :ref:`JSONRPCErrorResponse <func-JSONRPCErrorResponse>`
    - :ref:`Path <func-Path>`
    - :ref:`SessionStatus <func-SessionStatus>`
    - :ref:`accept <func-accept>`
    - :ref:`add_websocket_and_begin_replay <func-add_websocket_and_begin_replay>`
    - :ref:`close <func-close>`
    - :ref:`debug <func-debug>`
    - :ref:`end_replay <func-end_replay>`
    - ... and 23 more


.. _kimi_cli.web.api.sessions.truncate_context_at_turn:

truncate_context_at_turn
^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 955

**Description:**

    Read context.jsonl and return all lines up to and including the given turn.

    Turn detection is based on real user messages, excluding synthetic checkpoint
    user entries like \`\`<system>CHECKPOIN

**Parameters:**

    - ``context_path`` (*Path*)
    - ``turn_index`` (*int*)

**Returns:** ``list[str]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`_is_checkpoint_user_message <func-_is_checkpoint_user_message>`
    - :ref:`loads <func-loads>`
    - :ref:`open <func-open>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.fork_session``


.. _kimi_cli.web.api.sessions.truncate_wire_at_turn:

truncate_wire_at_turn
^^^^^^^^^^^^^^^^^^^^^

**Line:** 882

**Description:**

    Read wire.jsonl and return all lines up to and including the given turn.

    Args:
        wire\_path: Path to the wire.jsonl file
        turn\_index: 0-based turn index. Returns turns 0..turn\_index i

**Parameters:**

    - ``wire_path`` (*Path*)
    - ``turn_index`` (*int*)

**Returns:** ``list[str]``

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`append <func-append>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`loads <func-loads>`
    - :ref:`open <func-open>`
    - :ref:`strip <func-strip>`

**Called by:**

    - ``kimi_cli.web.api.sessions.fork_session``


.. _kimi_cli.web.api.sessions.update_session:

update_session
^^^^^^^^^^^^^^

**Line:** 783

**Description:**

    Update a session (e.g., rename title or archive/unarchive).

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``request`` (*UpdateSessionRequest*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``Session``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`get_editable_session <func-get_editable_session>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`load_session_metadata <func-load_session_metadata>`
    - :ref:`save_session_metadata <func-save_session_metadata>`
    - :ref:`model_copy <func-model_copy>`
    - :ref:`patch <func-patch>`
    - :ref:`str <func-str>`
    - ... and 1 more


.. _kimi_cli.web.api.sessions.upload_session_file:

upload_session_file
^^^^^^^^^^^^^^^^^^^

**Line:** 593

**Description:**

    Upload a file to a session.

**Parameters:**

    - ``session_id`` (*UUID*)
    - ``file`` (*UploadFile*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``UploadSessionFileResponse``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`UploadSessionFileResponse <func-UploadSessionFileResponse>`
    - :ref:`get_editable_session <func-get_editable_session>`
    - :ref:`sanitize_filename <func-sanitize_filename>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`post <func-post>`
    - :ref:`read <func-read>`
    - :ref:`splitext <func-splitext>`
    - :ref:`str <func-str>`
    - ... and 2 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_contains_symlink`` - Line 385
- ``_ensure_public_file_access_allowed`` - Line 411
- ``_get_work_dirs_sync`` - Line 288
- ``_is_checkpoint_user_message`` - Line 937
- ``_is_path_in_sensitive_location`` - Line 398
- ``_is_sensitive_relative_path`` - Line 367
- ``_read_wire_lines`` - Line 442
- ``_relative_parts`` - Line 355
- ``_update_last_session_id`` - Line 321
