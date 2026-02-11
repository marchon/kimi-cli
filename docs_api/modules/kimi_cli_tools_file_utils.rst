kimi_cli.tools.file.utils
=========================

.. module:: kimi_cli.tools.file.utils

Source: :file:`src/kimi_cli/tools/file/utils.py`

Classes
-------

.. _class-FileType:

FileType
^^^^^^^^

FileType class.


Functions
---------

.. _kimi_cli.tools.file.utils.detect_file_type:

detect_file_type
^^^^^^^^^^^^^^^^

**Line:** 263

**Description:**

    Detect File Type.
    
    Args:
    path: Description.
    header: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``path`` (*str | PurePath*)
    - ``header`` (*bytes | None*) = ``None``

**Returns:** ``FileType``

**Calls:**

    - :ref:`FileType <func-FileType>`
    - :ref:`PurePath <func-PurePath>`
    - :ref:`guess_type <func-guess_type>`
    - :ref:`sniff_media_from_magic <func-sniff_media_from_magic>`
    - :ref:`lower <func-lower>`
    - :ref:`startswith <func-startswith>`
    - :ref:`str <func-str>`

**Called by:**

    - ``kimi_cli.tools.file.read.ReadFile.__call__``
    - ``kimi_cli.tools.file.read_media.ReadMediaFile.__call__``


.. _kimi_cli.tools.file.utils.sniff_media_from_magic:

sniff_media_from_magic
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 217

**Description:**

    Sniff Media From Magic.
    
    Args:
    data: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``data`` (*bytes*)

**Returns:** ``FileType | None``

**Calls:**

    - :ref:`FileType <func-FileType>`
    - :ref:`_sniff_ftyp_brand <func-_sniff_ftyp_brand>`
    - :ref:`len <func-len>`
    - :ref:`lower <func-lower>`
    - :ref:`startswith <func-startswith>`

**Called by:**

    - ``kimi_cli.tools.file.utils.detect_file_type``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_sniff_ftyp_brand`` - Line 202
