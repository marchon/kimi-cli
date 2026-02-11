kimi_cli.ui.shell.prompt
========================

.. module:: kimi_cli.ui.shell.prompt

Source: :file:`src/kimi_cli/ui/shell/prompt.py`

Classes
-------

.. _class-AttachmentCache:

AttachmentCache
^^^^^^^^^^^^^^^

AttachmentCache class.


.. _class-CachedAttachment:

CachedAttachment
^^^^^^^^^^^^^^^^

CachedAttachment class.


.. _class-CustomPromptSession:

CustomPromptSession
^^^^^^^^^^^^^^^^^^^

CustomPromptSession class.


.. _class-LocalFileMentionCompleter:

LocalFileMentionCompleter
^^^^^^^^^^^^^^^^^^^^^^^^^

Offer fuzzy \`@\` path completion by indexing workspace files.


.. _class-PromptMode:

PromptMode
^^^^^^^^^^

PromptMode class.


.. _class-SlashCommandCompleter:

SlashCommandCompleter
^^^^^^^^^^^^^^^^^^^^^

A completer that:
    - Shows one line per slash command in the form: "/name (alias1, alias2)"
    - Fuzzy-matches by primary name or any alias while inserting the canonical "/name"
    - Only activates when the current token starts with '/'


.. _class-UserInput:

UserInput
^^^^^^^^^

UserInput class.


Functions
---------

.. _kimi_cli.ui.shell.prompt.toast:

toast
^^^^^

**Line:** 551

**Description:**

    Toast.
    
    Args:
    message: Description.
    duration: Description.
    topic: Description.
    immediate: Description.
    position: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``message`` (*str*)
    - ``duration`` (*float*) = ``5.0``
    - ``topic`` (*str | None*) = ``None``
    - ``immediate`` (*bool*) = ``False``
    - ``position`` = ``'left'``

**Returns:** ``None``

**Calls:**

    - :ref:`_ToastEntry <func-_ToastEntry>`
    - :ref:`append <func-append>`
    - :ref:`appendleft <func-appendleft>`
    - :ref:`list <func-list>`
    - :ref:`max <func-max>`
    - :ref:`remove <func-remove>`

**Called by:**

    - ``kimi_cli.soul.toolset.KimiToolset.load_mcp_tools``
    - ``kimi_cli.ui.shell.__init__.Shell._auto_update``


Methods
-------

- ``AttachmentCache.load_bytes`` - Line 684
- ``AttachmentCache.load_content_parts`` - Line 700
- ``AttachmentCache.store_bytes`` - Line 650
- ``AttachmentCache.store_image`` - Line 679
- ``CustomPromptSession.prompt`` - Line 904
- ``LocalFileMentionCompleter.get_completions`` - Line 470
- ``PromptMode.toggle`` - Line 78
- ``SlashCommandCompleter.get_completions`` - Line 214

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_build_image_part`` - Line 600
- ``_current_toast`` - Line 167
- ``_guess_image_mime`` - Line 584
- ``_load_history_entries`` - Line 505
- ``_parse_attachment_kind`` - Line 136
- ``_sanitize_surrogates`` - Line 713
