kimi_cli.utils.media_tags
=========================

.. module:: kimi_cli.utils.media_tags

Source: :file:`src/kimi_cli/utils/media_tags.py`

Functions
---------

.. _kimi_cli.utils.media_tags.wrap_media_part:

wrap_media_part
^^^^^^^^^^^^^^^

**Line:** 43

**Description:**

    Wrap Media Part.
    
    Args:
    part: Description.
    tag: Description.
    attrs: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``part`` (*ContentPart*)
    - ``tag`` (*str*)
    - ``attrs`` = ``None``

**Returns:** ``list[ContentPart]``

**Calls:**

    - :ref:`TextPart <func-TextPart>`
    - :ref:`_format_tag <func-_format_tag>`

**Called by:**

    - ``kimi_cli.tools.file.read_media.ReadMediaFile._read_media``
    - ``kimi_cli.ui.shell.prompt.AttachmentCache.load_content_parts``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_format_tag`` - Line 21
