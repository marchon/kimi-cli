kimi_cli.utils.slashcmd
=======================

.. module:: kimi_cli.utils.slashcmd

Source: :file:`src/kimi_cli/utils/slashcmd.py`

Classes
-------

.. _class-SlashCommand:

SlashCommand
^^^^^^^^^^^^

SlashCommand class.


.. _class-SlashCommandCall:

SlashCommandCall
^^^^^^^^^^^^^^^^

SlashCommandCall class.


.. _class-SlashCommandRegistry:

SlashCommandRegistry
^^^^^^^^^^^^^^^^^^^^

Registry for slash commands.


Functions
---------

.. _kimi_cli.utils.slashcmd.parse_slash_command_call:

parse_slash_command_call
^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 31

**Description:**

    Parse a slash command call from user input.

    Returns:
        SlashCommandCall if a slash command is found, else None. The \`args\` field contains
        the raw argument string after the command n

**Parameters:**

    - ``user_input`` (*str*)

**Returns:** ``SlashCommandCall | None``

**Calls:**

    - :ref:`SlashCommandCall <func-SlashCommandCall>`
    - :ref:`end <func-end>`
    - :ref:`group <func-group>`
    - :ref:`isspace <func-isspace>`
    - :ref:`len <func-len>`
    - :ref:`lstrip <func-lstrip>`
    - :ref:`match <func-match>`
    - :ref:`startswith <func-startswith>`

**Called by:**

    - ``kimi_cli.soul.kimisoul.KimiSoul.run``
    - ``kimi_cli.ui.shell.__init__.Shell._run_shell_command``
    - ``kimi_cli.ui.shell.__init__.Shell.run``
    - ``kimi_cli.ui.shell.replay._is_clear_command_input``


Methods
-------

- ``SlashCommand.slash_name`` - Line 16
- ``SlashCommandRegistry.command`` - Line 74
- ``SlashCommandRegistry.find_command`` - Line 121
- ``SlashCommandRegistry.list_commands`` - Line 124
