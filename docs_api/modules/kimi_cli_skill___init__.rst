kimi_cli.skill.__init__
=======================

.. module:: kimi_cli.skill.__init__

Source: :file:`src/kimi_cli/skill/__init__.py`

Classes
-------

.. _class-Skill:

Skill
^^^^^

Information about a single skill.


Functions
---------

.. _kimi_cli.skill.__init__.discover_skills:

discover_skills
^^^^^^^^^^^^^^^

**Line:** 164

**Description:**

    Discover all skills in the given directory.

    Args:
        skills\_dir: Kaos path to the directory containing skills.

    Returns:
        List of Skill objects, one for each valid skill found.

**Parameters:**

    - ``skills_dir`` (*KaosPath*)

**Returns:** ``list[Skill]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`info <func-info>`
    - :ref:`is_dir <func-is_dir>`
    - :ref:`is_file <func-is_file>`
    - :ref:`iterdir <func-iterdir>`
    - :ref:`parse_skill_text <func-parse_skill_text>`
    - :ref:`read_text <func-read_text>`
    - :ref:`sorted <func-sorted>`

**Called by:**

    - ``kimi_cli.skill.__init__.discover_skills_from_roots``


.. _kimi_cli.skill.__init__.discover_skills_from_roots:

discover_skills_from_roots
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 142

**Description:**

    Discover skills from multiple directory roots.

**Parameters:**

    - ``skills_dirs`` (*Iterable[KaosPath]*)

**Returns:** ``list[Skill]``

**Calls:**

    - :ref:`discover_skills <func-discover_skills>`
    - :ref:`normalize_skill_name <func-normalize_skill_name>`
    - :ref:`sorted <func-sorted>`
    - :ref:`values <func-values>`

**Called by:**

    - ``kimi_cli.soul.agent.Runtime.create``


.. _kimi_cli.skill.__init__.find_first_existing_dir:

find_first_existing_dir
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 17

**Description:**

    Return the first existing directory from candidates.

**Parameters:**

    - ``candidates`` (*Iterable[KaosPath]*)

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`is_dir <func-is_dir>`

**Called by:**

    - ``kimi_cli.skill.__init__.find_project_skills_dir``
    - ``kimi_cli.skill.__init__.find_user_skills_dir``


.. _kimi_cli.skill.__init__.find_project_skills_dir:

find_project_skills_dir
^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 43

**Description:**

    Return the first existing project-level skills directory.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`find_first_existing_dir <func-find_first_existing_dir>`
    - :ref:`get_project_skills_dir_candidates <func-get_project_skills_dir_candidates>`

**Called by:**

    - ``kimi_cli.skill.__init__.resolve_skills_roots``


.. _kimi_cli.skill.__init__.find_user_skills_dir:

find_user_skills_dir
^^^^^^^^^^^^^^^^^^^^

**Line:** 61

**Description:**

    Return the first existing user-level skills directory.

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`find_first_existing_dir <func-find_first_existing_dir>`
    - :ref:`get_user_skills_dir_candidates <func-get_user_skills_dir_candidates>`

**Called by:**

    - ``kimi_cli.skill.__init__.resolve_skills_roots``


.. _kimi_cli.skill.__init__.get_builtin_skills_dir:

get_builtin_skills_dir
^^^^^^^^^^^^^^^^^^^^^^

**Line:** 26

**Description:**

    Get the built-in skills directory path.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`

**Called by:**

    - ``kimi_cli.skill.__init__.resolve_skills_roots``


.. _kimi_cli.skill.__init__.get_project_skills_dir_candidates:

get_project_skills_dir_candidates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 32

**Description:**

    Get project-level skills directory candidates in priority order.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Called by:**

    - ``kimi_cli.skill.__init__.find_project_skills_dir``


.. _kimi_cli.skill.__init__.get_user_skills_dir_candidates:

get_user_skills_dir_candidates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 49

**Description:**

    Get user-level skills directory candidates in priority order.

**Calls:**

    - :ref:`home <func-home>`

**Called by:**

    - ``kimi_cli.skill.__init__.find_user_skills_dir``


.. _kimi_cli.skill.__init__.index_skills:

index_skills
^^^^^^^^^^^^

**Line:** 138

**Description:**

    Build a lookup table for skills by normalized name.

**Parameters:**

    - ``skills`` (*Iterable[Skill]*)

**Calls:**

    - :ref:`normalize_skill_name <func-normalize_skill_name>`

**Called by:**

    - ``kimi_cli.soul.agent.Runtime.create``


.. _kimi_cli.skill.__init__.normalize_skill_name:

normalize_skill_name
^^^^^^^^^^^^^^^^^^^^

**Line:** 134

**Description:**

    Normalize a skill name for lookup.

**Parameters:**

    - ``name`` (*str*)

**Returns:** ``str``

**Calls:**

    - :ref:`casefold <func-casefold>`

**Called by:**

    - ``kimi_cli.skill.__init__.discover_skills_from_roots``
    - ``kimi_cli.skill.__init__.index_skills``


.. _kimi_cli.skill.__init__.parse_skill_text:

parse_skill_text
^^^^^^^^^^^^^^^^

**Line:** 196

**Description:**

    Parse SKILL.md contents to extract name and description.

**Parameters:**

    - ``content`` (*str*)
    - ``dir_path`` (*KaosPath*)

**Returns:** ``Skill``

**Calls:**

    - :ref:`Skill <func-Skill>`
    - :ref:`ValueError <func-ValueError>`
    - :ref:`error <func-error>`
    - :ref:`get <func-get>`
    - :ref:`_parse_flow_from_skill <func-_parse_flow_from_skill>`
    - :ref:`parse_frontmatter <func-parse_frontmatter>`

**Called by:**

    - ``kimi_cli.skill.__init__.discover_skills``


.. _kimi_cli.skill.__init__.read_skill_text:

read_skill_text
^^^^^^^^^^^^^^^

**Line:** 152

**Description:**

    Read the SKILL.md contents for a skill.

**Parameters:**

    - ``skill`` (*Skill*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`read_text <func-read_text>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul._make_skill_runner``


.. _kimi_cli.skill.__init__.resolve_skills_roots:

resolve_skills_roots
^^^^^^^^^^^^^^^^^^^^

**Line:** 111

**Description:**

    Resolve layered skill roots in priority order.

    Built-in skills load first when supported by the active KAOS backend. When an
    override is provided, user/project discovery is skipped.

**Parameters:**

    - ``work_dir`` (*KaosPath*)
    - ``skills_dir_override`` (*KaosPath | None*) = ``None``

**Returns:** ``list[KaosPath]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`_supports_builtin_skills <func-_supports_builtin_skills>`
    - :ref:`find_project_skills_dir <func-find_project_skills_dir>`
    - :ref:`find_user_skills_dir <func-find_user_skills_dir>`
    - :ref:`get_builtin_skills_dir <func-get_builtin_skills_dir>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`

**Called by:**

    - ``kimi_cli.soul.agent.Runtime.create``


Methods
-------

- ``Skill.skill_md_file`` - Line 79

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_is_fence_close`` - Line 336
- ``_iter_fenced_codeblocks`` - Line 257
- ``_normalize_code_lang`` - Line 294
- ``_parse_fence_open`` - Line 311
- ``_parse_flow_block`` - Line 241
- ``_parse_flow_from_skill`` - Line 224
- ``_supports_builtin_skills`` - Line 106
