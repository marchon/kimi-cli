kimi_cli.utils.path
===================

.. module:: kimi_cli.utils.path

Source: :file:`src/kimi_cli/utils/path.py`

Functions
---------

.. _kimi_cli.utils.path.is_within_directory:

is_within_directory
^^^^^^^^^^^^^^^^^^^

**Line:** 10

**Description:**

    Check whether \*path\* is contained within \*directory\* using pure path semantics.
    Both arguments should already be canonicalized (e.g. via KaosPath.canonical()).

**Parameters:**

    - ``path`` (*KaosPath*)
    - ``directory`` (*KaosPath*)

**Returns:** ``bool``

**Calls:**

    - :ref:`PurePath <func-PurePath>`
    - :ref:`relative_to <func-relative_to>`
    - :ref:`str <func-str>`

**Called by:**

    - ``kimi_cli.tools.file.glob.Glob._validate_directory``
    - ``kimi_cli.tools.file.read.ReadFile._validate_path``
    - ``kimi_cli.tools.file.read_media.ReadMediaFile._validate_path``
    - ``kimi_cli.tools.file.replace.StrReplaceFile.__call__``
    - ``kimi_cli.tools.file.replace.StrReplaceFile._validate_path``
    - ``kimi_cli.tools.file.write.WriteFile.__call__``
    - ``kimi_cli.tools.file.write.WriteFile._validate_path``


.. _kimi_cli.utils.path.list_directory:

list_directory
^^^^^^^^^^^^^^

**Line:** 23

**Description:**

    Return an \`\`ls\`\`-like listing of \*work\_dir\*.

    This helper is used mainly to provide context to the LLM (for example
    \`\`KIMI\_WORK\_DIR\_LS\`\`) and to show top-level directory contents in tools.
   

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``str``

**Calls:**

    - :ref:`S_ISDIR <func-S_ISDIR>`
    - :ref:`append <func-append>`
    - :ref:`iterdir <func-iterdir>`
    - :ref:`join <func-join>`
    - :ref:`stat <func-stat>`

**Called by:**

    - ``kimi_cli.soul.agent.Runtime.create``
    - ``kimi_cli.tools.file.glob.Glob._validate_pattern``


.. _kimi_cli.utils.path.next_available_rotation:

next_available_rotation
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 100

**Description:**

    Return a reserved rotation path for \*path\* or \`\`None\`\` if parent is missing.

    The caller must overwrite/reuse the returned path immediately because this helper
    commits an empty placeholder fil

**Parameters:**

    - ``path`` (*Path*)

**Returns:** ``Path | None``

**Calls:**

    - :ref:`compile <func-compile>`
    - :ref:`escape <func-escape>`
    - :ref:`exists <func-exists>`
    - :ref:`group <func-group>`
    - :ref:`int <func-int>`
    - :ref:`_reserve_rotation_path <func-_reserve_rotation_path>`
    - :ref:`listdir <func-listdir>`
    - :ref:`match <func-match>`
    - :ref:`max <func-max>`

**Called by:**

    - ``kimi_cli.soul.context.Context.clear``
    - ``kimi_cli.soul.context.Context.revert_to``
    - ``kimi_cli.tools.multiagent.task.Task._get_subagent_context_file``


.. _kimi_cli.utils.path.shorten_home:

shorten_home
^^^^^^^^^^^^

**Line:** 55

**Description:**

    Convert absolute path to use \`~\` for home directory.

**Parameters:**

    - ``path`` (*KaosPath*)

**Returns:** ``KaosPath``

**Calls:**

    - :ref:`KaosPath <func-KaosPath>`
    - :ref:`home <func-home>`
    - :ref:`relative_to <func-relative_to>`

**Called by:**

    - ``kimi_cli.app.KimiCLI.run_shell``


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_reserve_rotation_path`` - Line 87
