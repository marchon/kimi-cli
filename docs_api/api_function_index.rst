API Function Index
==================

This page provides an alphabetical index of all public functions in the codebase.
Each function entry shows:

- **Module**: Where the function is defined
- **Line**: Line number in the source file
- **Parameters**: Function parameters with types and defaults
- **Returns**: Return type
- **Calls**: Functions this function calls
- **Called by**: Functions that call this one

.. contents::
   :local:
   :depth: 2


_
-

.. _func-_ApprovalRequestPanel.get_selected_response:

_ApprovalRequestPanel.get_selected_response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 473)

**Description:**

    Get the approval response based on selected option.

**Parameters:**

    - ``self``

**Returns:** ``ApprovalResponse.Kind``


.. _func-_ApprovalRequestPanel.move_down:

_ApprovalRequestPanel.move_down
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 469)

**Description:**

    Move selection down.

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`len <func-len>`


.. _func-_ApprovalRequestPanel.move_up:

_ApprovalRequestPanel.move_up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 465)

**Description:**

    Move selection up.

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`len <func-len>`


.. _func-_ApprovalRequestPanel.render:

_ApprovalRequestPanel.render
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 411)

**Description:**

    Render the approval menu as a panel.

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``

**Calls:**

    - :ref:`Group <func-Group>`
    - :ref:`Padding <func-Padding>`
    - :ref:`Text <func-Text>`
    - :ref:`_render_block <func-_render_block>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`escape <func-escape>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`min <func-min>`


.. _func-_ApprovalRequestPanel.render_full:

_ApprovalRequestPanel.render_full
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 461)

**Description:**

    Render full content for pager (no truncation).

**Parameters:**

    - ``self``

**Returns:** ``list[RenderableType]``

**Calls:**

    - :ref:`_render_block <func-_render_block>`


.. _func-_ContentBlock.append:

_ContentBlock.append
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 188)

**Parameters:**

    - ``self``
    - ``content`` (*str*)

**Returns:** ``None``


.. _func-_ContentBlock.compose:

_ContentBlock.compose
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 176)

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``


.. _func-_ContentBlock.compose_final:

_ContentBlock.compose_final
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 179)

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Markdown <func-Markdown>`


.. _func-_LiveView.append_content:

_LiveView.append_content
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 712)

**Parameters:**

    - ``self``
    - ``part`` (*ContentPart*)

**Returns:** ``None``

**Calls:**

    - :ref:`_ContentBlock <func-_ContentBlock>`
    - :ref:`append <func-append>`
    - :ref:`flush_content <func-flush_content>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.append_tool_call:

_LiveView.append_tool_call
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 730)

**Parameters:**

    - ``self``
    - ``tool_call`` (*ToolCall*)

**Returns:** ``None``

**Calls:**

    - :ref:`_ToolCallBlock <func-_ToolCallBlock>`
    - :ref:`flush_content <func-flush_content>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.append_tool_call_part:

_LiveView.append_tool_call_part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 736)

**Parameters:**

    - ``self``
    - ``part`` (*ToolCallPart*)

**Returns:** ``None``

**Calls:**

    - :ref:`append_args_part <func-append_args_part>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.append_tool_result:

_LiveView.append_tool_result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 744)

**Parameters:**

    - ``self``
    - ``result`` (*ToolResult*)

**Returns:** ``None``

**Calls:**

    - :ref:`finish <func-finish>`
    - :ref:`flush_finished_tool_calls <func-flush_finished_tool_calls>`
    - :ref:`get <func-get>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.cleanup:

_LiveView.cleanup
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 670)

**Description:**

    Cleanup the live view on step end or interruption.

**Parameters:**

    - ``self``
    - ``is_interrupt`` (*bool*)

**Returns:** ``None``

**Calls:**

    - :ref:`ToolError <func-ToolError>`
    - :ref:`ToolOk <func-ToolOk>`
    - :ref:`finish <func-finish>`
    - :ref:`flush_content <func-flush_content>`
    - :ref:`flush_finished_tool_calls <func-flush_finished_tool_calls>`
    - :ref:`popleft <func-popleft>`
    - :ref:`resolve <func-resolve>`
    - :ref:`values <func-values>`


.. _func-_LiveView.compose:

_LiveView.compose
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 562)

**Description:**

    Compose the live view display content.

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``

**Calls:**

    - :ref:`Group <func-Group>`
    - :ref:`append <func-append>`
    - :ref:`compose <func-compose>`
    - :ref:`render <func-render>`
    - :ref:`values <func-values>`


.. _func-_LiveView.dispatch_keyboard_event:

_LiveView.dispatch_keyboard_event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 631)

**Parameters:**

    - ``self``
    - ``event`` (*KeyEvent*)

**Returns:** ``None``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`get_selected_response <func-get_selected_response>`
    - :ref:`move_down <func-move_down>`
    - :ref:`move_up <func-move_up>`
    - :ref:`popleft <func-popleft>`
    - :ref:`refresh_soon <func-refresh_soon>`
    - :ref:`remove <func-remove>`
    - :ref:`resolve <func-resolve>`
    - :ref:`set <func-set>`
    - :ref:`show_next_approval_request <func-show_next_approval_request>`


.. _func-_LiveView.dispatch_wire_message:

_LiveView.dispatch_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 579)

**Description:**

    Dispatch the Wire message to UI components.

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`Panel <func-Panel>`
    - :ref:`Spinner <func-Spinner>`
    - :ref:`Text <func-Text>`
    - :ref:`append_content <func-append_content>`
    - :ref:`append_tool_call_part <func-append_tool_call_part>`
    - :ref:`append_tool_result <func-append_tool_result>`
    - :ref:`cleanup <func-cleanup>`
    - :ref:`flush_content <func-flush_content>`
    - :ref:`handle_subagent_event <func-handle_subagent_event>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`message_stringify <func-message_stringify>`
    - :ref:`print <func-print>`
    - :ref:`refresh_soon <func-refresh_soon>`
    - :ref:`request_approval <func-request_approval>`
    - :ref:`update <func-update>`
    - :ref:`warning <func-warning>`


.. _func-_LiveView.flush_content:

_LiveView.flush_content
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 691)

**Description:**

    Flush the current content block.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`compose_final <func-compose_final>`
    - :ref:`print <func-print>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.flush_finished_tool_calls:

_LiveView.flush_finished_tool_calls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 698)

**Description:**

    Flush all leading finished tool call blocks.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`compose <func-compose>`
    - :ref:`keys <func-keys>`
    - :ref:`list <func-list>`
    - :ref:`pop <func-pop>`
    - :ref:`print <func-print>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.handle_subagent_event:

_LiveView.handle_subagent_event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 782)

**Parameters:**

    - ``self``
    - ``event`` (*SubagentEvent*)

**Returns:** ``None``

**Calls:**

    - :ref:`append_sub_tool_call_part <func-append_sub_tool_call_part>`
    - :ref:`finish_sub_tool_call <func-finish_sub_tool_call>`
    - :ref:`get <func-get>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.refresh_soon:

_LiveView.refresh_soon
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 559)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-_LiveView.request_approval:

_LiveView.request_approval
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 750)

**Parameters:**

    - ``self``
    - ``request`` (*ApprovalRequest*)

**Returns:** ``None``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`bell <func-bell>`
    - :ref:`resolve <func-resolve>`
    - :ref:`show_next_approval_request <func-show_next_approval_request>`


.. _func-_LiveView.show_next_approval_request:

_LiveView.show_next_approval_request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 762)

**Description:**

    Show the next approval request from the queue.
        If there are no pending requests, clear the current approval panel.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`_ApprovalRequestPanel <func-_ApprovalRequestPanel>`
    - :ref:`popleft <func-popleft>`
    - :ref:`refresh_soon <func-refresh_soon>`


.. _func-_LiveView.visualize_loop:

_LiveView.visualize_loop
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 507)

**Parameters:**

    - ``self``
    - ``wire`` (*WireUISide*)

**Calls:**

    - :ref:`Live <func-Live>`
    - :ref:`_reset_live_shape <func-_reset_live_shape>`
    - :ref:`cleanup <func-cleanup>`
    - :ref:`compose <func-compose>`
    - :ref:`dispatch_keyboard_event <func-dispatch_keyboard_event>`
    - :ref:`dispatch_wire_message <func-dispatch_wire_message>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_keyboard_listener <func-_keyboard_listener>`
    - :ref:`_show_approval_in_pager <func-_show_approval_in_pager>`
    - :ref:`pause <func-pause>`
    - :ref:`receive <func-receive>`
    - :ref:`resume <func-resume>`
    - :ref:`start <func-start>`
    - :ref:`stop <func-stop>`
    - :ref:`update <func-update>`


.. _func-_ModelIDConv.from_acp_model_id:

_ModelIDConv.from_acp_model_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 47)

**Parameters:**

    - ``cls``
    - ``model_id`` (*str*)

**Returns:** ``\_ModelIDConv``

**Calls:**

    - :ref:`_ModelIDConv <func-_ModelIDConv>`
    - :ref:`endswith <func-endswith>`
    - :ref:`len <func-len>`


.. _func-_ModelIDConv.to_acp_model_id:

_ModelIDConv.to_acp_model_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 52)

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-_NullWritable.can_write_eof:

_NullWritable.can_write_eof
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 165)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-_NullWritable.close:

_NullWritable.close
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 168)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-_NullWritable.drain:

_NullWritable.drain
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 171)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-_NullWritable.is_closing:

_NullWritable.is_closing
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 174)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-_NullWritable.wait_closed:

_NullWritable.wait_closed
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 177)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-_NullWritable.write:

_NullWritable.write
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 180)

**Parameters:**

    - ``self``
    - ``data`` (*bytes*)

**Returns:** ``None``


.. _func-_NullWritable.write_eof:

_NullWritable.write_eof
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 186)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-_NullWritable.writelines:

_NullWritable.writelines
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 183)

**Returns:** ``None``


.. _func-_StatusBlock.render:

_StatusBlock.render
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 143)

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``


.. _func-_StatusBlock.update:

_StatusBlock.update
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 146)

**Parameters:**

    - ``self``
    - ``status`` (*StatusUpdate*)

**Returns:** ``None``


.. _func-_ToolCallBlock.append_args_part:

_ToolCallBlock.append_args_part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 225)

**Parameters:**

    - ``self``
    - ``args_part`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`_get_headline_markup <func-_get_headline_markup>`
    - :ref:`append_string <func-append_string>`
    - :ref:`extract_key_argument <func-extract_key_argument>`
    - :ref:`from_markup <func-from_markup>`


.. _func-_ToolCallBlock.append_sub_tool_call:

_ToolCallBlock.append_sub_tool_call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 242)

**Parameters:**

    - ``self``
    - ``tool_call`` (*ToolCall*)


.. _func-_ToolCallBlock.append_sub_tool_call_part:

_ToolCallBlock.append_sub_tool_call_part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 246)

**Parameters:**

    - ``self``
    - ``tool_call_part`` (*ToolCallPart*)


.. _func-_ToolCallBlock.compose:

_ToolCallBlock.compose
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 218)

**Parameters:**

    - ``self``

**Returns:** ``RenderableType``


.. _func-_ToolCallBlock.finish:

_ToolCallBlock.finish
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 238)

**Parameters:**

    - ``self``
    - ``result`` (*ToolReturnValue*)

**Calls:**

    - :ref:`_compose <func-_compose>`


.. _func-_ToolCallBlock.finish_sub_tool_call:

_ToolCallBlock.finish_sub_tool_call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 256)

**Parameters:**

    - ``self``
    - ``tool_result`` (*ToolResult*)

**Calls:**

    - :ref:`FinishedSubCall <func-FinishedSubCall>`
    - :ref:`_compose <func-_compose>`
    - :ref:`append <func-append>`
    - :ref:`pop <func-pop>`


.. _func-_ToolCallBlock.finished:

_ToolCallBlock.finished
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 222)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-_ToolCallState.acp_tool_call_id:

_ToolCallState.acp_tool_call_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 124)

**Parameters:**

    - ``self``

**Returns:** ``str``

**Calls:**

    - :ref:`get <func-get>`


.. _func-_ToolCallState.append_args_part:

_ToolCallState.append_args_part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 133)

**Description:**

    Append a new arguments part to the accumulated args and lexer.

**Parameters:**

    - ``self``
    - ``args_part`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`append_string <func-append_string>`


.. _func-_ToolCallState.get_title:

_ToolCallState.get_title
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 138)

**Description:**

    Get the current title with subtitle if available.

**Parameters:**

    - ``self``

**Returns:** ``str``

**Calls:**

    - :ref:`extract_key_argument <func-extract_key_argument>`


.. _func-_WireRecorder.join:

_WireRecorder.join
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 37)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`suppress <func-suppress>`



A
-

.. _func-acp:

acp
^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 35)

**Description:**

    Run Kimi Code CLI ACP server.

**Calls:**

    - :ref:`acp_main <func-acp_main>`
    - :ref:`command <func-command>`


.. _func-ACP.run:

ACP.run
^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 99)

**Description:**

    Run the ACP server.

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`ACPServerSingleSession <func-ACPServerSingleSession>`
    - :ref:`info <func-info>`
    - :ref:`run_agent <func-run_agent>`


.. _func-acp_blocks_to_content_parts:

acp_blocks_to_content_parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.convert``

**File:** :file:`src/kimi_cli/acp/convert.py` (line 14)

**Description:**

    Acp Blocks To Content Parts.
    
    Args:
    prompt: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``prompt`` (*list[ACPContentBlock]*)

**Returns:** ``list[ContentPart]``

**Calls:**

    - :ref:`ImageURLPart <func-ImageURLPart>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`append <func-append>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`prompt <func-prompt>` (from ``kimi_cli.acp.session.ACPSession``)


.. _func-acp_main:

acp_main
^^^^^^^^

**Module:** ``kimi_cli.acp.__init__``

**File:** :file:`src/kimi_cli/acp/__init__.py` (line 1)

**Description:**

    Entry point for the multi-session ACP server.

**Returns:** ``None``

**Calls:**

    - :ref:`ACPServer <func-ACPServer>`
    - :ref:`info <func-info>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`run <func-run>`
    - :ref:`run_agent <func-run_agent>`

**Called by:**

    - :ref:`acp <func-acp>` (from ``kimi_cli.cli.__init__``)


.. _func-acp_mcp_servers_to_mcp_config:

acp_mcp_servers_to_mcp_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.mcp``

**File:** :file:`src/kimi_cli/acp/mcp.py` (line 9)

**Description:**

    Acp Mcp Servers To Mcp Config.
    
    Args:
    mcp\_servers: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``mcp_servers`` (*list[MCPServer]*)

**Returns:** ``MCPConfig``

**Calls:**

    - :ref:`MCPConfig <func-MCPConfig>`
    - :ref:`MCPConfigError <func-MCPConfigError>`
    - :ref:`_convert_acp_mcp_server <func-_convert_acp_mcp_server>`
    - :ref:`model_validate <func-model_validate>`

**Called by:**

    - :ref:`load_session <func-load_session>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`new_session <func-new_session>` (from ``kimi_cli.acp.server.ACPServer``)


.. _func-ACPKaos.chdir:

ACPKaos.chdir
^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 48)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)

**Returns:** ``None``

**Calls:**

    - :ref:`chdir <func-chdir>`


.. _func-ACPKaos.exec:

ACPKaos.exec
^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 132)

**Parameters:**

    - ``self``
    - ``*args`` (*str*)
    - ``env`` = ``None``

**Returns:** ``KaosProcess``

**Calls:**

    - :ref:`exec <func-exec>`


.. _func-ACPKaos.getcwd:

ACPKaos.getcwd
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 45)

**Parameters:**

    - ``self``

**Returns:** ``KaosPath``

**Calls:**

    - :ref:`getcwd <func-getcwd>`


.. _func-ACPKaos.gethome:

ACPKaos.gethome
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 42)

**Parameters:**

    - ``self``

**Returns:** ``KaosPath``

**Calls:**

    - :ref:`gethome <func-gethome>`


.. _func-ACPKaos.glob:

ACPKaos.glob
^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 57)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``pattern`` (*str*)
    - ``case_sensitive`` (*bool*) = ``True``

**Returns:** ``AsyncGenerator[KaosPath]``

**Calls:**

    - :ref:`glob <func-glob>`


.. _func-ACPKaos.iterdir:

ACPKaos.iterdir
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 54)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)

**Returns:** ``AsyncGenerator[KaosPath]``

**Calls:**

    - :ref:`iterdir <func-iterdir>`


.. _func-ACPKaos.mkdir:

ACPKaos.mkdir
^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 127)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``parents`` (*bool*) = ``False``
    - ``exist_ok`` (*bool*) = ``False``

**Returns:** ``None``

**Calls:**

    - :ref:`mkdir <func-mkdir>`


.. _func-ACPKaos.normpath:

ACPKaos.normpath
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 39)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)

**Returns:** ``KaosPath``

**Calls:**

    - :ref:`normpath <func-normpath>`


.. _func-ACPKaos.pathclass:

ACPKaos.pathclass
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 36)

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`pathclass <func-pathclass>`


.. _func-ACPKaos.readbytes:

ACPKaos.readbytes
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 62)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``n`` (*int | None*) = ``None``

**Returns:** ``bytes``

**Calls:**

    - :ref:`readbytes <func-readbytes>`


.. _func-ACPKaos.readlines:

ACPKaos.readlines
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 78)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``encoding`` (*str*) = ``'utf-8'``
    - ``errors`` = ``'strict'``

**Returns:** ``AsyncGenerator[str]``

**Calls:**

    - :ref:`readtext <func-readtext>`
    - :ref:`splitlines <func-splitlines>`


.. _func-ACPKaos.readtext:

ACPKaos.readtext
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 65)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``encoding`` (*str*) = ``'utf-8'``
    - ``errors`` = ``'strict'``

**Returns:** ``str``

**Calls:**

    - :ref:`_abs_path <func-_abs_path>`
    - :ref:`read_text_file <func-read_text_file>`
    - :ref:`readtext <func-readtext>`


.. _func-ACPKaos.stat:

ACPKaos.stat
^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 51)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``follow_symlinks`` (*bool*) = ``True``

**Returns:** ``StatResult``

**Calls:**

    - :ref:`stat <func-stat>`


.. _func-ACPKaos.writebytes:

ACPKaos.writebytes
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 89)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``data`` (*bytes*)

**Returns:** ``int``

**Calls:**

    - :ref:`writebytes <func-writebytes>`


.. _func-ACPKaos.writetext:

ACPKaos.writetext
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 92)

**Parameters:**

    - ``self``
    - ``path`` (*StrOrKaosPath*)
    - ``data`` (*str*)
    - ``mode`` = ``'w'``
    - ``encoding`` (*str*) = ``'utf-8'``
    - ``errors`` = ``'strict'``

**Returns:** ``int``

**Calls:**

    - :ref:`_abs_path <func-_abs_path>`
    - :ref:`len <func-len>`
    - :ref:`readtext <func-readtext>`
    - :ref:`write_text_file <func-write_text_file>`
    - :ref:`writetext <func-writetext>`


.. _func-ACPProcess.kill:

ACPProcess.kill
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 226)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`kill <func-kill>`


.. _func-ACPProcess.pid:

ACPProcess.pid
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 216)

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-ACPProcess.returncode:

ACPProcess.returncode
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 220)

**Parameters:**

    - ``self``

**Returns:** ``int | None``


.. _func-ACPProcess.wait:

ACPProcess.wait
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.kaos``

**File:** :file:`src/kimi_cli/acp/kaos.py` (line 223)

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-ACPServer.authenticate:

ACPServer.authenticate
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 351)

**Parameters:**

    - ``self``
    - ``method_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.AuthenticateResponse | None``


.. _func-ACPServer.cancel:

ACPServer.cancel
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 364)

**Parameters:**

    - ``self``
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``

**Calls:**

    - :ref:`cancel <func-cancel>`
    - :ref:`error <func-error>`
    - :ref:`info <func-info>`
    - :ref:`invalid_params <func-invalid_params>`


.. _func-ACPServer.ext_method:

ACPServer.ext_method
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 372)

**Parameters:**

    - ``self``
    - ``method`` (*str*)
    - ``params``


.. _func-ACPServer.ext_notification:

ACPServer.ext_notification
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 375)

**Parameters:**

    - ``self``
    - ``method`` (*str*)
    - ``params``

**Returns:** ``None``


.. _func-ACPServer.initialize:

ACPServer.initialize
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 108)

**Parameters:**

    - ``self``
    - ``protocol_version`` (*int*)
    - ``client_capabilities`` (*acp.schema.ClientCapabilities | None*) = ``None``
    - ``client_info`` (*acp.schema.Implementation | None*) = ``None``
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.InitializeResponse``

**Calls:**

    - :ref:`AgentCapabilities <func-AgentCapabilities>`
    - :ref:`AuthMethod <func-AuthMethod>`
    - :ref:`Implementation <func-Implementation>`
    - :ref:`InitializeResponse <func-InitializeResponse>`
    - :ref:`McpCapabilities <func-McpCapabilities>`
    - :ref:`PromptCapabilities <func-PromptCapabilities>`
    - :ref:`SessionCapabilities <func-SessionCapabilities>`
    - :ref:`SessionListCapabilities <func-SessionListCapabilities>`
    - :ref:`endswith <func-endswith>`
    - :ref:`index <func-index>`
    - :ref:`info <func-info>`


.. _func-ACPServer.list_sessions:

ACPServer.list_sessions
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 280)

**Parameters:**

    - ``self``
    - ``cursor`` (*str | None*) = ``None``
    - ``cwd`` (*str | None*) = ``None``
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.schema.ListSessionsResponse``

**Calls:**

    - :ref:`ListSessionsResponse <func-ListSessionsResponse>`
    - :ref:`Path <func-Path>`
    - :ref:`SessionInfo <func-SessionInfo>`
    - :ref:`astimezone <func-astimezone>`
    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`info <func-info>`
    - :ref:`isoformat <func-isoformat>`
    - :ref:`list <func-list>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`


.. _func-ACPServer.load_session:

ACPServer.load_session
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 239)

**Parameters:**

    - ``self``
    - ``cwd`` (*str*)
    - ``mcp_servers`` (*list[MCPServer]*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``

**Calls:**

    - :ref:`ACPKaos <func-ACPKaos>`
    - :ref:`ACPSession <func-ACPSession>`
    - :ref:`Path <func-Path>`
    - :ref:`_ModelIDConv <func-_ModelIDConv>`
    - :ref:`create <func-create>`
    - :ref:`error <func-error>`
    - :ref:`find <func-find>`
    - :ref:`info <func-info>`
    - :ref:`invalid_params <func-invalid_params>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`acp_mcp_servers_to_mcp_config <func-acp_mcp_servers_to_mcp_config>`
    - :ref:`replace_tools <func-replace_tools>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`
    - :ref:`warning <func-warning>`


.. _func-ACPServer.new_session:

ACPServer.new_session
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 179)

**Parameters:**

    - ``self``
    - ``cwd`` (*str*)
    - ``mcp_servers`` (*list[MCPServer]*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.NewSessionResponse``

**Calls:**

    - :ref:`ACPKaos <func-ACPKaos>`
    - :ref:`ACPSession <func-ACPSession>`
    - :ref:`AvailableCommand <func-AvailableCommand>`
    - :ref:`AvailableCommandsUpdate <func-AvailableCommandsUpdate>`
    - :ref:`NewSessionResponse <func-NewSessionResponse>`
    - :ref:`Path <func-Path>`
    - :ref:`SessionMode <func-SessionMode>`
    - :ref:`SessionModeState <func-SessionModeState>`
    - :ref:`SessionModelState <func-SessionModelState>`
    - :ref:`_ModelIDConv <func-_ModelIDConv>`
    - :ref:`create_task <func-create_task>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`acp_mcp_servers_to_mcp_config <func-acp_mcp_servers_to_mcp_config>`
    - :ref:`_expand_llm_models <func-_expand_llm_models>`
    - :ref:`replace_tools <func-replace_tools>`
    - :ref:`list_commands <func-list_commands>`
    - :ref:`session_update <func-session_update>`
    - :ref:`to_acp_model_id <func-to_acp_model_id>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`


.. _func-ACPServer.on_connect:

ACPServer.on_connect
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 104)

**Parameters:**

    - ``self``
    - ``conn`` (*acp.Client*)

**Returns:** ``None``

**Calls:**

    - :ref:`info <func-info>`


.. _func-ACPServer.prompt:

ACPServer.prompt
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 354)

**Parameters:**

    - ``self``
    - ``prompt`` (*list[ACPContentBlock]*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.PromptResponse``

**Calls:**

    - :ref:`error <func-error>`
    - :ref:`info <func-info>`
    - :ref:`invalid_params <func-invalid_params>`
    - :ref:`prompt <func-prompt>`


.. _func-ACPServer.set_session_mode:

ACPServer.set_session_mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 301)

**Parameters:**

    - ``self``
    - ``mode_id`` (*str*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``


.. _func-ACPServer.set_session_model:

ACPServer.set_session_model
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.server``

**File:** :file:`src/kimi_cli/acp/server.py` (line 304)

**Parameters:**

    - ``self``
    - ``model_id`` (*str*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``

**Calls:**

    - :ref:`error <func-error>`
    - :ref:`from_acp_model_id <func-from_acp_model_id>`
    - :ref:`get <func-get>`
    - :ref:`info <func-info>`
    - :ref:`invalid_params <func-invalid_params>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`create_llm <func-create_llm>`


.. _func-ACPServerSingleSession.authenticate:

ACPServerSingleSession.authenticate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 76)

**Parameters:**

    - ``self``
    - ``method_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.AuthenticateResponse | None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.cancel:

ACPServerSingleSession.cancel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 84)

**Parameters:**

    - ``self``
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.ext_method:

ACPServerSingleSession.ext_method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 87)

**Parameters:**

    - ``self``
    - ``method`` (*str*)
    - ``params``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.ext_notification:

ACPServerSingleSession.ext_notification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 90)

**Parameters:**

    - ``self``
    - ``method`` (*str*)
    - ``params``

**Returns:** ``None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.initialize:

ACPServerSingleSession.initialize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 42)

**Parameters:**

    - ``self``
    - ``protocol_version`` (*int*)
    - ``client_capabilities`` (*acp.schema.ClientCapabilities | None*) = ``None``
    - ``client_info`` (*acp.schema.Implementation | None*) = ``None``
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.InitializeResponse``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.list_sessions:

ACPServerSingleSession.list_sessions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 61)

**Parameters:**

    - ``self``
    - ``cursor`` (*str | None*) = ``None``
    - ``cwd`` (*str | None*) = ``None``
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.schema.ListSessionsResponse``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.load_session:

ACPServerSingleSession.load_session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 56)

**Parameters:**

    - ``self``
    - ``cwd`` (*str*)
    - ``mcp_servers`` (*list[MCPServer]*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.new_session:

ACPServerSingleSession.new_session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 51)

**Parameters:**

    - ``self``
    - ``cwd`` (*str*)
    - ``mcp_servers`` (*list[MCPServer]*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.NewSessionResponse``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.on_connect:

ACPServerSingleSession.on_connect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 35)

**Parameters:**

    - ``self``
    - ``conn`` (*acp.Client*)

**Returns:** ``None``

**Calls:**

    - :ref:`info <func-info>`


.. _func-ACPServerSingleSession.prompt:

ACPServerSingleSession.prompt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 79)

**Parameters:**

    - ``self``
    - ``prompt`` (*list[ACPContentBlock]*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.PromptResponse``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.set_session_mode:

ACPServerSingleSession.set_session_mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 66)

**Parameters:**

    - ``self``
    - ``mode_id`` (*str*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.SetSessionModeResponse | None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPServerSingleSession.set_session_model:

ACPServerSingleSession.set_session_model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.acp.__init__``

**File:** :file:`src/kimi_cli/ui/acp/__init__.py` (line 71)

**Parameters:**

    - ``self``
    - ``model_id`` (*str*)
    - ``session_id`` (*str*)
    - ``**kwargs`` (*Any*)

**Returns:** ``acp.SetSessionModelResponse | None``

**Calls:**

    - :ref:`_raise <func-_raise>`


.. _func-ACPSession.cancel:

ACPSession.cancel
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 243)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`set <func-set>`
    - :ref:`warning <func-warning>`


.. _func-ACPSession.cli:

ACPSession.cli
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 169)

**Description:**

    The Kimi Code CLI instance bound to this ACP session.

**Parameters:**

    - ``self``

**Returns:** ``KimiCLI``


.. _func-ACPSession.id:

ACPSession.id
^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 164)

**Description:**

    The ID of the ACP session.

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-ACPSession.prompt:

ACPSession.prompt
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 173)

**Parameters:**

    - ``self``
    - ``prompt`` (*list[ACPContentBlock]*)

**Returns:** ``acp.PromptResponse``

**Calls:**

    - :ref:`PromptResponse <func-PromptResponse>`
    - :ref:`_TurnState <func-_TurnState>`
    - :ref:`_handle_approval_request <func-_handle_approval_request>`
    - :ref:`_send_text <func-_send_text>`
    - :ref:`_send_thinking <func-_send_thinking>`
    - :ref:`_send_tool_call <func-_send_tool_call>`
    - :ref:`_send_tool_call_part <func-_send_tool_call_part>`
    - :ref:`_send_tool_result <func-_send_tool_result>`
    - :ref:`auth_required <func-auth_required>`
    - :ref:`exception <func-exception>`
    - :ref:`info <func-info>`
    - :ref:`internal_error <func-internal_error>`
    - :ref:`acp_blocks_to_content_parts <func-acp_blocks_to_content_parts>`
    - :ref:`reset <func-reset>`
    - :ref:`reset_current_kaos <func-reset_current_kaos>`
    - :ref:`run <func-run>`
    - :ref:`set <func-set>`
    - :ref:`set_current_kaos <func-set_current_kaos>`
    - :ref:`str <func-str>`
    - :ref:`warning <func-warning>`


.. _func-Approval.fetch_request:

Approval.fetch_request
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 103)

**Description:**

    Fetch an approval request from the queue. Intended to be called by the soul.

**Parameters:**

    - ``self``

**Returns:** ``Request``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`get <func-get>`
    - :ref:`resolve_request <func-resolve_request>`


.. _func-Approval.is_yolo:

Approval.is_yolo
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 48)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-Approval.request:

Approval.request
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 51)

**Description:**

    Request approval for the given action. Intended to be called by tools.

        Args:
            sender (str): The name of the sender.
            action (str): The action to request approval for.
  
    ...

**Parameters:**

    - ``self``
    - ``sender`` (*str*)
    - ``action`` (*str*)
    - ``description`` (*str*)
    - ``display`` (*list[DisplayBlock] | None*) = ``None``

**Returns:** ``bool``

**Calls:**

    - :ref:`Request <func-Request>`
    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`debug <func-debug>`
    - :ref:`get_current_tool_call_or_none <func-get_current_tool_call_or_none>`
    - :ref:`put_nowait <func-put_nowait>`
    - :ref:`str <func-str>`
    - :ref:`uuid4 <func-uuid4>`


.. _func-Approval.resolve_request:

Approval.resolve_request
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 119)

**Description:**

    Resolve an approval request with the given response. Intended to be called by the soul.

        Args:
            request\_id (str): The ID of the request to resolve.
            response (Response): 
    ...

**Parameters:**

    - ``self``
    - ``request_id`` (*str*)
    - ``response`` (*Response*)

**Returns:** ``None``

**Calls:**

    - :ref:`KeyError <func-KeyError>`
    - :ref:`add <func-add>`
    - :ref:`debug <func-debug>`
    - :ref:`pop <func-pop>`
    - :ref:`set_result <func-set_result>`


.. _func-Approval.set_yolo:

Approval.set_yolo
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 45)

**Parameters:**

    - ``self``
    - ``yolo`` (*bool*)

**Returns:** ``None``


.. _func-Approval.share:

Approval.share
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.approval``

**File:** :file:`src/kimi_cli/soul/approval.py` (line 41)

**Description:**

    Create a new approval queue that shares state (yolo + auto-approve).

**Parameters:**

    - ``self``

**Returns:** ``Approval``

**Calls:**

    - :ref:`Approval <func-Approval>`


.. _func-ApprovalRequest.resolve:

ApprovalRequest.resolve
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 182)

**Description:**

    Resolve the approval request with the given response.
        This will cause the \`wait()\` method to return the response.

**Parameters:**

    - ``self``
    - ``response`` (*ApprovalResponse.Kind*)

**Returns:** ``None``

**Calls:**

    - :ref:`_get_future <func-_get_future>`
    - :ref:`done <func-done>`
    - :ref:`set_result <func-set_result>`


.. _func-ApprovalRequest.resolved:

ApprovalRequest.resolved
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 192)

**Description:**

    Whether the request is resolved.

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`done <func-done>`


.. _func-ApprovalRequest.wait:

ApprovalRequest.wait
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 173)

**Description:**

    Wait for the request to be resolved or cancelled.

        Returns:
            ApprovalResponse.Kind: The response to the approval request.

**Parameters:**

    - ``self``

**Returns:** ``ApprovalResponse.Kind``

**Calls:**

    - :ref:`_get_future <func-_get_future>`


.. _func-AttachmentCache.load_bytes:

AttachmentCache.load_bytes
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 684)

**Parameters:**

    - ``self``
    - ``kind`` (*CachedAttachmentKind*)
    - ``attachment_id`` (*str*)

**Calls:**

    - :ref:`_dir_for <func-_dir_for>`
    - :ref:`exists <func-exists>`
    - :ref:`read_bytes <func-read_bytes>`
    - :ref:`warning <func-warning>`


.. _func-AttachmentCache.load_content_parts:

AttachmentCache.load_content_parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 700)

**Parameters:**

    - ``self``
    - ``kind`` (*CachedAttachmentKind*)
    - ``attachment_id`` (*str*)

**Returns:** ``list[ContentPart] | None``

**Calls:**

    - :ref:`_build_image_part <func-_build_image_part>`
    - :ref:`_guess_image_mime <func-_guess_image_mime>`
    - :ref:`wrap_media_part <func-wrap_media_part>`
    - :ref:`load_bytes <func-load_bytes>`
    - :ref:`str <func-str>`


.. _func-AttachmentCache.store_bytes:

AttachmentCache.store_bytes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 650)

**Parameters:**

    - ``self``
    - ``kind`` (*CachedAttachmentKind*)
    - ``suffix`` (*str*)
    - ``payload`` (*bytes*)

**Returns:** ``CachedAttachment | None``

**Calls:**

    - :ref:`CachedAttachment <func-CachedAttachment>`
    - :ref:`_ensure_dir <func-_ensure_dir>`
    - :ref:`_reserve_id <func-_reserve_id>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`hexdigest <func-hexdigest>`
    - :ref:`pop <func-pop>`
    - :ref:`sha256 <func-sha256>`
    - :ref:`warning <func-warning>`
    - :ref:`write_bytes <func-write_bytes>`


.. _func-AttachmentCache.store_image:

AttachmentCache.store_image
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 679)

**Parameters:**

    - ``self``
    - ``image`` (*Image.Image*)

**Returns:** ``CachedAttachment | None``

**Calls:**

    - :ref:`BytesIO <func-BytesIO>`
    - :ref:`getvalue <func-getvalue>`
    - :ref:`save <func-save>`
    - :ref:`store_bytes <func-store_bytes>`


.. _func-augment_provider_with_env_vars:

augment_provider_with_env_vars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.llm``

**File:** :file:`src/kimi_cli/llm.py` (line 53)

**Description:**

    Override provider/model settings from environment variables.

    Returns:
        Mapping of environment variables that were applied.

**Parameters:**

    - ``provider`` (*LLMProvider*)
    - ``model`` (*LLMModel*)

**Calls:**

    - :ref:`SecretStr <func-SecretStr>`
    - :ref:`cast <func-cast>`
    - :ref:`get_args <func-get_args>`
    - :ref:`getenv <func-getenv>`
    - :ref:`int <func-int>`
    - :ref:`lower <func-lower>`
    - :ref:`set <func-set>`
    - :ref:`split <func-split>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`create <func-create>` (from ``kimi_cli.app.KimiCLI``)


.. _func-AuthMiddleware.dispatch:

AuthMiddleware.dispatch
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 159)

**Parameters:**

    - ``self``
    - ``request`` (*Request*)
    - ``call_next``

**Calls:**

    - :ref:`JSONResponse <func-JSONResponse>`
    - :ref:`call_next <func-call_next>`
    - :ref:`get <func-get>`
    - :ref:`extract_token_from_request <func-extract_token_from_request>`
    - :ref:`get_client_ip <func-get_client_ip>`
    - :ref:`is_origin_allowed <func-is_origin_allowed>`
    - :ref:`is_private_ip <func-is_private_ip>`
    - :ref:`verify_token <func-verify_token>`
    - :ref:`startswith <func-startswith>`
    - :ref:`upper <func-upper>`



B
-

.. _func-BlockQuote.on_child_close:

BlockQuote.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 259)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`


.. _func-BroadcastQueue.publish:

BroadcastQueue.publish
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.broadcast``

**File:** :file:`src/kimi_cli/utils/broadcast.py` (line 22)

**Description:**

    Publish an item to all subscription queues.

**Parameters:**

    - ``self``
    - ``item`` (*T*)

**Returns:** ``None``

**Calls:**

    - :ref:`gather <func-gather>`
    - :ref:`put <func-put>`


.. _func-BroadcastQueue.publish_nowait:

BroadcastQueue.publish_nowait
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.broadcast``

**File:** :file:`src/kimi_cli/utils/broadcast.py` (line 26)

**Description:**

    Publish an item to all subscription queues without waiting.

**Parameters:**

    - ``self``
    - ``item`` (*T*)

**Returns:** ``None``

**Calls:**

    - :ref:`put_nowait <func-put_nowait>`


.. _func-BroadcastQueue.shutdown:

BroadcastQueue.shutdown
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.broadcast``

**File:** :file:`src/kimi_cli/utils/broadcast.py` (line 31)

**Description:**

    Close all subscription queues.

**Parameters:**

    - ``self``
    - ``immediate`` (*bool*) = ``False``

**Returns:** ``None``

**Calls:**

    - :ref:`clear <func-clear>`
    - :ref:`shutdown <func-shutdown>`


.. _func-BroadcastQueue.subscribe:

BroadcastQueue.subscribe
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.broadcast``

**File:** :file:`src/kimi_cli/utils/broadcast.py` (line 12)

**Description:**

    Create a new subscription queue.

**Parameters:**

    - ``self``

**Returns:** ``Queue[T]``

**Calls:**

    - :ref:`Queue <func-Queue>`
    - :ref:`add <func-add>`


.. _func-BroadcastQueue.unsubscribe:

BroadcastQueue.unsubscribe
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.broadcast``

**File:** :file:`src/kimi_cli/utils/broadcast.py` (line 18)

**Description:**

    Remove a subscription queue.

**Parameters:**

    - ``self``
    - ``queue`` (*Queue[T]*)

**Returns:** ``None``

**Calls:**

    - :ref:`discard <func-discard>`


.. _func-build_diff_blocks:

build_diff_blocks
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.diff``

**File:** :file:`src/kimi_cli/utils/diff.py` (line 8)

**Description:**

    Build diff display blocks grouped with small context windows.

**Parameters:**

    - ``path`` (*str*)
    - ``old_text`` (*str*)
    - ``new_text`` (*str*)

**Returns:** ``list[DiffDisplayBlock]``

**Calls:**

    - :ref:`DiffDisplayBlock <func-DiffDisplayBlock>`
    - :ref:`SequenceMatcher <func-SequenceMatcher>`
    - :ref:`append <func-append>`
    - :ref:`get_grouped_opcodes <func-get_grouped_opcodes>`
    - :ref:`join <func-join>`
    - :ref:`splitlines <func-splitlines>`

**Called by:**

    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.replace.StrReplaceFile``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.write.WriteFile``)



C
-

.. _func-changelog:

changelog
^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 263)

**Description:**

    Show release notes

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`items <func-items>`
    - :ref:`lower <func-lower>`
    - :ref:`pager <func-pager>`
    - :ref:`print <func-print>`
    - :ref:`startswith <func-startswith>`


.. _func-check_message:

check_message
^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.message``

**File:** :file:`src/kimi_cli/soul/message.py` (line 90)

**Description:**

    Check the message content, return the missing model capabilities.

**Parameters:**

    - ``message`` (*Message*)
    - ``model_capabilities`` (*set[ModelCapability]*)

**Returns:** ``set[ModelCapability]``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - :ref:`_grow_context <func-_grow_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_turn <func-_turn>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)


.. _func-clear:

clear
^^^^^

**Module:** ``kimi_cli.soul.slash``

**File:** :file:`src/kimi_cli/soul/slash.py` (line 31)

**Description:**

    Clear the context

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`command <func-command>`
    - :ref:`info <func-info>`
    - :ref:`clear <func-clear>`
    - :ref:`wire_send <func-wire_send>`

**Called by:**

    - :ref:`compact_context <func-compact_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.slash``)


.. _func-clear:

clear
^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 305)

**Description:**

    Clear the context

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Reload <func-Reload>`
    - :ref:`command <func-command>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`run_soul_command <func-run_soul_command>`

**Called by:**

    - :ref:`mcp_reset_auth <func-mcp_reset_auth>` (from ``kimi_cli.cli.mcp``)
    - :ref:`_iter_top_level_statements <func-_iter_top_level_statements>` (from ``kimi_cli.skill.flow.d2``)
    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`revert_to <func-revert_to>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`feed <func-feed>` (from ``kimi_cli.ui.print.visualize.FinalOnlyJsonPrinter``)
    - :ref:`flush <func-flush>` (from ``kimi_cli.ui.print.visualize.FinalOnlyJsonPrinter``)
    - :ref:`feed <func-feed>` (from ``kimi_cli.ui.print.visualize.FinalOnlyTextPrinter``)
    - :ref:`flush <func-flush>` (from ``kimi_cli.ui.print.visualize.FinalOnlyTextPrinter``)
    - :ref:`flush <func-flush>` (from ``kimi_cli.ui.print.visualize.JsonPrinter``)
    - :ref:`_resume_sync <func-_resume_sync>` (from ``kimi_cli.ui.shell.keyboard.KeyboardListener``)
    - :ref:`stop <func-stop>` (from ``kimi_cli.ui.shell.keyboard.KeyboardListener``)
    - :ref:`_listen_for_keyboard_unix <func-_listen_for_keyboard_unix>` (from ``kimi_cli.ui.shell.keyboard``)
    - :ref:`_listen_for_keyboard_windows <func-_listen_for_keyboard_windows>` (from ``kimi_cli.ui.shell.keyboard``)
    - :ref:`login <func-login>` (from ``kimi_cli.ui.shell.oauth``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.ui.shell.oauth``)
    - :ref:`shutdown <func-shutdown>` (from ``kimi_cli.utils.broadcast.BroadcastQueue``)
    - :ref:`_close_all_websockets <func-_close_all_websockets>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`_read_loop <func-_read_loop>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`end_replay <func-end_replay>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`start <func-start>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`stop_worker <func-stop_worker>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`_shutdown <func-_shutdown>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-CodeBlock.create:

CodeBlock.create
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 226)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``CodeBlock``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`partition <func-partition>`


.. _func-compact:

compact
^^^^^^^

**Module:** ``kimi_cli.soul.slash``

**File:** :file:`src/kimi_cli/soul/slash.py` (line 39)

**Description:**

    Compact the context

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`compact_context <func-compact_context>`
    - :ref:`info <func-info>`
    - :ref:`wire_send <func-wire_send>`

**Called by:**

    - :ref:`compact_context <func-compact_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)


.. _func-Compaction.compact:

Compaction.compact
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.compaction``

**File:** :file:`src/kimi_cli/soul/compaction.py` (line 18)

**Description:**

    Compact a sequence of messages into a new sequence of messages.

        Args:
            messages (Sequence[Message]): The messages to compact.
            llm (LLM): The LLM to use for compaction.

    ...

**Parameters:**

    - ``self``
    - ``messages`` (*Sequence[Message]*)
    - ``llm`` (*LLM*)

**Returns:** ``Sequence[Message]``


.. _func-Config.validate_model:

Config.validate_model
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 155)

**Parameters:**

    - ``self``

**Returns:** ``Self``

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`model_validator <func-model_validator>`
    - :ref:`values <func-values>`


.. _func-Context.append_message:

Context.append_message
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 161)

**Parameters:**

    - ``self``
    - ``message`` (*Message | Sequence[Message]*)

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`open <func-open>`
    - :ref:`write <func-write>`


.. _func-Context.checkpoint:

Context.checkpoint
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 67)

**Parameters:**

    - ``self``
    - ``add_user_message`` (*bool*)

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`append_message <func-append_message>`
    - :ref:`debug <func-debug>`
    - :ref:`dumps <func-dumps>`
    - :ref:`system <func-system>`
    - :ref:`open <func-open>`
    - :ref:`write <func-write>`


.. _func-Context.clear:

Context.clear
^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 133)

**Description:**

    Clear the context history.
        This is almost equivalent to revert\_to(0), but without relying on the assumption
        that the first checkpoint exists.
        File backend will be rotated.

   
    ...

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`clear <func-clear>`
    - :ref:`debug <func-debug>`
    - :ref:`error <func-error>`
    - :ref:`next_available_rotation <func-next_available_rotation>`
    - :ref:`replace <func-replace>`
    - :ref:`touch <func-touch>`


.. _func-Context.file_backend:

Context.file_backend
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 64)

**Parameters:**

    - ``self``

**Returns:** ``Path``


.. _func-Context.history:

Context.history
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 52)

**Parameters:**

    - ``self``

**Returns:** ``Sequence[Message]``


.. _func-Context.n_checkpoints:

Context.n_checkpoints
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 60)

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-Context.restore:

Context.restore
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 23)

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`append <func-append>`
    - :ref:`debug <func-debug>`
    - :ref:`error <func-error>`
    - :ref:`exists <func-exists>`
    - :ref:`loads <func-loads>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`open <func-open>`
    - :ref:`stat <func-stat>`
    - :ref:`strip <func-strip>`


.. _func-Context.revert_to:

Context.revert_to
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 79)

**Description:**

    Revert the context to the specified checkpoint.
        After this, the specified checkpoint and all subsequent content will be
        removed from the context. File backend will be rotated.

       
    ...

**Parameters:**

    - ``self``
    - ``checkpoint_id`` (*int*)

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`ValueError <func-ValueError>`
    - :ref:`append <func-append>`
    - :ref:`clear <func-clear>`
    - :ref:`debug <func-debug>`
    - :ref:`error <func-error>`
    - :ref:`next_available_rotation <func-next_available_rotation>`
    - :ref:`loads <func-loads>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`open <func-open>`
    - :ref:`replace <func-replace>`
    - :ref:`strip <func-strip>`
    - :ref:`write <func-write>`


.. _func-Context.token_count:

Context.token_count
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 56)

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-Context.update_token_count:

Context.update_token_count
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.context``

**File:** :file:`src/kimi_cli/soul/context.py` (line 170)

**Parameters:**

    - ``self``
    - ``token_count`` (*int*)

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`dumps <func-dumps>`
    - :ref:`open <func-open>`
    - :ref:`write <func-write>`


.. _func-convert_mcp_tool_result:

convert_mcp_tool_result
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 451)

**Description:**

    Convert MCP tool result to kosong tool return value.

    Raises:
        ValueError: If any content part has unsupported type or mime type.

**Parameters:**

    - ``result`` (*CallToolResult*)

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`ToolError <func-ToolError>`
    - :ref:`ToolOk <func-ToolOk>`
    - :ref:`append <func-append>`
    - :ref:`convert_mcp_content <func-convert_mcp_content>`

**Called by:**

    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.soul.toolset.MCPTool``)


.. _func-create_app:

create_app
^^^^^^^^^^

**Module:** ``kimi_cli.web.app``

**File:** :file:`src/kimi_cli/web/app.py` (line 215)

**Description:**

    Create the FastAPI application for Kimi CLI web UI.

**Parameters:**

    - ``session_token`` (*str | None*) = ``None``
    - ``allowed_origins`` (*list[str] | None*) = ``None``
    - ``enforce_origin`` (*bool | None*) = ``None``
    - ``restrict_sensitive_apis`` (*bool | None*) = ``None``
    - ``max_public_path_depth`` (*int | None*) = ``None``
    - ``lan_only`` (*bool | None*) = ``None``

**Returns:** ``FastAPI``

**Calls:**

    - :ref:`FastAPI <func-FastAPI>`
    - :ref:`KimiCLIRunner <func-KimiCLIRunner>`
    - :ref:`StaticFiles <func-StaticFiles>`
    - :ref:`add_middleware <func-add_middleware>`
    - :ref:`cast <func-cast>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`get_scalar_api_reference <func-get_scalar_api_reference>`
    - :ref:`getcwd <func-getcwd>`
    - :ref:`include_router <func-include_router>`
    - :ref:`int <func-int>`
    - :ref:`isdigit <func-isdigit>`
    - :ref:`_load_env_flag <func-_load_env_flag>`
    - :ref:`normalize_allowed_origins <func-normalize_allowed_origins>`
    - :ref:`mount <func-mount>`
    - :ref:`start <func-start>`
    - :ref:`stop <func-stop>`


.. _func-create_llm:

create_llm
^^^^^^^^^^

**Module:** ``kimi_cli.llm``

**File:** :file:`src/kimi_cli/llm.py` (line 183)

**Description:**

    Create Llm.
    
    Args:
    provider: Description.
    model: Description.
    thinking: Description.
    session\_id: Description.
    oauth: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider`` (*LLMProvider*)
    - ``model`` (*LLMModel*)
    - ``thinking`` (*bool | None*) = ``None``
    - ``session_id`` (*str | None*) = ``None``
    - ``oauth`` (*OAuthManager | None*) = ``None``

**Returns:** ``LLM | None``

**Calls:**

    - :ref:`Anthropic <func-Anthropic>`
    - :ref:`ChaosChatProvider <func-ChaosChatProvider>`
    - :ref:`ChaosConfig <func-ChaosConfig>`
    - :ref:`GoogleGenAI <func-GoogleGenAI>`
    - :ref:`Kimi <func-Kimi>`
    - :ref:`LLM <func-LLM>`
    - :ref:`OpenAILegacy <func-OpenAILegacy>`
    - :ref:`OpenAIResponses <func-OpenAIResponses>`
    - :ref:`ScriptedEchoChatProvider <func-ScriptedEchoChatProvider>`
    - :ref:`float <func-float>`
    - :ref:`get_secret_value <func-get_secret_value>`
    - :ref:`getenv <func-getenv>`
    - :ref:`int <func-int>`
    - :ref:`_kimi_default_headers <func-_kimi_default_headers>`
    - :ref:`_load_scripted_echo_scripts <func-_load_scripted_echo_scripts>`
    - :ref:`derive_model_capabilities <func-derive_model_capabilities>`
    - :ref:`lower <func-lower>`
    - :ref:`resolve_api_key <func-resolve_api_key>`
    - :ref:`strip <func-strip>`
    - :ref:`update <func-update>`
    - :ref:`with_generation_kwargs <func-with_generation_kwargs>`
    - :ref:`with_thinking <func-with_thinking>`

**Called by:**

    - :ref:`set_session_model <func-set_session_model>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`create <func-create>` (from ``kimi_cli.app.KimiCLI``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)


.. _func-create_session:

create_session
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 535)

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
    - :ref:`invalidate_work_dirs_cache <func-invalidate_work_dirs_cache>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`now <func-now>`
    - :ref:`post <func-post>`
    - :ref:`resolve <func-resolve>`
    - :ref:`stat <func-stat>`
    - :ref:`str <func-str>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`


.. _func-CustomPromptSession.prompt:

CustomPromptSession.prompt
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 904)

**Parameters:**

    - ``self``

**Returns:** ``UserInput``

**Calls:**

    - :ref:`TextPart <func-TextPart>`
    - :ref:`UserInput <func-UserInput>`
    - :ref:`_append_history_entry <func-_append_history_entry>`
    - :ref:`append <func-append>`
    - :ref:`extend <func-extend>`
    - :ref:`group <func-group>`
    - :ref:`_parse_attachment_kind <func-_parse_attachment_kind>`
    - :ref:`_sanitize_surrogates <func-_sanitize_surrogates>`
    - :ref:`load_content_parts <func-load_content_parts>`
    - :ref:`patch_stdout <func-patch_stdout>`
    - :ref:`prompt_async <func-prompt_async>`
    - :ref:`replace <func-replace>`
    - :ref:`search <func-search>`
    - :ref:`span <func-span>`
    - :ref:`str <func-str>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`



D
-

.. _func-debug:

debug
^^^^^

**Module:** ``kimi_cli.ui.shell.debug``

**File:** :file:`src/kimi_cli/ui/shell/debug.py` (line 158)

**Description:**

    Debug the context

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Group <func-Group>`
    - :ref:`Panel <func-Panel>`
    - :ref:`Rule <func-Rule>`
    - :ref:`Text <func-Text>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_format_message <func-_format_message>`
    - :ref:`len <func-len>`
    - :ref:`pager <func-pager>`
    - :ref:`print <func-print>`

**Called by:**

    - :ref:`_handle_approval_request <func-_handle_approval_request>` (from ``kimi_cli.acp.session.ACPSession``)
    - :ref:`_send_tool_call <func-_send_tool_call>` (from ``kimi_cli.acp.session.ACPSession``)
    - :ref:`_send_tool_call_part <func-_send_tool_call_part>` (from ``kimi_cli.acp.session.ACPSession``)
    - :ref:`_send_tool_result <func-_send_tool_result>` (from ``kimi_cli.acp.session.ACPSession``)
    - :ref:`load_config <func-load_config>` (from ``kimi_cli.config``)
    - :ref:`save_config <func-save_config>` (from ``kimi_cli.config``)
    - :ref:`load_metadata <func-load_metadata>` (from ``kimi_cli.metadata``)
    - :ref:`save_metadata <func-save_metadata>` (from ``kimi_cli.metadata``)
    - :ref:`continue_ <func-continue_>` (from ``kimi_cli.session.Session``)
    - :ref:`create <func-create>` (from ``kimi_cli.session.Session``)
    - :ref:`find <func-find>` (from ``kimi_cli.session.Session``)
    - :ref:`list <func-list>` (from ``kimi_cli.session.Session``)
    - :ref:`run_soul <func-run_soul>` (from ``kimi_cli.soul.__init__``)
    - :ref:`_load_system_prompt <func-_load_system_prompt>` (from ``kimi_cli.soul.agent``)
    - :ref:`load_agent <func-load_agent>` (from ``kimi_cli.soul.agent``)
    - :ref:`fetch_request <func-fetch_request>` (from ``kimi_cli.soul.approval.Approval``)
    - :ref:`request <func-request>` (from ``kimi_cli.soul.approval.Approval``)
    - :ref:`resolve_request <func-resolve_request>` (from ``kimi_cli.soul.approval.Approval``)
    - :ref:`compact <func-compact>` (from ``kimi_cli.soul.compaction.SimpleCompaction``)
    - :ref:`append_message <func-append_message>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`checkpoint <func-checkpoint>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`restore <func-restore>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`revert_to <func-revert_to>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`update_token_count <func-update_token_count>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`_agent_loop <func-_agent_loop>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_grow_context <func-_grow_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_step <func-_step>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_turn <func-_turn>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_load_tool <func-_load_tool>` (from ``kimi_cli.soul.toolset.KimiToolset``)
    - :ref:`load_mcp_tools <func-load_mcp_tools>` (from ``kimi_cli.soul.toolset.KimiToolset``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.grep_local.Grep``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.print.__init__.Print``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_run_slash_command <func-_run_slash_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run_soul_command <func-run_soul_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_try_paste_image <func-_try_paste_image>` (from ``kimi_cli.ui.shell.prompt.CustomPromptSession``)
    - :ref:`_do_update <func-_do_update>` (from ``kimi_cli.ui.shell.update``)
    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_broadcast <func-_broadcast>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`add_websocket_and_begin_replay <func-add_websocket_and_begin_replay>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`remove_websocket <func-remove_websocket>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`shutdown <func-shutdown>` (from ``kimi_cli.wire.__init__.Wire``)
    - :ref:`send <func-send>` (from ``kimi_cli.wire.__init__.WireSoulSide``)
    - :ref:`receive <func-receive>` (from ``kimi_cli.wire.__init__.WireUISide``)
    - :ref:`_write_loop <func-_write_loop>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-delete_session:

delete_session
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 763)

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
    - :ref:`str <func-str>`


.. _func-delete_tokens:

delete_tokens
^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 434)

**Description:**

    Delete Tokens.
    
    Args:
    ref: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)

**Returns:** ``None``

**Calls:**

    - :ref:`_delete_from_file <func-_delete_from_file>`
    - :ref:`_delete_from_keyring <func-_delete_from_keyring>`

**Called by:**

    - :ref:`_refresh_tokens <func-_refresh_tokens>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`logout_kimi_code <func-logout_kimi_code>` (from ``kimi_cli.auth.oauth``)


.. _func-DenwaRenji.fetch_pending_dmail:

DenwaRenji.fetch_pending_dmail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.denwarenji``

**File:** :file:`src/kimi_cli/soul/denwarenji.py` (line 32)

**Description:**

    Fetch a pending D-Mail. Intended to be called by the soul.

**Parameters:**

    - ``self``

**Returns:** ``DMail | None``


.. _func-DenwaRenji.send_dmail:

DenwaRenji.send_dmail
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.denwarenji``

**File:** :file:`src/kimi_cli/soul/denwarenji.py` (line 18)

**Description:**

    Send a D-Mail. Intended to be called by the SendDMail tool.

**Parameters:**

    - ``self``
    - ``dmail`` (*DMail*)

**Calls:**

    - :ref:`DenwaRenjiError <func-DenwaRenjiError>`


.. _func-DenwaRenji.set_n_checkpoints:

DenwaRenji.set_n_checkpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.denwarenji``

**File:** :file:`src/kimi_cli/soul/denwarenji.py` (line 28)

**Description:**

    Set the number of checkpoints. Intended to be called by the soul.

**Parameters:**

    - ``self``
    - ``n_checkpoints`` (*int*)


.. _func-derive_model_capabilities:

derive_model_capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.llm``

**File:** :file:`src/kimi_cli/llm.py` (line 15)

**Description:**

    Derive Model Capabilities.
    
    Args:
    model: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``model`` (*LLMModel*)

**Returns:** ``set[ModelCapability]``

**Calls:**

    - :ref:`lower <func-lower>`
    - :ref:`set <func-set>`
    - :ref:`update <func-update>`

**Called by:**

    - :ref:`_expand_llm_models <func-_expand_llm_models>` (from ``kimi_cli.acp.server``)
    - :ref:`create_llm <func-create_llm>` (from ``kimi_cli.llm``)
    - :ref:`model <func-model>` (from ``kimi_cli.ui.shell.slash``)
    - :ref:`_build_global_config <func-_build_global_config>` (from ``kimi_cli.web.api.config``)


.. _func-deserialize_wire_message:

deserialize_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.serde``

**File:** :file:`src/kimi_cli/wire/serde.py` (line 6)

**Description:**

    Convert a jsonifiable dict into a \`WireMessage\`.

    Raises:
        ValueError: If the message type is unknown or the payload is invalid.

**Parameters:**

    - ``data``

**Returns:** ``WireMessage``

**Calls:**

    - :ref:`model_validate <func-model_validate>`
    - :ref:`to_wire_message <func-to_wire_message>`

**Called by:**

    - :ref:`_read_wire_lines <func-_read_wire_lines>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_read_loop <func-_read_loop>` (from ``kimi_cli.web.runner.process.SessionProcess``)


.. _func-detect_file_type:

detect_file_type
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.file.utils``

**File:** :file:`src/kimi_cli/tools/file/utils.py` (line 263)

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

    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.read.ReadFile``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.read_media.ReadMediaFile``)


.. _func-discover_skills:

discover_skills
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 164)

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

    - :ref:`discover_skills_from_roots <func-discover_skills_from_roots>` (from ``kimi_cli.skill.__init__``)


.. _func-discover_skills_from_roots:

discover_skills_from_roots
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 142)

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

    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)


.. _func-display_block_to_acp_content:

display_block_to_acp_content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.convert``

**File:** :file:`src/kimi_cli/acp/convert.py` (line 41)

**Description:**

    Display Block To Acp Content.
    
    Args:
    block: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``block`` (*DisplayBlock*)

**Returns:** ``acp.schema.FileEditToolCallContent | None``

**Calls:**

    - :ref:`FileEditToolCallContent <func-FileEditToolCallContent>`
    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - :ref:`tool_result_to_acp_content <func-tool_result_to_acp_content>` (from ``kimi_cli.acp.convert``)
    - :ref:`_handle_approval_request <func-_handle_approval_request>` (from ``kimi_cli.acp.session.ACPSession``)


.. _func-do_update:

do_update
^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.update``

**File:** :file:`src/kimi_cli/ui/shell/update.py` (line 118)

**Description:**

    Do Update.
    
    Args:
    print: Description.
    check\_only: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``print`` (*bool*) = ``True``
    - ``check_only`` (*bool*) = ``False``

**Returns:** ``UpdateResult``

**Calls:**

    - :ref:`_do_update <func-_do_update>`

**Called by:**

    - :ref:`_auto_update <func-_auto_update>` (from ``kimi_cli.ui.shell.__init__.Shell``)



E
-

.. _func-enable_character_wrap:

enable_character_wrap
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.__init__``

**File:** :file:`src/kimi_cli/utils/rich/__init__.py` (line 26)

**Description:**

    Switch Rich's wrapping logic to break on every character.

    Rich's default behavior tries to preserve whole words; we override the
    internal regex so markdown rendering can fold text at any colu
    ...

**Returns:** ``None``


.. _func-enable_logging:

enable_logging
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 31)

**Description:**

    Enable Logging.
    
    Args:
    debug: Description.
    redirect\_stderr: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``debug`` (*bool*) = ``False``
    - ``redirect_stderr`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`enable <func-enable>`
    - :ref:`get_share_dir <func-get_share_dir>`
    - :ref:`redirect_stderr_to_logger <func-redirect_stderr_to_logger>`
    - :ref:`remove <func-remove>`

**Called by:**

    - :ref:`acp_main <func-acp_main>` (from ``kimi_cli.acp.__init__``)
    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`web_worker <func-web_worker>` (from ``kimi_cli.cli.__init__``)
    - :ref:`main <func-main>` (from ``kimi_cli.web.runner.worker``)


.. _func-ensure_new_line:

ensure_new_line
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.term``

**File:** :file:`src/kimi_cli/utils/term.py` (line 166)

**Description:**

    Ensure the next prompt starts at column 0 regardless of prior command output.

**Returns:** ``None``

**Calls:**

    - :ref:`isatty <func-isatty>`
    - :ref:`_cursor_column_unix <func-_cursor_column_unix>`
    - :ref:`_cursor_column_windows <func-_cursor_column_windows>`
    - :ref:`_write_newline <func-_write_newline>`

**Called by:**

    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)


.. _func-ensure_tty_sane:

ensure_tty_sane
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.term``

**File:** :file:`src/kimi_cli/utils/term.py` (line 68)

**Description:**

    Restore basic tty settings so Ctrl-C works after raw-mode operations.

**Returns:** ``None``

**Calls:**

    - :ref:`fileno <func-fileno>`
    - :ref:`isatty <func-isatty>`
    - :ref:`suppress <func-suppress>`
    - :ref:`tcgetattr <func-tcgetattr>`
    - :ref:`tcsetattr <func-tcsetattr>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)


.. _func-Environment.detect:

Environment.detect
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.environment``

**File:** :file:`src/kimi_cli/utils/environment.py` (line 19)

**Returns:** ``Environment``

**Calls:**

    - :ref:`Environment <func-Environment>`
    - :ref:`KaosPath <func-KaosPath>`
    - :ref:`is_file <func-is_file>`
    - :ref:`machine <func-machine>`
    - :ref:`system <func-system>`
    - :ref:`version <func-version>`


.. _func-exit:

exit
^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 44)

**Description:**

    Exit the application

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`command <func-command>`

**Called by:**

    - :ref:`main <func-main>` (from ``kimi_cli.web.runner.worker``)


.. _func-extract_first_turn_from_wire:

extract_first_turn_from_wire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 828)

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

    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)


.. _func-extract_key_argument:

extract_key_argument
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.__init__``

**File:** :file:`src/kimi_cli/tools/__init__.py` (line 43)

**Description:**

    Extract Key Argument.
    
    Args:
    json\_content: Description.
    tool\_name: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``json_content`` (*str | streamingjson.Lexer*)
    - ``tool_name`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`cast <func-cast>`
    - :ref:`complete_json <func-complete_json>`
    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`join <func-join>`
    - :ref:`_normalize_path <func-_normalize_path>`
    - :ref:`shorten_middle <func-shorten_middle>`
    - :ref:`loads <func-loads>`
    - :ref:`str <func-str>`

**Called by:**

    - :ref:`get_title <func-get_title>` (from ``kimi_cli.acp.session._ToolCallState``)
    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.ui.shell.visualize._ToolCallBlock``)
    - :ref:`_compose <func-_compose>` (from ``kimi_cli.ui.shell.visualize._ToolCallBlock``)
    - :ref:`append_args_part <func-append_args_part>` (from ``kimi_cli.ui.shell.visualize._ToolCallBlock``)


.. _func-extract_token_from_request:

extract_token_from_request
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 125)

**Description:**

    Get auth token from Authorization header or query (GET-only).

**Parameters:**

    - ``request`` (*Request*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`parse_bearer_token <func-parse_bearer_token>`
    - :ref:`upper <func-upper>`

**Called by:**

    - :ref:`dispatch <func-dispatch>` (from ``kimi_cli.web.auth.AuthMiddleware``)



F
-

.. _func-feedback:

feedback
^^^^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 294)

**Description:**

    Submit feedback to make Kimi Code CLI better

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`open <func-open>`
    - :ref:`print <func-print>`


.. _func-FetchURL.fetch_with_http_get:

FetchURL.fetch_with_http_get
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.web.fetch``

**File:** :file:`src/kimi_cli/tools/web/fetch.py` (line 45)

**Parameters:**

    - ``params`` (*Params*)

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`ToolResultBuilder <func-ToolResultBuilder>`
    - :ref:`error <func-error>`
    - :ref:`extract <func-extract>`
    - :ref:`get <func-get>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`lower <func-lower>`
    - :ref:`ok <func-ok>`
    - :ref:`startswith <func-startswith>`
    - :ref:`str <func-str>`
    - :ref:`text <func-text>`
    - :ref:`write <func-write>`


.. _func-FinalOnlyJsonPrinter.feed:

FinalOnlyJsonPrinter.feed
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 166)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`clear <func-clear>`
    - :ref:`_merge_content <func-_merge_content>`


.. _func-FinalOnlyJsonPrinter.flush:

FinalOnlyJsonPrinter.flush
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 175)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`clear <func-clear>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`print <func-print>`


.. _func-FinalOnlyTextPrinter.feed:

FinalOnlyTextPrinter.feed
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 141)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`clear <func-clear>`
    - :ref:`_merge_content <func-_merge_content>`


.. _func-FinalOnlyTextPrinter.flush:

FinalOnlyTextPrinter.flush
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 150)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`clear <func-clear>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`print <func-print>`


.. _func-find_available_port:

find_available_port
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.app``

**File:** :file:`src/kimi_cli/web/app.py` (line 98)

**Description:**

    Find an available port starting from start\_port.

    Args:
        host: Host address to bind to
        start\_port: Starting port number (1-65535)
        max\_attempts: Maximum number of ports to tr
    ...

**Parameters:**

    - ``host`` (*str*)
    - ``start_port`` (*int*)
    - ``max_attempts`` (*int*) = ``MAX_PORT_ATTEMPTS``

**Returns:** ``int``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`ValueError <func-ValueError>`
    - :ref:`bind <func-bind>`
    - :ref:`_get_address_family <func-_get_address_family>`
    - :ref:`range <func-range>`
    - :ref:`setsockopt <func-setsockopt>`
    - :ref:`socket <func-socket>`

**Called by:**

    - :ref:`run_web_server <func-run_web_server>` (from ``kimi_cli.web.app``)


.. _func-find_first_existing_dir:

find_first_existing_dir
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 17)

**Description:**

    Return the first existing directory from candidates.

**Parameters:**

    - ``candidates`` (*Iterable[KaosPath]*)

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`is_dir <func-is_dir>`

**Called by:**

    - :ref:`find_project_skills_dir <func-find_project_skills_dir>` (from ``kimi_cli.skill.__init__``)
    - :ref:`find_user_skills_dir <func-find_user_skills_dir>` (from ``kimi_cli.skill.__init__``)


.. _func-find_project_skills_dir:

find_project_skills_dir
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 43)

**Description:**

    Return the first existing project-level skills directory.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`find_first_existing_dir <func-find_first_existing_dir>`
    - :ref:`get_project_skills_dir_candidates <func-get_project_skills_dir_candidates>`

**Called by:**

    - :ref:`resolve_skills_roots <func-resolve_skills_roots>` (from ``kimi_cli.skill.__init__``)


.. _func-find_user_skills_dir:

find_user_skills_dir
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 61)

**Description:**

    Return the first existing user-level skills directory.

**Returns:** ``KaosPath | None``

**Calls:**

    - :ref:`find_first_existing_dir <func-find_first_existing_dir>`
    - :ref:`get_user_skills_dir_candidates <func-get_user_skills_dir_candidates>`

**Called by:**

    - :ref:`resolve_skills_roots <func-resolve_skills_roots>` (from ``kimi_cli.skill.__init__``)


.. _func-flatten_union:

flatten_union
^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.typing``

**File:** :file:`src/kimi_cli/utils/typing.py` (line 4)

**Description:**

    If \`tp\` is a \`UnionType\`, return its flattened arguments as a tuple.
    Otherwise, return a tuple with \`tp\` as the only element.

**Parameters:**

    - ``tp`` (*Any*)

**Calls:**

    - :ref:`extend <func-extend>`
    - :ref:`get_args <func-get_args>`
    - :ref:`get_origin <func-get_origin>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`flatten_union <func-flatten_union>`
    - :ref:`tuple <func-tuple>`

**Called by:**

    - :ref:`flatten_union <func-flatten_union>` (from ``kimi_cli.utils.typing``)


.. _func-FlowRunner.ralph_loop:

FlowRunner.ralph_loop
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 555)

**Parameters:**

    - ``user_message`` (*Message*)
    - ``max_ralph_iterations`` (*int*)

**Returns:** ``FlowRunner``

**Calls:**

    - :ref:`Flow <func-Flow>`
    - :ref:`FlowEdge <func-FlowEdge>`
    - :ref:`FlowNode <func-FlowNode>`
    - :ref:`FlowRunner <func-FlowRunner>`
    - :ref:`Message <func-Message>`
    - :ref:`append <func-append>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`list <func-list>`
    - :ref:`strip <func-strip>`


.. _func-FlowRunner.run:

FlowRunner.run
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 594)

**Parameters:**

    - ``self``
    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`MaxStepsReached <func-MaxStepsReached>`
    - :ref:`_execute_flow_node <func-_execute_flow_node>`
    - :ref:`error <func-error>`
    - :ref:`get <func-get>`
    - :ref:`info <func-info>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`


.. _func-fork_session:

fork_session
^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 993)

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
    - :ref:`finditer <func-finditer>`
    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`group <func-group>`
    - :ref:`guess_type <func-guess_type>`
    - :ref:`is_dir <func-is_dir>`
    - :ref:`is_file <func-is_file>`
    - :ref:`get_editable_session <func-get_editable_session>`
    - :ref:`invalidate_work_dirs_cache <func-invalidate_work_dirs_cache>`
    - :ref:`truncate_context_at_turn <func-truncate_context_at_turn>`
    - :ref:`truncate_wire_at_turn <func-truncate_wire_at_turn>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`load_session_metadata <func-load_session_metadata>`
    - :ref:`save_session_metadata <func-save_session_metadata>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`now <func-now>`
    - :ref:`open <func-open>`
    - :ref:`post <func-post>`
    - :ref:`set <func-set>`
    - :ref:`startswith <func-startswith>`
    - :ref:`stat <func-stat>`
    - :ref:`str <func-str>`
    - :ref:`write <func-write>`
    - :ref:`write_text <func-write_text>`


.. _func-format_duration:

format_duration
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.datetime``

**File:** :file:`src/kimi_cli/utils/datetime.py` (line 3)

**Description:**

    Format a duration in seconds using short units.

**Parameters:**

    - ``seconds`` (*int*)

**Returns:** ``str``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`divmod <func-divmod>`
    - :ref:`join <func-join>`
    - :ref:`timedelta <func-timedelta>`

**Called by:**

    - :ref:`_format_reset_time <func-_format_reset_time>` (from ``kimi_cli.ui.shell.usage``)
    - :ref:`_reset_hint <func-_reset_hint>` (from ``kimi_cli.ui.shell.usage``)


.. _func-format_relative_time:

format_relative_time
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.datetime``

**File:** :file:`src/kimi_cli/utils/datetime.py` (line 20)

**Description:**

    Format a timestamp as a relative time string.

**Parameters:**

    - ``timestamp`` (*float*)

**Returns:** ``str``

**Calls:**

    - :ref:`fromtimestamp <func-fromtimestamp>`
    - :ref:`int <func-int>`
    - :ref:`now <func-now>`
    - :ref:`strftime <func-strftime>`
    - :ref:`timedelta <func-timedelta>`
    - :ref:`total_seconds <func-total_seconds>`

**Called by:**

    - :ref:`list_sessions <func-list_sessions>` (from ``kimi_cli.ui.shell.slash``)


.. _func-format_release_notes:

format_release_notes
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.changelog``

**File:** :file:`src/kimi_cli/utils/changelog.py` (line 5)

**Description:**

    Format Release Notes.
    
    Args:
    changelog: Description.
    include\_lib\_changes: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``changelog``
    - ``include_lib_changes`` (*bool*)

**Returns:** ``str``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`items <func-items>`
    - :ref:`join <func-join>`
    - :ref:`lower <func-lower>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip <func-strip>`


.. _func-format_unified_diff:

format_unified_diff
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.diff``

**File:** :file:`src/kimi_cli/utils/diff.py` (line 34)

**Description:**

    Format a unified diff between old\_text and new\_text.

    Args:
        old\_text: The original text.
        new\_text: The new text.
        path: Optional file path for the diff header.
        inclu
    ...

**Parameters:**

    - ``old_text`` (*str*)
    - ``new_text`` (*str*)
    - ``path`` (*str*) = ``''``
    - ``include_file_header`` (*bool*) = ``True``

**Returns:** ``str``

**Calls:**

    - :ref:`endswith <func-endswith>`
    - :ref:`join <func-join>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`startswith <func-startswith>`
    - :ref:`unified_diff <func-unified_diff>`

**Called by:**

    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.ui.shell.visualize._ApprovalRequestPanel``)



G
-

.. _func-generate_session_title:

generate_session_title
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 1105)

**Description:**

    Generate a concise session title using AI based on the first conversation turn.

    If request body is empty or parameters are missing, the backend will
    automatically read the first turn from wir
    ...

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
    - :ref:`get_editable_session <func-get_editable_session>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`load_session_metadata <func-load_session_metadata>`
    - :ref:`save_session_metadata <func-save_session_metadata>`
    - :ref:`len <func-len>`
    - :ref:`model_copy <func-model_copy>`
    - :ref:`post <func-post>`
    - :ref:`shorten <func-shorten>`
    - :ref:`split <func-split>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`


.. _func-get_agents_dir:

get_agents_dir
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.agentspec``

**File:** :file:`src/kimi_cli/agentspec.py` (line 11)

**Description:**

    Get Agents Dir.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`


.. _func-get_builtin_skills_dir:

get_builtin_skills_dir
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 26)

**Description:**

    Get the built-in skills directory path.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`

**Called by:**

    - :ref:`resolve_skills_roots <func-resolve_skills_roots>` (from ``kimi_cli.skill.__init__``)


.. _func-get_clean_env:

get_clean_env
^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.subprocess_env``

**File:** :file:`src/kimi_cli/utils/subprocess_env.py` (line 35)

**Description:**

    Get a clean environment suitable for spawning subprocesses.

    In a PyInstaller-frozen application on Linux, this function restores
    the original library path environment variables, preventing su
    ...

**Parameters:**

    - ``base_env`` = ``None``

**Calls:**

    - :ref:`dict <func-dict>`
    - :ref:`getattr <func-getattr>`

**Called by:**

    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.tools.shell.__init__.Shell``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`get_session_git_diff <func-get_session_git_diff>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`start <func-start>` (from ``kimi_cli.web.runner.process.SessionProcess``)


.. _func-get_client_ip:

get_client_ip
^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 15)

**Description:**

    Extract client IP from request.

    Args:
        request: The incoming request
        trust\_proxy: If True, trust X-Forwarded-For header (only enable behind trusted proxy)

**Parameters:**

    - ``request`` (*Request*)
    - ``trust_proxy`` (*bool*) = ``False``

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`split <func-split>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`dispatch <func-dispatch>` (from ``kimi_cli.web.auth.AuthMiddleware``)


.. _func-get_config_file:

get_config_file
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 21)

**Description:**

    Get the configuration file path.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - :ref:`load_config <func-load_config>` (from ``kimi_cli.config``)
    - :ref:`save_config <func-save_config>` (from ``kimi_cli.config``)
    - :ref:`get_config_toml <func-get_config_toml>` (from ``kimi_cli.web.api.config``)
    - :ref:`update_config_toml <func-update_config_toml>` (from ``kimi_cli.web.api.config``)


.. _func-get_config_toml:

get_config_toml
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.config``

**File:** :file:`src/kimi_cli/web/api/config.py` (line 115)

**Description:**

    Get kimi-cli config.toml.

**Parameters:**

    - ``http_request`` (*Request*)

**Returns:** ``ConfigToml``

**Calls:**

    - :ref:`ConfigToml <func-ConfigToml>`
    - :ref:`exists <func-exists>`
    - :ref:`get <func-get>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`read_text <func-read_text>`
    - :ref:`str <func-str>`


.. _func-get_current_acp_tool_call_id_or_none:

get_current_acp_tool_call_id_or_none
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 101)

**Description:**

    See \`\_ToolCallState.acp\_tool\_call\_id\`.

**Returns:** ``str | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`get_current_tool_call_or_none <func-get_current_tool_call_or_none>`

**Called by:**

    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.acp.tools.Terminal``)


.. _func-get_current_tool_call_or_none:

get_current_tool_call_or_none
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 50)

**Description:**

    Get the current tool call or None.
    Expect to be not None when called from a \`\_\_call\_\_\` method of a tool.

**Returns:** ``ToolCall | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - :ref:`get_current_acp_tool_call_id_or_none <func-get_current_acp_tool_call_id_or_none>` (from ``kimi_cli.acp.session``)
    - :ref:`request <func-request>` (from ``kimi_cli.soul.approval.Approval``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.soul.toolset.WireExternalTool``)
    - :ref:`_run_subagent <func-_run_subagent>` (from ``kimi_cli.tools.multiagent.task.Task``)
    - :ref:`_fetch_with_service <func-_fetch_with_service>` (from ``kimi_cli.tools.web.fetch.FetchURL``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.web.search.SearchWeb``)


.. _func-get_cursor_row:

get_cursor_row
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.term``

**File:** :file:`src/kimi_cli/utils/term.py` (line 133)

**Description:**

    Get the current cursor row (1-indexed).

**Returns:** ``int | None``

**Calls:**

    - :ref:`isatty <func-isatty>`
    - :ref:`_cursor_position_unix <func-_cursor_position_unix>`
    - :ref:`_cursor_position_windows <func-_cursor_position_windows>`


.. _func-get_default_config:

get_default_config
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 163)

**Description:**

    Get the default configuration.

**Returns:** ``Config``

**Calls:**

    - :ref:`Config <func-Config>`
    - :ref:`Services <func-Services>`

**Called by:**

    - :ref:`load_config <func-load_config>` (from ``kimi_cli.config``)


.. _func-get_device_id:

get_device_id
^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 231)

**Description:**

    Get Device Id.

**Returns:** ``str``

**Calls:**

    - :ref:`exists <func-exists>`
    - :ref:`_device_id_path <func-_device_id_path>`
    - :ref:`_ensure_private_file <func-_ensure_private_file>`
    - :ref:`read_text <func-read_text>`
    - :ref:`strip <func-strip>`
    - :ref:`uuid4 <func-uuid4>`
    - :ref:`write_text <func-write_text>`

**Called by:**

    - :ref:`_common_headers <func-_common_headers>` (from ``kimi_cli.auth.oauth``)


.. _func-get_editable_session:

get_editable_session
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 335)

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

    - :ref:`delete_session <func-delete_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`update_session <func-update_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`upload_session_file <func-upload_session_file>` (from ``kimi_cli.web.api.sessions``)


.. _func-get_env_bool:

get_env_bool
^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.envvar``

**File:** :file:`src/kimi_cli/utils/envvar.py` (line 21)

**Description:**

    Get Env Bool.
    
    Args:
    name: Description.
    default: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``name`` (*str*)
    - ``default`` (*bool*) = ``False``

**Returns:** ``bool``

**Calls:**

    - :ref:`getenv <func-getenv>`
    - :ref:`lower <func-lower>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)


.. _func-get_global_config:

get_global_config
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.config``

**File:** :file:`src/kimi_cli/web/api/config.py` (line 159)

**Description:**

    Get global (kimi-cli) config snapshot.

**Returns:** ``GlobalConfig``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`_build_global_config <func-_build_global_config>`


.. _func-get_global_mcp_config_file:

get_global_mcp_config_file
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 8)

**Description:**

    Get the global MCP config file path.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`_load_mcp_config <func-_load_mcp_config>` (from ``kimi_cli.cli.mcp``)
    - :ref:`_save_mcp_config <func-_save_mcp_config>` (from ``kimi_cli.cli.mcp``)
    - :ref:`mcp_add <func-mcp_add>` (from ``kimi_cli.cli.mcp``)
    - :ref:`mcp_list <func-mcp_list>` (from ``kimi_cli.cli.mcp``)
    - :ref:`mcp_remove <func-mcp_remove>` (from ``kimi_cli.cli.mcp``)
    - :ref:`run_worker <func-run_worker>` (from ``kimi_cli.web.runner.worker``)


.. _func-get_metadata_file:

get_metadata_file
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 12)

**Description:**

    Get Metadata File.

**Returns:** ``Path``

**Calls:**

    - :ref:`get_share_dir <func-get_share_dir>`

**Called by:**

    - :ref:`load_metadata <func-load_metadata>` (from ``kimi_cli.metadata``)
    - :ref:`save_metadata <func-save_metadata>` (from ``kimi_cli.metadata``)


.. _func-get_platform_by_id:

get_platform_by_id
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 104)

**Description:**

    Get Platform By Id.
    
    Args:
    platform\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - :ref:`_apply_kimi_code_config <func-_apply_kimi_code_config>` (from ``kimi_cli.auth.oauth``)
    - :ref:`login_kimi_code <func-login_kimi_code>` (from ``kimi_cli.auth.oauth``)
    - :ref:`get_platform_name_for_provider <func-get_platform_name_for_provider>` (from ``kimi_cli.auth.platforms``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`_usage_url <func-_usage_url>` (from ``kimi_cli.ui.shell.usage``)


.. _func-get_platform_by_name:

get_platform_by_name
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 116)

**Description:**

    Get Platform By Name.
    
    Args:
    name: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``name`` (*str*)

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - :ref:`select_platform <func-select_platform>` (from ``kimi_cli.ui.shell.setup``)


.. _func-get_platform_name_for_provider:

get_platform_name_for_provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 179)

**Description:**

    Get Platform Name For Provider.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`get_platform_by_id <func-get_platform_by_id>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`

**Called by:**

    - :ref:`model <func-model>` (from ``kimi_cli.ui.shell.slash``)


.. _func-get_project_skills_dir_candidates:

get_project_skills_dir_candidates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 32)

**Description:**

    Get project-level skills directory candidates in priority order.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Called by:**

    - :ref:`find_project_skills_dir <func-find_project_skills_dir>` (from ``kimi_cli.skill.__init__``)


.. _func-get_runner:

get_runner
^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 72)

**Description:**

    Get the KimiCLIRunner from the FastAPI app state.

**Parameters:**

    - ``req`` (*Request*)

**Returns:** ``KimiCLIRunner``


.. _func-get_runner_ws:

get_runner_ws
^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 76)

**Description:**

    Get the KimiCLIRunner from the FastAPI app state (for WebSocket routes).

**Parameters:**

    - ``ws`` (*WebSocket*)

**Returns:** ``KimiCLIRunner``


.. _func-get_session:

get_session
^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 522)

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

    - :ref:`delete_session <func-delete_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_editable_session <func-get_editable_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_session <func-get_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`list_sessions <func-list_sessions>` (from ``kimi_cli.web.api.sessions``)


.. _func-get_session_file:

get_session_file
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 678)

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
    - :ref:`is_dir <func-is_dir>`
    - :ref:`is_relative_to <func-is_relative_to>`
    - :ref:`iterdir <func-iterdir>`
    - :ref:`_contains_symlink <func-_contains_symlink>`
    - :ref:`_ensure_public_file_access_allowed <func-_ensure_public_file_access_allowed>`
    - :ref:`_is_path_in_sensitive_location <func-_is_path_in_sensitive_location>`
    - :ref:`_is_sensitive_relative_path <func-_is_sensitive_relative_path>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`quote <func-quote>`
    - :ref:`read_bytes <func-read_bytes>`
    - :ref:`relative_to <func-relative_to>`
    - :ref:`resolve <func-resolve>`
    - :ref:`sort <func-sort>`
    - :ref:`stat <func-stat>`
    - :ref:`str <func-str>`


.. _func-get_session_git_diff:

get_session_git_diff
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 91)

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
    - :ref:`int <func-int>`
    - :ref:`get_clean_env <func-get_clean_env>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`len <func-len>`
    - :ref:`split <func-split>`
    - :ref:`strip <func-strip>`
    - :ref:`wait_for <func-wait_for>`


.. _func-get_session_upload_file:

get_session_upload_file
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 632)

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


.. _func-get_share_dir:

get_share_dir
^^^^^^^^^^^^^

**Module:** ``kimi_cli.share``

**File:** :file:`src/kimi_cli/share.py` (line 5)

**Description:**

    Get the share directory path.

**Returns:** ``Path``

**Calls:**

    - :ref:`Path <func-Path>`
    - :ref:`getenv <func-getenv>`
    - :ref:`home <func-home>`
    - :ref:`mkdir <func-mkdir>`

**Called by:**

    - :ref:`enable_logging <func-enable_logging>` (from ``kimi_cli.app``)
    - :ref:`_credentials_dir <func-_credentials_dir>` (from ``kimi_cli.auth.oauth``)
    - :ref:`_device_id_path <func-_device_id_path>` (from ``kimi_cli.auth.oauth``)
    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>` (from ``kimi_cli.cli.mcp``)
    - :ref:`_migrate_json_config_to_toml <func-_migrate_json_config_to_toml>` (from ``kimi_cli.config``)
    - :ref:`get_config_file <func-get_config_file>` (from ``kimi_cli.config``)
    - :ref:`sessions_dir <func-sessions_dir>` (from ``kimi_cli.metadata.WorkDirMeta``)
    - :ref:`get_metadata_file <func-get_metadata_file>` (from ``kimi_cli.metadata``)
    - :ref:`_download_and_install_rg <func-_download_and_install_rg>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`_find_existing_rg <func-_find_existing_rg>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.ui.shell.prompt.CustomPromptSession``)


.. _func-get_startup_dir:

get_startup_dir
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 252)

**Description:**

    Get the directory where kimi web was started.

**Parameters:**

    - ``request`` (*Request*)

**Returns:** ``str``

**Calls:**

    - :ref:`get <func-get>`


.. _func-get_user_skills_dir_candidates:

get_user_skills_dir_candidates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 49)

**Description:**

    Get user-level skills directory candidates in priority order.

**Calls:**

    - :ref:`home <func-home>`

**Called by:**

    - :ref:`find_user_skills_dir <func-find_user_skills_dir>` (from ``kimi_cli.skill.__init__``)


.. _func-get_wire_or_none:

get_wire_or_none
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 135)

**Description:**

    Get the current wire or None.
    Expect to be not None when called from anywhere in the agent loop.

**Returns:** ``Wire | None``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - :ref:`wire_send <func-wire_send>` (from ``kimi_cli.soul.__init__``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.soul.toolset.WireExternalTool``)
    - :ref:`_run_subagent <func-_run_subagent>` (from ``kimi_cli.tools.multiagent.task.Task``)


.. _func-get_work_dirs:

get_work_dirs
^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 317)

**Description:**

    Get a list of available work directories from metadata.

**Returns:** ``list[str]``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`to_thread <func-to_thread>`


.. _func-grab_image_from_clipboard:

grab_image_from_clipboard
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.clipboard``

**File:** :file:`src/kimi_cli/utils/clipboard.py` (line 114)

**Description:**

    Read an image from the clipboard if possible.

**Returns:** ``Image.Image | None``

**Calls:**

    - :ref:`grabclipboard <func-grabclipboard>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_open_first_image <func-_open_first_image>`
    - :ref:`_read_clipboard_file_paths_macos_native <func-_read_clipboard_file_paths_macos_native>`

**Called by:**

    - :ref:`_try_paste_image <func-_try_paste_image>` (from ``kimi_cli.ui.shell.prompt.CustomPromptSession``)



H
-

.. _func-Heading.create:

Heading.create
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 195)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``Heading``

**Calls:**

    - :ref:`cls <func-cls>`


.. _func-Heading.on_enter:

Heading.on_enter
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 198)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``

**Calls:**

    - :ref:`Text <func-Text>`
    - :ref:`enter_style <func-enter_style>`


.. _func-help:

help
^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 63)

**Description:**

    Show help information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`Text <func-Text>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`pager <func-pager>`
    - :ref:`print <func-print>`
    - :ref:`section <func-section>`
    - :ref:`slash_name <func-slash_name>`
    - :ref:`sorted <func-sorted>`
    - :ref:`startswith <func-startswith>`
    - :ref:`values <func-values>`



I
-

.. _func-ImageItem.create:

ImageItem.create
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 512)

**Description:**

    Factory to create markdown element,

        Args:
            markdown (Markdown): The parent Markdown object.
            token (Any): A token from markdown-it.

        Returns:
            Markdow
    ...

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``MarkdownElement``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`get <func-get>`
    - :ref:`str <func-str>`


.. _func-ImageItem.on_enter:

ImageItem.on_enter
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 530)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``

**Calls:**

    - :ref:`Text <func-Text>`
    - :ref:`on_enter <func-on_enter>`
    - :ref:`super <func-super>`


.. _func-index_skills:

index_skills
^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 138)

**Description:**

    Build a lookup table for skills by normalized name.

**Parameters:**

    - ``skills`` (*Iterable[Skill]*)

**Calls:**

    - :ref:`normalize_skill_name <func-normalize_skill_name>`

**Called by:**

    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)


.. _func-info:

info
^^^^

**Module:** ``kimi_cli.cli.info``

**File:** :file:`src/kimi_cli/cli/info.py` (line 76)

**Description:**

    Show version and protocol information.

**Parameters:**

    - ``json_output`` = ``False``

**Calls:**

    - :ref:`Option <func-Option>`
    - :ref:`callback <func-callback>`
    - :ref:`_emit_info <func-_emit_info>`

**Called by:**

    - :ref:`acp_main <func-acp_main>` (from ``kimi_cli.acp.__init__``)
    - :ref:`cancel <func-cancel>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`initialize <func-initialize>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`list_sessions <func-list_sessions>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`load_session <func-load_session>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`new_session <func-new_session>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`on_connect <func-on_connect>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`prompt <func-prompt>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`set_session_model <func-set_session_model>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`prompt <func-prompt>` (from ``kimi_cli.acp.session.ACPSession``)
    - :ref:`create <func-create>` (from ``kimi_cli.app.KimiCLI``)
    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`_migrate_json_config_to_toml <func-_migrate_json_config_to_toml>` (from ``kimi_cli.config``)
    - :ref:`_migrate_session_context_file <func-_migrate_session_context_file>` (from ``kimi_cli.session``)
    - :ref:`discover_skills <func-discover_skills>` (from ``kimi_cli.skill.__init__``)
    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)
    - :ref:`_load_system_prompt <func-_load_system_prompt>` (from ``kimi_cli.soul.agent``)
    - :ref:`load_agent <func-load_agent>` (from ``kimi_cli.soul.agent``)
    - :ref:`load_agents_md <func-load_agents_md>` (from ``kimi_cli.soul.agent``)
    - :ref:`run <func-run>` (from ``kimi_cli.soul.kimisoul.FlowRunner``)
    - :ref:`_agent_loop <func-_agent_loop>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_retry_log <func-_retry_log>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.slash``)
    - :ref:`compact <func-compact>` (from ``kimi_cli.soul.slash``)
    - :ref:`load_mcp_tools <func-load_mcp_tools>` (from ``kimi_cli.soul.toolset.KimiToolset``)
    - :ref:`load_tools <func-load_tools>` (from ``kimi_cli.soul.toolset.KimiToolset``)
    - :ref:`_download_and_install_rg <func-_download_and_install_rg>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.acp.__init__.ACP``)
    - :ref:`on_connect <func-on_connect>` (from ``kimi_cli.ui.acp.__init__.ACPServerSingleSession``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.print.__init__.Print``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_run_slash_command <func-_run_slash_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run_soul_command <func-run_soul_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_build_replay_turns_from_wire <func-_build_replay_turns_from_wire>` (from ``kimi_cli.ui.shell.replay``)
    - :ref:`_do_update <func-_do_update>` (from ``kimi_cli.ui.shell.update``)
    - :ref:`_send_merged <func-_send_merged>` (from ``kimi_cli.wire.__init__.WireSoulSide``)
    - :ref:`send <func-send>` (from ``kimi_cli.wire.__init__.WireSoulSide``)
    - :ref:`_read_loop <func-_read_loop>` (from ``kimi_cli.wire.server.WireServer``)
    - :ref:`serve <func-serve>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-init:

init
^^^^

**Module:** ``kimi_cli.soul.slash``

**File:** :file:`src/kimi_cli/soul/slash.py` (line 51)

**Description:**

    Analyze the codebase and generate an \`AGENTS.md\` file

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`Context <func-Context>`
    - :ref:`KimiSoul <func-KimiSoul>`
    - :ref:`Message <func-Message>`
    - :ref:`Path <func-Path>`
    - :ref:`TemporaryDirectory <func-TemporaryDirectory>`
    - :ref:`append_message <func-append_message>`
    - :ref:`load_agents_md <func-load_agents_md>`
    - :ref:`system <func-system>`
    - :ref:`run <func-run>`


.. _func-install_sigint_handler:

install_sigint_handler
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.signals``

**File:** :file:`src/kimi_cli/utils/signals.py` (line 7)

**Description:**

    Install a SIGINT handler that works on Unix and Windows.

    On Unix event loops, prefer \`loop.add\_signal\_handler\`.
    On Windows (or other platforms) where it is not implemented, fall back to
    \`
    ...

**Parameters:**

    - ``loop`` (*asyncio.AbstractEventLoop*)
    - ``handler``

**Calls:**

    - :ref:`add_signal_handler <func-add_signal_handler>`
    - :ref:`getsignal <func-getsignal>`
    - :ref:`handler <func-handler>`
    - :ref:`remove_signal_handler <func-remove_signal_handler>`
    - :ref:`signal <func-signal>`
    - :ref:`suppress <func-suppress>`

**Called by:**

    - :ref:`run <func-run>` (from ``kimi_cli.ui.print.__init__.Print``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run_soul_command <func-run_soul_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`serve <func-serve>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-invalidate_sessions_cache:

invalidate_sessions_cache
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 37)

**Description:**

    Clear the sessions cache.

    Call this after any mutation (create/update/delete).
    This ensures the next read sees fresh data.

**Returns:** ``None``

**Called by:**

    - :ref:`create_session <func-create_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`delete_session <func-delete_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`update_session <func-update_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`run_auto_archive <func-run_auto_archive>` (from ``kimi_cli.web.store.sessions``)


.. _func-invalidate_work_dirs_cache:

invalidate_work_dirs_cache
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 80)

**Description:**

    Clear the work dirs cache.

**Returns:** ``None``

**Called by:**

    - :ref:`create_session <func-create_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)


.. _func-is_clipboard_available:

is_clipboard_available
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.clipboard``

**File:** :file:`src/kimi_cli/utils/clipboard.py` (line 11)

**Description:**

    Check if the Pyperclip clipboard is available.

**Returns:** ``bool``

**Calls:**

    - :ref:`paste <func-paste>`

**Called by:**

    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.ui.shell.prompt.CustomPromptSession``)


.. _func-is_event:

is_event
^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 333)

**Description:**

    Check if the message is an Event.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[Event]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - :ref:`_build_replay_turns_from_wire <func-_build_replay_turns_from_wire>` (from ``kimi_cli.ui.shell.replay``)
    - :ref:`_validate_params <func-_validate_params>` (from ``kimi_cli.wire.jsonrpc.JSONRPCEventMessage``)
    - :ref:`_handle_replay <func-_handle_replay>` (from ``kimi_cli.wire.server.WireServer``)
    - :ref:`_validate_event <func-_validate_event>` (from ``kimi_cli.wire.types.SubagentEvent``)


.. _func-is_managed_provider_key:

is_managed_provider_key
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 167)

**Description:**

    Is Managed Provider Key.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`startswith <func-startswith>`

**Called by:**

    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.ui.shell.oauth``)


.. _func-is_origin_allowed:

is_origin_allowed
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 98)

**Description:**

    Check if an origin is allowed.

    Args:
        origin: The origin to check
        allowed\_origins: List of allowed origins.
                        - None: use default localhost regex
            
    ...

**Parameters:**

    - ``origin`` (*str*)
    - ``allowed_origins`` (*Iterable[str] | None*)

**Returns:** ``bool``

**Calls:**

    - :ref:`bool <func-bool>`
    - :ref:`list <func-list>`
    - :ref:`match <func-match>`
    - :ref:`rstrip <func-rstrip>`

**Called by:**

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`dispatch <func-dispatch>` (from ``kimi_cli.web.auth.AuthMiddleware``)


.. _func-is_private_ip:

is_private_ip
^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 30)

**Description:**

    Check if an IP address is in a private range (RFC 1918 + localhost).

    Supports both IPv4 and IPv6 addresses.

**Parameters:**

    - ``ip`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`ip_address <func-ip_address>`

**Called by:**

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_get_private_addresses <func-_get_private_addresses>` (from ``kimi_cli.web.app``)
    - :ref:`dispatch <func-dispatch>` (from ``kimi_cli.web.auth.AuthMiddleware``)


.. _func-is_request:

is_request
^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 337)

**Description:**

    Check if the message is a Request.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[Request]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - :ref:`_read_wire_lines <func-_read_wire_lines>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_validate_params <func-_validate_params>` (from ``kimi_cli.wire.jsonrpc.JSONRPCRequestMessage``)
    - :ref:`_handle_replay <func-_handle_replay>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-is_wire_message:

is_wire_message
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 341)

**Description:**

    Check if the message is a WireMessage.

**Parameters:**

    - ``msg`` (*Any*)

**Returns:** ``TypeGuard[WireMessage]``

**Calls:**

    - :ref:`isinstance <func-isinstance>`

**Called by:**

    - :ref:`flush <func-flush>` (from ``kimi_cli.wire.__init__.WireSoulSide``)
    - :ref:`_validate_event <func-_validate_event>` (from ``kimi_cli.wire.types.SubagentEvent``)


.. _func-is_within_directory:

is_within_directory
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.path``

**File:** :file:`src/kimi_cli/utils/path.py` (line 10)

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

    - :ref:`_validate_directory <func-_validate_directory>` (from ``kimi_cli.tools.file.glob.Glob``)
    - :ref:`_validate_path <func-_validate_path>` (from ``kimi_cli.tools.file.read.ReadFile``)
    - :ref:`_validate_path <func-_validate_path>` (from ``kimi_cli.tools.file.read_media.ReadMediaFile``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.replace.StrReplaceFile``)
    - :ref:`_validate_path <func-_validate_path>` (from ``kimi_cli.tools.file.replace.StrReplaceFile``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.write.WriteFile``)
    - :ref:`_validate_path <func-_validate_path>` (from ``kimi_cli.tools.file.write.WriteFile``)



J
-

.. _func-JsonPrinter.feed:

JsonPrinter.feed
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 81)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`_ToolCallState <func-_ToolCallState>`
    - :ref:`flush <func-flush>`
    - :ref:`get <func-get>`
    - :ref:`_merge_content <func-_merge_content>`
    - :ref:`merge_in_place <func-merge_in_place>`


.. _func-JsonPrinter.flush:

JsonPrinter.flush
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 106)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`append <func-append>`
    - :ref:`clear <func-clear>`
    - :ref:`tool_result_to_message <func-tool_result_to_message>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`print <func-print>`
    - :ref:`values <func-values>`


.. _func-JSONRPCMessage.is_notification:

JSONRPCMessage.is_notification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.jsonrpc``

**File:** :file:`src/kimi_cli/wire/jsonrpc.py` (line 161)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-JSONRPCMessage.is_request:

JSONRPCMessage.is_request
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.jsonrpc``

**File:** :file:`src/kimi_cli/wire/jsonrpc.py` (line 158)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-JSONRPCMessage.is_response:

JSONRPCMessage.is_response
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.jsonrpc``

**File:** :file:`src/kimi_cli/wire/jsonrpc.py` (line 164)

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-JSONRPCMessage.method_is_inbound:

JSONRPCMessage.method_is_inbound
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.jsonrpc``

**File:** :file:`src/kimi_cli/wire/jsonrpc.py` (line 155)

**Parameters:**

    - ``self``

**Returns:** ``bool``



K
-

.. _func-KeyboardListener.get:

KeyboardListener.get
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 107)

**Parameters:**

    - ``self``

**Returns:** ``KeyEvent``

**Calls:**

    - :ref:`get <func-get>`


.. _func-KeyboardListener.pause:

KeyboardListener.pause
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 96)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`to_thread <func-to_thread>`


.. _func-KeyboardListener.resume:

KeyboardListener.resume
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 104)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`to_thread <func-to_thread>`


.. _func-KeyboardListener.start:

KeyboardListener.start
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 68)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Thread <func-Thread>`
    - :ref:`call_soon_threadsafe <func-call_soon_threadsafe>`
    - :ref:`get_running_loop <func-get_running_loop>`
    - :ref:`start <func-start>`


.. _func-KeyboardListener.stop:

KeyboardListener.stop
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 86)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`clear <func-clear>`
    - :ref:`is_alive <func-is_alive>`
    - :ref:`set <func-set>`
    - :ref:`to_thread <func-to_thread>`


.. _func-kimi:

kimi
^^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 197)

**Description:**

    Kimi, your next CLI agent.

**Parameters:**

    - ``ctx`` (*typer.Context*)
    - ``version`` = ``False``
    - ``verbose`` = ``False``
    - ``debug`` = ``False``
    - ``local_work_dir`` = ``None``
    - ``session_id`` = ``None``
    - ``continue_`` = ``False``
    - ``config_string`` = ``None``
    - ``config_file`` = ``None``
    - ``model_name`` = ``None``
    - ``thinking`` = ``None``
    - ``yolo`` = ``False``
    - ``prompt`` = ``None``
    - ``print_mode`` = ``False``
    - ``acp_mode`` = ``False``
    - ``wire_mode`` = ``False``
    - ``input_format`` = ``None``
    - ``output_format`` = ``None``
    - ``final_message_only`` = ``False``
    - ``quiet`` = ``False``
    - ``agent`` = ``None``
    - ``agent_file`` = ``None``
    - ``mcp_config_file`` = ``None``
    - ``mcp_config`` = ``None``
    - ``local_skills_dir`` = ``None``
    - ``max_steps_per_turn`` = ``None``
    - ``max_retries_per_step`` = ``None``
    - ``max_ralph_iterations`` = ``None``

**Calls:**

    - :ref:`BadParameter <func-BadParameter>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`Reload <func-Reload>`
    - :ref:`_emit_fatal_error <func-_emit_fatal_error>`
    - :ref:`_post_run <func-_post_run>`
    - :ref:`_reload_loop <func-_reload_loop>`
    - :ref:`_run <func-_run>`
    - :ref:`append <func-append>`
    - :ref:`callback <func-callback>`
    - :ref:`continue_ <func-continue_>`
    - :ref:`create <func-create>`
    - :ref:`cwd <func-cwd>`
    - :ref:`delete <func-delete>`
    - :ref:`echo <func-echo>`
    - :ref:`encode <func-encode>`
    - :ref:`exception <func-exception>`
    - :ref:`exists <func-exists>`
    - :ref:`find <func-find>`
    - :ref:`flush <func-flush>`
    - :ref:`format_exc <func-format_exc>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`get_work_dir_meta <func-get_work_dir_meta>`
    - :ref:`info <func-info>`
    - :ref:`is_empty <func-is_empty>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - :ref:`join <func-join>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`load_config_from_string <func-load_config_from_string>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`save_metadata <func-save_metadata>`
    - :ref:`get_share_dir <func-get_share_dir>`
    - :ref:`open_original_stderr <func-open_original_stderr>`
    - :ref:`redirect_stderr_to_logger <func-redirect_stderr_to_logger>`
    - :ref:`restore_stderr <func-restore_stderr>`
    - :ref:`ensure_tty_sane <func-ensure_tty_sane>`
    - :ref:`run_web_server <func-run_web_server>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`loads <func-loads>`
    - :ref:`new_work_dir_meta <func-new_work_dir_meta>`
    - :ref:`read_text <func-read_text>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`run_acp <func-run_acp>`
    - :ref:`run_print <func-run_print>`
    - :ref:`run_shell <func-run_shell>`
    - :ref:`run_wire_stdio <func-run_wire_stdio>`
    - :ref:`signal <func-signal>`
    - :ref:`unsafe_from_local_path <func-unsafe_from_local_path>`
    - :ref:`warning <func-warning>`
    - :ref:`write <func-write>`


.. _func-KimiCLI.create:

KimiCLI.create
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 64)

**Description:**

    Create a KimiCLI instance.

        Args:
            session (Session): A session created by \`Session.create\` or \`Session.continue\_\`.
            config (Config | Path | None, optional): Configuratio
    ...

**Parameters:**

    - ``session`` (*Session*)
    - ``config`` (*Config | Path | None*) = ``None``
    - ``model_name`` (*str | None*) = ``None``
    - ``thinking`` (*bool | None*) = ``None``
    - ``yolo`` (*bool*) = ``False``
    - ``agent_file`` (*Path | None*) = ``None``
    - ``mcp_configs`` = ``None``
    - ``skills_dir`` (*KaosPath | None*) = ``None``
    - ``max_steps_per_turn`` (*int | None*) = ``None``
    - ``max_retries_per_step`` (*int | None*) = ``None``
    - ``max_ralph_iterations`` (*int | None*) = ``None``

**Returns:** ``KimiCLI``

**Calls:**

    - :ref:`Context <func-Context>`
    - :ref:`KimiCLI <func-KimiCLI>`
    - :ref:`KimiSoul <func-KimiSoul>`
    - :ref:`LLMModel <func-LLMModel>`
    - :ref:`LLMProvider <func-LLMProvider>`
    - :ref:`OAuthManager <func-OAuthManager>`
    - :ref:`SecretStr <func-SecretStr>`
    - :ref:`create <func-create>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`load_config <func-load_config>`
    - :ref:`augment_provider_with_env_vars <func-augment_provider_with_env_vars>`
    - :ref:`create_llm <func-create_llm>`
    - :ref:`load_agent <func-load_agent>`
    - :ref:`restore <func-restore>`


.. _func-KimiCLI.run:

KimiCLI.run
^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 210)

**Description:**

    Run the Kimi Code CLI instance without any UI and yield Wire messages directly.

        Args:
            user\_input (str | list[ContentPart]): The user input to the agent.
            cancel\_event (
    ...

**Parameters:**

    - ``self``
    - ``user_input`` (*str | list[ContentPart]*)
    - ``cancel_event`` (*asyncio.Event*)
    - ``merge_wire_messages`` (*bool*) = ``False``

**Returns:** ``AsyncGenerator[WireMessage]``

**Calls:**

    - :ref:`Event <func-Event>`
    - :ref:`_env <func-_env>`
    - :ref:`create_task <func-create_task>`
    - :ref:`receive <func-receive>`
    - :ref:`run_soul <func-run_soul>`
    - :ref:`set <func-set>`
    - :ref:`set_result <func-set_result>`
    - :ref:`ui_side <func-ui_side>`
    - :ref:`wait <func-wait>`


.. _func-KimiCLI.run_acp:

KimiCLI.run_acp
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 358)

**Description:**

    Run the Kimi Code CLI instance as ACP server.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`ACP <func-ACP>`
    - :ref:`_env <func-_env>`
    - :ref:`run <func-run>`


.. _func-KimiCLI.run_print:

KimiCLI.run_print
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 337)

**Description:**

    Run the Kimi Code CLI instance with print UI.

**Parameters:**

    - ``self``
    - ``input_format`` (*InputFormat*)
    - ``output_format`` (*OutputFormat*)
    - ``command`` (*str | None*) = ``None``
    - ``final_only`` (*bool*) = ``False``

**Returns:** ``bool``

**Calls:**

    - :ref:`Print <func-Print>`
    - :ref:`_env <func-_env>`
    - :ref:`run <func-run>`


.. _func-KimiCLI.run_shell:

KimiCLI.run_shell
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 259)

**Description:**

    Run the Kimi Code CLI instance with shell UI.

**Parameters:**

    - ``self``
    - ``command`` (*str | None*) = ``None``

**Returns:** ``bool``

**Calls:**

    - :ref:`Shell <func-Shell>`
    - :ref:`WelcomeInfoItem <func-WelcomeInfoItem>`
    - :ref:`_env <func-_env>`
    - :ref:`append <func-append>`
    - :ref:`get <func-get>`
    - :ref:`model_display_name <func-model_display_name>`
    - :ref:`shorten_home <func-shorten_home>`
    - :ref:`run <func-run>`
    - :ref:`str <func-str>`


.. _func-KimiCLI.run_wire_stdio:

KimiCLI.run_wire_stdio
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 366)

**Description:**

    Run the Kimi Code CLI instance as Wire server over stdio.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`WireServer <func-WireServer>`
    - :ref:`_env <func-_env>`
    - :ref:`serve <func-serve>`


.. _func-KimiCLI.session:

KimiCLI.session
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 194)

**Description:**

    Get the Session instance.

**Parameters:**

    - ``self``

**Returns:** ``Session``


.. _func-KimiCLI.soul:

KimiCLI.soul
^^^^^^^^^^^^

**Module:** ``kimi_cli.app``

**File:** :file:`src/kimi_cli/app.py` (line 189)

**Description:**

    Get the KimiSoul instance.

**Parameters:**

    - ``self``

**Returns:** ``KimiSoul``


.. _func-KimiCLIRunner.detach_websocket:

KimiCLIRunner.detach_websocket
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 697)

**Description:**

    Detach a WebSocket from a session.

**Parameters:**

    - ``self``
    - ``ws`` (*WebSocket*)
    - ``session_id`` (*UUID*)

**Returns:** ``None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`remove_websocket <func-remove_websocket>`


.. _func-KimiCLIRunner.get_or_create_session:

KimiCLIRunner.get_or_create_session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 686)

**Description:**

    Get or create a session process.

**Parameters:**

    - ``self``
    - ``session_id`` (*UUID*)

**Returns:** ``SessionProcess``

**Calls:**

    - :ref:`SessionProcess <func-SessionProcess>`


.. _func-KimiCLIRunner.get_session:

KimiCLIRunner.get_session
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 693)

**Description:**

    Get a session process if it exists.

**Parameters:**

    - ``self``
    - ``session_id`` (*UUID*)

**Returns:** ``SessionProcess | None``

**Calls:**

    - :ref:`get <func-get>`


.. _func-KimiCLIRunner.restart_running_workers:

KimiCLIRunner.restart_running_workers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 704)

**Description:**

    Restart all running workers to apply global config updates.

        Args:
            reason: Reason for the restart (e.g., "config\_update")
            force: If True, also restart busy sessions (ma
    ...

**Parameters:**

    - ``self``
    - ``reason`` (*str*)
    - ``force`` (*bool*)

**Returns:** ``RestartWorkersSummary``

**Calls:**

    - :ref:`RestartWorkersSummary <func-RestartWorkersSummary>`
    - :ref:`append <func-append>`
    - :ref:`create_task <func-create_task>`
    - :ref:`gather <func-gather>`
    - :ref:`items <func-items>`
    - :ref:`restart_worker <func-restart_worker>`


.. _func-KimiCLIRunner.start:

KimiCLIRunner.start
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 669)

**Description:**

    Start the runner (no-op, sessions started on demand).

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-KimiCLIRunner.stop:

KimiCLIRunner.stop
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 673)

**Description:**

    Stop all running sessions.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`cancel <func-cancel>`
    - :ref:`create_task <func-create_task>`
    - :ref:`stop <func-stop>`
    - :ref:`suppress <func-suppress>`
    - :ref:`values <func-values>`
    - :ref:`wait <func-wait>`


.. _func-KimiSoul.agent:

KimiSoul.agent
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 163)

**Parameters:**

    - ``self``

**Returns:** ``Agent``


.. _func-KimiSoul.available_slash_commands:

KimiSoul.available_slash_commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 188)

**Parameters:**

    - ``self``

**Returns:** ``list[SlashCommand[Any]]``


.. _func-KimiSoul.compact_context:

KimiSoul.compact_context
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 489)

**Description:**

    Compact the context.

        Raises:
            LLMNotSet: When the LLM is not set.
            ChatProviderError: When the chat provider returns an error.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`CompactionBegin <func-CompactionBegin>`
    - :ref:`CompactionEnd <func-CompactionEnd>`
    - :ref:`LLMNotSet <func-LLMNotSet>`
    - :ref:`_checkpoint <func-_checkpoint>`
    - :ref:`_compact_with_retry <func-_compact_with_retry>`
    - :ref:`append_message <func-append_message>`
    - :ref:`clear <func-clear>`
    - :ref:`compact <func-compact>`
    - :ref:`partial <func-partial>`
    - :ref:`retry_if_exception <func-retry_if_exception>`
    - :ref:`stop_after_attempt <func-stop_after_attempt>`
    - :ref:`wait_exponential_jitter <func-wait_exponential_jitter>`
    - :ref:`wire_send <func-wire_send>`


.. _func-KimiSoul.context:

KimiSoul.context
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 171)

**Parameters:**

    - ``self``

**Returns:** ``Context``


.. _func-KimiSoul.model_capabilities:

KimiSoul.model_capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 141)

**Parameters:**

    - ``self``

**Returns:** ``set[ModelCapability] | None``


.. _func-KimiSoul.model_name:

KimiSoul.model_name
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 137)

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-KimiSoul.name:

KimiSoul.name
^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 133)

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-KimiSoul.run:

KimiSoul.run
^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 191)

**Parameters:**

    - ``self``
    - ``user_input`` (*str | list[ContentPart]*)

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`TurnBegin <func-TurnBegin>`
    - :ref:`TurnEnd <func-TurnEnd>`
    - :ref:`_find_slash_command <func-_find_slash_command>`
    - :ref:`_turn <func-_turn>`
    - :ref:`ensure_fresh <func-ensure_fresh>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`func <func-func>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`parse_slash_command_call <func-parse_slash_command_call>`
    - :ref:`ralph_loop <func-ralph_loop>`
    - :ref:`run <func-run>`
    - :ref:`strip <func-strip>`
    - :ref:`wire_send <func-wire_send>`


.. _func-KimiSoul.runtime:

KimiSoul.runtime
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 167)

**Parameters:**

    - ``self``

**Returns:** ``Runtime``


.. _func-KimiSoul.status:

KimiSoul.status
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 156)

**Parameters:**

    - ``self``

**Returns:** ``StatusSnapshot``

**Calls:**

    - :ref:`StatusSnapshot <func-StatusSnapshot>`
    - :ref:`is_yolo <func-is_yolo>`


.. _func-KimiSoul.thinking:

KimiSoul.thinking
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 147)

**Description:**

    Whether thinking mode is enabled.

**Parameters:**

    - ``self``

**Returns:** ``bool | None``


.. _func-KimiSoul.wire_file:

KimiSoul.wire_file
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.kimisoul``

**File:** :file:`src/kimi_cli/soul/kimisoul.py` (line 181)

**Parameters:**

    - ``self``

**Returns:** ``WireFile``


.. _func-KimiToolset.add:

KimiToolset.add
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 82)

**Parameters:**

    - ``self``
    - ``tool`` (*ToolType*)

**Returns:** ``None``


.. _func-KimiToolset.cleanup:

KimiToolset.cleanup
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 343)

**Description:**

    Cleanup any resources held by the toolset.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`cancel <func-cancel>`
    - :ref:`close <func-close>`
    - :ref:`suppress <func-suppress>`
    - :ref:`values <func-values>`


.. _func-KimiToolset.find:

KimiToolset.find
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 89)

**Parameters:**

    - ``self``
    - ``tool_name_or_type`` (*str | type[ToolType]*)

**Returns:** ``ToolType | None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`values <func-values>`


.. _func-KimiToolset.handle:

KimiToolset.handle
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 102)

**Parameters:**

    - ``self``
    - ``tool_call`` (*ToolCall*)

**Returns:** ``HandleResult``

**Calls:**

    - :ref:`ToolNotFoundError <func-ToolNotFoundError>`
    - :ref:`ToolParseError <func-ToolParseError>`
    - :ref:`ToolResult <func-ToolResult>`
    - :ref:`ToolRuntimeError <func-ToolRuntimeError>`
    - :ref:`_call <func-_call>`
    - :ref:`create_task <func-create_task>`
    - :ref:`loads <func-loads>`
    - :ref:`reset <func-reset>`
    - :ref:`str <func-str>`


.. _func-KimiToolset.load_mcp_tools:

KimiToolset.load_mcp_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 208)

**Description:**

    Load MCP tools from specified MCP configs.

        Raises:
            MCPRuntimeError(KimiCLIException, RuntimeError): When any MCP server cannot be
                connected.

**Parameters:**

    - ``self``
    - ``mcp_configs`` (*list[MCPConfig]*)
    - ``runtime`` (*Runtime*)
    - ``in_background`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`Client <func-Client>`
    - :ref:`FileTokenStorage <func-FileTokenStorage>`
    - :ref:`MCPConfig <func-MCPConfig>`
    - :ref:`MCPRuntimeError <func-MCPRuntimeError>`
    - :ref:`MCPServerInfo <func-MCPServerInfo>`
    - :ref:`MCPTool <func-MCPTool>`
    - :ref:`_check_oauth_tokens <func-_check_oauth_tokens>`
    - :ref:`_connect <func-_connect>`
    - :ref:`_connect_server <func-_connect_server>`
    - :ref:`_toast_mcp <func-_toast_mcp>`
    - :ref:`add <func-add>`
    - :ref:`append <func-append>`
    - :ref:`create_task <func-create_task>`
    - :ref:`debug <func-debug>`
    - :ref:`error <func-error>`
    - :ref:`gather <func-gather>`
    - :ref:`get <func-get>`
    - :ref:`get_tokens <func-get_tokens>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - :ref:`toast <func-toast>`
    - :ref:`list_tools <func-list_tools>`
    - :ref:`warning <func-warning>`


.. _func-KimiToolset.load_tools:

KimiToolset.load_tools
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 157)

**Description:**

    Load tools from paths like \`kimi\_cli.tools.shell:Shell\`.

        Raises:
            InvalidToolError(KimiCLIException, ValueError): When any tool cannot be loaded.

**Parameters:**

    - ``self``
    - ``tool_paths`` (*list[str]*)
    - ``dependencies``

**Returns:** ``None``

**Calls:**

    - :ref:`InvalidToolError <func-InvalidToolError>`
    - :ref:`_load_tool <func-_load_tool>`
    - :ref:`add <func-add>`
    - :ref:`append <func-append>`
    - :ref:`info <func-info>`


.. _func-KimiToolset.mcp_servers:

KimiToolset.mcp_servers
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 153)

**Description:**

    Get MCP servers info.

**Parameters:**

    - ``self``


.. _func-KimiToolset.register_external_tool:

KimiToolset.register_external_tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 131)

**Parameters:**

    - ``self``
    - ``name`` (*str*)
    - ``description`` (*str*)
    - ``parameters``

**Calls:**

    - :ref:`WireExternalTool <func-WireExternalTool>`
    - :ref:`add <func-add>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`str <func-str>`


.. _func-KimiToolset.tools:

KimiToolset.tools
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 99)

**Parameters:**

    - ``self``

**Returns:** ``list[Tool]``

**Calls:**

    - :ref:`values <func-values>`


.. _func-KimiToolset.wait_for_mcp_tools:

KimiToolset.wait_for_mcp_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.toolset``

**File:** :file:`src/kimi_cli/soul/toolset.py` (line 332)

**Description:**

    Wait for background MCP tool loading to finish.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`done <func-done>`



L
-

.. _func-LaborMarket.add_dynamic_subagent:

LaborMarket.add_dynamic_subagent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 74)

**Description:**

    Add a dynamic subagent.

**Parameters:**

    - ``self``
    - ``name`` (*str*)
    - ``agent`` (*Agent*)


.. _func-LaborMarket.add_fixed_subagent:

LaborMarket.add_fixed_subagent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 69)

**Description:**

    Add a fixed subagent.

**Parameters:**

    - ``self``
    - ``name`` (*str*)
    - ``agent`` (*Agent*)
    - ``description`` (*str*)


.. _func-LaborMarket.subagents:

LaborMarket.subagents
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 65)

**Description:**

    Get all subagents in the labor market.

**Parameters:**

    - ``self``


.. _func-Link.create:

Link.create
^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 498)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``MarkdownElement``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`get <func-get>`
    - :ref:`str <func-str>`


.. _func-list_directory:

list_directory
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.path``

**File:** :file:`src/kimi_cli/utils/path.py` (line 23)

**Description:**

    Return an \`\`ls\`\`-like listing of \*work\_dir\*.

    This helper is used mainly to provide context to the LLM (for example
    \`\`KIMI\_WORK\_DIR\_LS\`\`) and to show top-level directory contents in tools.
   
    ...

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

    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)
    - :ref:`_validate_pattern <func-_validate_pattern>` (from ``kimi_cli.tools.file.glob.Glob``)


.. _func-list_models:

list_models
^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 262)

**Description:**

    List Models.
    
    Args:
    platform: Description.
    api\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform`` (*Platform*)
    - ``api_key`` (*str*)

**Returns:** ``list[ModelInfo]``

**Calls:**

    - :ref:`_list_models <func-_list_models>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`startswith <func-startswith>`
    - :ref:`tuple <func-tuple>`

**Called by:**

    - :ref:`login_kimi_code <func-login_kimi_code>` (from ``kimi_cli.auth.oauth``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`_setup_platform <func-_setup_platform>` (from ``kimi_cli.ui.shell.setup``)


.. _func-list_sessions:

list_sessions
^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 487)

**Description:**

    List sessions with optional pagination and search.

    Args:
        limit: Maximum number of sessions to return (default 100, max 500).
        offset: Number of sessions to skip (default 0).
      
    ...

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


.. _func-list_sessions:

list_sessions
^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 314)

**Description:**

    List sessions and resume optionally

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`ChoiceInput <func-ChoiceInput>`
    - :ref:`Reload <func-Reload>`
    - :ref:`append <func-append>`
    - :ref:`command <func-command>`
    - :ref:`insert <func-insert>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`format_relative_time <func-format_relative_time>`
    - :ref:`list <func-list>`
    - :ref:`print <func-print>`
    - :ref:`prompt_async <func-prompt_async>`
    - :ref:`refresh <func-refresh>`


.. _func-ListElement.create:

ListElement.create
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 380)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``ListElement``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`get <func-get>`
    - :ref:`int <func-int>`


.. _func-ListElement.on_child_close:

ListElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 388)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`isinstance <func-isinstance>`


.. _func-listen_for_keyboard:

listen_for_keyboard
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.keyboard``

**File:** :file:`src/kimi_cli/ui/shell/keyboard.py` (line 110)

**Description:**

    Listen For Keyboard.

**Returns:** ``AsyncGenerator[KeyEvent]``

**Calls:**

    - :ref:`KeyboardListener <func-KeyboardListener>`
    - :ref:`get <func-get>`
    - :ref:`start <func-start>`
    - :ref:`stop <func-stop>`


.. _func-ListItem.create:

ListItem.create
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 425)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``MarkdownElement``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`max <func-max>`


.. _func-ListItem.on_child_close:

ListItem.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 434)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`


.. _func-ListItem.render_bullet:

ListItem.render_bullet
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 438)

**Parameters:**

    - ``self``
    - ``console`` (*Console*)
    - ``options`` (*ConsoleOptions*)

**Returns:** ``RenderResult``

**Calls:**

    - :ref:`Segment <func-Segment>`
    - :ref:`_line_starts_with_list_marker <func-_line_starts_with_list_marker>`
    - :ref:`join <func-join>`
    - :ref:`len <func-len>`
    - :ref:`loop_first <func-loop_first>`
    - :ref:`lstrip <func-lstrip>`
    - :ref:`max <func-max>`
    - :ref:`render_lines <func-render_lines>`


.. _func-ListItem.render_number:

ListItem.render_number
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 464)

**Parameters:**

    - ``self``
    - ``console`` (*Console*)
    - ``options`` (*ConsoleOptions*)
    - ``number`` (*int*)
    - ``last_number`` (*int*)

**Returns:** ``RenderResult``

**Calls:**

    - :ref:`Segment <func-Segment>`
    - :ref:`_line_starts_with_list_marker <func-_line_starts_with_list_marker>`
    - :ref:`join <func-join>`
    - :ref:`len <func-len>`
    - :ref:`loop_first <func-loop_first>`
    - :ref:`lstrip <func-lstrip>`
    - :ref:`max <func-max>`
    - :ref:`render_lines <func-render_lines>`


.. _func-LLM.model_name:

LLM.model_name
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.llm``

**File:** :file:`src/kimi_cli/llm.py` (line 46)

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-LLMProvider.dump_secret:

LLMProvider.dump_secret
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 54)

**Parameters:**

    - ``self``
    - ``v`` (*SecretStr*)

**Calls:**

    - :ref:`field_serializer <func-field_serializer>`
    - :ref:`get_secret_value <func-get_secret_value>`


.. _func-load_agent:

load_agent
^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 244)

**Description:**

    Load agent from specification file.

    Raises:
        FileNotFoundError: When the agent file is not found.
        AgentSpecError(KimiCLIException, ValueError): When the agent specification is inva
    ...

**Parameters:**

    - ``agent_file`` (*Path*)
    - ``runtime`` (*Runtime*)
    - ``mcp_configs``

**Returns:** ``Agent``

**Calls:**

    - :ref:`Agent <func-Agent>`
    - :ref:`KimiToolset <func-KimiToolset>`
    - :ref:`MCPConfigError <func-MCPConfigError>`
    - :ref:`add_fixed_subagent <func-add_fixed_subagent>`
    - :ref:`append <func-append>`
    - :ref:`copy_for_fixed_subagent <func-copy_for_fixed_subagent>`
    - :ref:`debug <func-debug>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - :ref:`load_agent_spec <func-load_agent_spec>`
    - :ref:`_load_system_prompt <func-_load_system_prompt>`
    - :ref:`load_agent <func-load_agent>`
    - :ref:`load_mcp_tools <func-load_mcp_tools>`
    - :ref:`load_tools <func-load_tools>`
    - :ref:`model_validate <func-model_validate>`

**Called by:**

    - :ref:`create <func-create>` (from ``kimi_cli.app.KimiCLI``)
    - :ref:`load_agent <func-load_agent>` (from ``kimi_cli.soul.agent``)


.. _func-load_agent_spec:

load_agent_spec
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.agentspec``

**File:** :file:`src/kimi_cli/agentspec.py` (line 133)

**Description:**

    Load agent specification from file.

    Raises:
        FileNotFoundError: If the agent spec file is not found.
        AgentSpecError: If the agent spec is not valid.

**Parameters:**

    - ``agent_file`` (*Path*)

**Returns:** ``ResolvedAgentSpec``

**Calls:**

    - :ref:`AgentSpecError <func-AgentSpecError>`
    - :ref:`ResolvedAgentSpec <func-ResolvedAgentSpec>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_load_agent_spec <func-_load_agent_spec>`

**Called by:**

    - :ref:`load_agent <func-load_agent>` (from ``kimi_cli.soul.agent``)


.. _func-load_agents_md:

load_agents_md
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 78)

**Description:**

    Load Agents Md.
    
    Args:
    work\_dir: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`info <func-info>`
    - :ref:`is_file <func-is_file>`
    - :ref:`read_text <func-read_text>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)
    - :ref:`init <func-init>` (from ``kimi_cli.soul.slash``)


.. _func-load_all_sessions:

load_all_sessions
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 420)

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

    - :ref:`load_all_sessions_cached <func-load_all_sessions_cached>` (from ``kimi_cli.web.store.sessions``)


.. _func-load_all_sessions_cached:

load_all_sessions_cached
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 432)

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


.. _func-load_config:

load_config
^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 172)

**Description:**

    Load configuration from config file.
    If the config file does not exist, create it with default configuration.

    Args:
        config\_file (Path | None): Path to the configuration file. If None,
    ...

**Parameters:**

    - ``config_file`` (*Path | None*) = ``None``

**Returns:** ``Config``

**Calls:**

    - :ref:`ConfigError <func-ConfigError>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`expanduser <func-expanduser>`
    - :ref:`_migrate_json_config_to_toml <func-_migrate_json_config_to_toml>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`get_default_config <func-get_default_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`loads <func-loads>`
    - :ref:`lower <func-lower>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`read_text <func-read_text>`
    - :ref:`resolve <func-resolve>`

**Called by:**

    - :ref:`set_session_model <func-set_session_model>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`create <func-create>` (from ``kimi_cli.app.KimiCLI``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`login <func-login>` (from ``kimi_cli.cli.__init__``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.cli.__init__``)
    - :ref:`_apply_setup_result <func-_apply_setup_result>` (from ``kimi_cli.ui.shell.setup``)
    - :ref:`model <func-model>` (from ``kimi_cli.ui.shell.slash``)
    - :ref:`_build_global_config <func-_build_global_config>` (from ``kimi_cli.web.api.config``)
    - :ref:`update_global_config <func-update_global_config>` (from ``kimi_cli.web.api.config``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_encode_uploaded_files <func-_encode_uploaded_files>` (from ``kimi_cli.web.runner.process.SessionProcess``)


.. _func-load_config_from_string:

load_config_from_string
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 221)

**Description:**

    Load configuration from a TOML or JSON string.

    Args:
        config\_string (str): TOML or JSON configuration text.

    Returns:
        Validated Config object.

    Raises:
        ConfigError:
    ...

**Parameters:**

    - ``config_string`` (*str*)

**Returns:** ``Config``

**Calls:**

    - :ref:`ConfigError <func-ConfigError>`
    - :ref:`loads <func-loads>`
    - :ref:`model_validate <func-model_validate>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`update_config_toml <func-update_config_toml>` (from ``kimi_cli.web.api.config``)


.. _func-load_desc:

load_desc
^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 50)

**Description:**

    Load a tool description from a file, rendered via Jinja2.

**Parameters:**

    - ``path`` (*Path*)
    - ``context`` = ``None``

**Returns:** ``str``

**Calls:**

    - :ref:`Environment <func-Environment>`
    - :ref:`from_string <func-from_string>`
    - :ref:`read_text <func-read_text>`
    - :ref:`render <func-render>`

**Called by:**

    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.tools.file.read.ReadFile``)
    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.tools.file.read_media.ReadMediaFile``)
    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.tools.multiagent.task.Task``)
    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.tools.shell.__init__.Shell``)


.. _func-load_metadata:

load_metadata
^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 75)

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

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`continue_ <func-continue_>` (from ``kimi_cli.session.Session``)
    - :ref:`create <func-create>` (from ``kimi_cli.session.Session``)
    - :ref:`find <func-find>` (from ``kimi_cli.session.Session``)
    - :ref:`list <func-list>` (from ``kimi_cli.session.Session``)
    - :ref:`_get_work_dirs_sync <func-_get_work_dirs_sync>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_update_last_session_id <func-_update_last_session_id>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`delete_session <func-delete_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_build_sessions_index <func-_build_sessions_index>` (from ``kimi_cli.web.store.sessions``)
    - :ref:`load_session_by_id <func-load_session_by_id>` (from ``kimi_cli.web.store.sessions``)


.. _func-load_session_by_id:

load_session_by_id
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 504)

**Description:**

    Load a session by ID.

    This function first checks the cache/disk scan, then falls back to
    directly constructing the session from metadata if not found (handles
    newly created sessions with 
    ...

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

    - :ref:`get_editable_session <func-get_editable_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_session <func-get_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_session_file <func-get_session_file>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_session_git_diff <func-get_session_git_diff>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`get_session_upload_file <func-get_session_upload_file>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`update_session <func-update_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_encode_uploaded_files <func-_encode_uploaded_files>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`run_worker <func-run_worker>` (from ``kimi_cli.web.runner.worker``)


.. _func-load_session_metadata:

load_session_metadata
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 121)

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

    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`update_session <func-update_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_build_sessions_index <func-_build_sessions_index>` (from ``kimi_cli.web.store.sessions``)
    - :ref:`_ensure_title <func-_ensure_title>` (from ``kimi_cli.web.store.sessions``)
    - :ref:`load_session_by_id <func-load_session_by_id>` (from ``kimi_cli.web.store.sessions``)


.. _func-load_sessions_page:

load_sessions_page
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 451)

**Description:**

    Load a paginated list of sessions, optionally filtered by query and archived status.

    Args:
        limit: Maximum number of sessions to return.
        offset: Number of sessions to skip.
       
    ...

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

    - :ref:`list_sessions <func-list_sessions>` (from ``kimi_cli.web.api.sessions``)


.. _func-load_tokens:

load_tokens
^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 390)

**Description:**

    Load Tokens.
    
    Args:
    ref: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)

**Returns:** ``OAuthToken | None``

**Calls:**

    - :ref:`_delete_from_keyring <func-_delete_from_keyring>`
    - :ref:`_load_from_file <func-_load_from_file>`
    - :ref:`_load_from_keyring <func-_load_from_keyring>`
    - :ref:`_save_to_file <func-_save_to_file>`
    - :ref:`suppress <func-suppress>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`_load_initial_tokens <func-_load_initial_tokens>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`_migrate_oauth_storage <func-_migrate_oauth_storage>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`_refresh_tokens <func-_refresh_tokens>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`ensure_fresh <func-ensure_fresh>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`resolve_api_key <func-resolve_api_key>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)


.. _func-LocalFileMentionCompleter.get_completions:

LocalFileMentionCompleter.get_completions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 470)

**Parameters:**

    - ``self``
    - ``document`` (*Document*)
    - ``complete_event`` (*CompleteEvent*)

**Returns:** ``Iterable[Completion]``

**Calls:**

    - :ref:`Document <func-Document>`
    - :ref:`_extract_fragment <func-_extract_fragment>`
    - :ref:`_is_completed_file <func-_is_completed_file>`
    - :ref:`get_completions <func-get_completions>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`lower <func-lower>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`sort <func-sort>`
    - :ref:`split <func-split>`
    - :ref:`startswith <func-startswith>`


.. _func-login:

login
^^^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 85)

**Description:**

    Login to your Kimi account.

**Parameters:**

    - ``json`` (*bool*)

**Returns:** ``None``

**Calls:**

    - :ref:`Console <func-Console>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`_run <func-_run>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`login_kimi_code <func-login_kimi_code>`
    - :ref:`load_config <func-load_config>`
    - :ref:`print <func-print>`
    - :ref:`run <func-run>`
    - :ref:`start <func-start>`
    - :ref:`status <func-status>`
    - :ref:`stop <func-stop>`


.. _func-login:

login
^^^^^

**Module:** ``kimi_cli.ui.shell.oauth``

**File:** :file:`src/kimi_cli/ui/shell/oauth.py` (line 106)

**Description:**

    Login or setup a platform.

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`_login_kimi_code <func-_login_kimi_code>`
    - :ref:`select_platform <func-select_platform>`
    - :ref:`setup_platform <func-setup_platform>`
    - :ref:`clear <func-clear>`
    - :ref:`sleep <func-sleep>`


.. _func-login_kimi_code:

login_kimi_code
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 617)

**Description:**

    Login Kimi Code.
    
    Args:
    config: Description.
    open\_browser: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)
    - ``open_browser`` (*bool*) = ``True``

**Returns:** ``AsyncIterator[OAuthEvent]``

**Calls:**

    - :ref:`OAuthDeviceExpired <func-OAuthDeviceExpired>`
    - :ref:`OAuthEvent <func-OAuthEvent>`
    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`error <func-error>`
    - :ref:`from_response <func-from_response>`
    - :ref:`get <func-get>`
    - :ref:`_apply_kimi_code_config <func-_apply_kimi_code_config>`
    - :ref:`_request_device_token <func-_request_device_token>`
    - :ref:`_select_default_model_and_thinking <func-_select_default_model_and_thinking>`
    - :ref:`request_device_authorization <func-request_device_authorization>`
    - :ref:`save_tokens <func-save_tokens>`
    - :ref:`get_platform_by_id <func-get_platform_by_id>`
    - :ref:`list_models <func-list_models>`
    - :ref:`save_config <func-save_config>`
    - :ref:`max <func-max>`
    - :ref:`open <func-open>`
    - :ref:`sleep <func-sleep>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`login <func-login>` (from ``kimi_cli.cli.__init__``)
    - :ref:`_login_kimi_code <func-_login_kimi_code>` (from ``kimi_cli.ui.shell.oauth``)


.. _func-logout:

logout
^^^^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 44)

**Description:**

    Logout from your Kimi account.

**Parameters:**

    - ``json`` (*bool*)

**Returns:** ``None``

**Calls:**

    - :ref:`Console <func-Console>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`_run <func-_run>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`logout_kimi_code <func-logout_kimi_code>`
    - :ref:`load_config <func-load_config>`
    - :ref:`print <func-print>`
    - :ref:`run <func-run>`


.. _func-logout:

logout
^^^^^^

**Module:** ``kimi_cli.ui.shell.oauth``

**File:** :file:`src/kimi_cli/ui/shell/oauth.py` (line 125)

**Description:**

    Logout from the current platform.

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`get <func-get>`
    - :ref:`items <func-items>`
    - :ref:`logout_kimi_code <func-logout_kimi_code>`
    - :ref:`is_managed_provider_key <func-is_managed_provider_key>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`
    - :ref:`save_config <func-save_config>`
    - :ref:`_current_model_key <func-_current_model_key>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`clear <func-clear>`
    - :ref:`list <func-list>`
    - :ref:`print <func-print>`
    - :ref:`sleep <func-sleep>`


.. _func-logout_kimi_code:

logout_kimi_code
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 732)

**Description:**

    Logout Kimi Code.
    
    Args:
    config: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)

**Returns:** ``AsyncIterator[OAuthEvent]``

**Calls:**

    - :ref:`OAuthEvent <func-OAuthEvent>`
    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`items <func-items>`
    - :ref:`delete_tokens <func-delete_tokens>`
    - :ref:`managed_provider_key <func-managed_provider_key>`
    - :ref:`save_config <func-save_config>`
    - :ref:`list <func-list>`

**Called by:**

    - :ref:`logout <func-logout>` (from ``kimi_cli.cli.__init__``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.ui.shell.oauth``)



M
-

.. _func-main:

main
^^^^

**Module:** ``kimi_cli.web.runner.worker``

**File:** :file:`src/kimi_cli/web/runner/worker.py` (line 59)

**Description:**

    Entry point for the worker subprocess.

**Returns:** ``None``

**Calls:**

    - :ref:`UUID <func-UUID>`
    - :ref:`exit <func-exit>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`run_worker <func-run_worker>`
    - :ref:`len <func-len>`
    - :ref:`print <func-print>`


.. _func-managed_model_key:

managed_model_key
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 140)

**Description:**

    Managed Model Key.
    
    Args:
    platform\_id: Description.
    model\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)
    - ``model_id`` (*str*)

**Returns:** ``str``

**Called by:**

    - :ref:`_apply_kimi_code_config <func-_apply_kimi_code_config>` (from ``kimi_cli.auth.oauth``)
    - :ref:`_apply_models <func-_apply_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`_apply_setup_result <func-_apply_setup_result>` (from ``kimi_cli.ui.shell.setup``)


.. _func-managed_provider_key:

managed_provider_key
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 128)

**Description:**

    Managed Provider Key.
    
    Args:
    platform\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform_id`` (*str*)

**Returns:** ``str``

**Called by:**

    - :ref:`_apply_access_token <func-_apply_access_token>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`_kimi_code_ref <func-_kimi_code_ref>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`_apply_kimi_code_config <func-_apply_kimi_code_config>` (from ``kimi_cli.auth.oauth``)
    - :ref:`logout_kimi_code <func-logout_kimi_code>` (from ``kimi_cli.auth.oauth``)
    - :ref:`_apply_setup_result <func-_apply_setup_result>` (from ``kimi_cli.ui.shell.setup``)


.. _func-MarkdownContext.current_style:

MarkdownContext.current_style
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 566)

**Description:**

    Current style which is the product of all styles on the stack.

**Parameters:**

    - ``self``

**Returns:** ``Style``


.. _func-MarkdownContext.enter_style:

MarkdownContext.enter_style
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 581)

**Description:**

    Enter a style context.

**Parameters:**

    - ``self``
    - ``style_name`` (*str | Style*)

**Returns:** ``Style``

**Calls:**

    - :ref:`Style <func-Style>`
    - :ref:`copy <func-copy>`
    - :ref:`get_style <func-get_style>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`push <func-push>`


.. _func-MarkdownContext.leave_style:

MarkdownContext.leave_style
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 601)

**Description:**

    Leave a style context.

**Parameters:**

    - ``self``

**Returns:** ``Style``

**Calls:**

    - :ref:`pop <func-pop>`


.. _func-MarkdownContext.on_text:

MarkdownContext.on_text
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 570)

**Description:**

    Called when the parser visits text.

**Parameters:**

    - ``self``
    - ``text`` (*str*)
    - ``node_type`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`assemble <func-assemble>`
    - :ref:`highlight <func-highlight>`
    - :ref:`_strip_background <func-_strip_background>`
    - :ref:`on_text <func-on_text>`
    - :ref:`rstrip <func-rstrip>`


.. _func-MarkdownElement.create:

MarkdownElement.create
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 30)

**Description:**

    Factory to create markdown element,

        Args:
            markdown (Markdown): The parent Markdown object.
            token (Token): A node from markdown-it.

        Returns:
            Markdo
    ...

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``MarkdownElement``

**Calls:**

    - :ref:`cls <func-cls>`


.. _func-MarkdownElement.on_child_close:

MarkdownElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 63)

**Description:**

    Called when a child element is closed.

        This method allows a parent element to take over rendering of its children.

        Args:
            context (MarkdownContext): The markdown context.

    ...

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``


.. _func-MarkdownElement.on_enter:

MarkdownElement.on_enter
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 42)

**Description:**

    Called when the node is entered.

        Args:
            context (MarkdownContext): The markdown context.

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``


.. _func-MarkdownElement.on_leave:

MarkdownElement.on_leave
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 56)

**Description:**

    Called when the parser leaves the element.

        Args:
            context (MarkdownContext): [description]

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``


.. _func-MarkdownElement.on_text:

MarkdownElement.on_text
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 49)

**Description:**

    Called when text is parsed.

        Args:
            context (MarkdownContext): The markdown context.

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``text`` (*TextType*)

**Returns:** ``None``


.. _func-mcp:

mcp
^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 366)

**Description:**

    Show MCP servers and tools

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`BulletColumns <func-BulletColumns>`
    - :ref:`Group <func-Group>`
    - :ref:`append <func-append>`
    - :ref:`from_markup <func-from_markup>`
    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`items <func-items>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`len <func-len>`
    - :ref:`print <func-print>`
    - :ref:`sum <func-sum>`
    - :ref:`values <func-values>`


.. _func-mcp_add:

mcp_add
^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 109)

**Description:**

    Add an MCP server.

**Parameters:**

    - ``name``
    - ``server_args`` = ``None``
    - ``transport`` = ``'stdio'``
    - ``env`` = ``None``
    - ``header`` = ``None``
    - ``auth`` = ``None``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Exit <func-Exit>`
    - :ref:`Option <func-Option>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`_parse_key_value_pairs <func-_parse_key_value_pairs>`
    - :ref:`_save_mcp_config <func-_save_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`len <func-len>`
    - :ref:`strip <func-strip>`


.. _func-mcp_auth:

mcp_auth
^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 265)

**Description:**

    Authorize with an OAuth-enabled MCP server.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Client <func-Client>`
    - :ref:`Exit <func-Exit>`
    - :ref:`_auth <func-_auth>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`len <func-len>`
    - :ref:`list_tools <func-list_tools>`
    - :ref:`run <func-run>`
    - :ref:`type <func-type>`


.. _func-mcp_list:

mcp_list
^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 237)

**Description:**

    List all MCP servers.

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`items <func-items>`
    - :ref:`join <func-join>`
    - :ref:`_has_oauth_tokens <func-_has_oauth_tokens>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`rstrip <func-rstrip>`


.. _func-mcp_remove:

mcp_remove
^^^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 207)

**Description:**

    Remove an MCP server.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`_load_mcp_config <func-_load_mcp_config>`
    - :ref:`_save_mcp_config <func-_save_mcp_config>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`


.. _func-mcp_reset_auth:

mcp_reset_auth
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 298)

**Description:**

    Reset OAuth authorization for an MCP server (clear cached tokens).

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Exit <func-Exit>`
    - :ref:`FileTokenStorage <func-FileTokenStorage>`
    - :ref:`clear <func-clear>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`type <func-type>`


.. _func-mcp_test:

mcp_test
^^^^^^^^

**Module:** ``kimi_cli.cli.mcp``

**File:** :file:`src/kimi_cli/cli/mcp.py` (line 321)

**Description:**

    Test connection to an MCP server and list available tools.

**Parameters:**

    - ``name``

**Calls:**

    - :ref:`Argument <func-Argument>`
    - :ref:`Client <func-Client>`
    - :ref:`Exit <func-Exit>`
    - :ref:`_test <func-_test>`
    - :ref:`command <func-command>`
    - :ref:`echo <func-echo>`
    - :ref:`_get_mcp_server <func-_get_mcp_server>`
    - :ref:`len <func-len>`
    - :ref:`list_tools <func-list_tools>`
    - :ref:`run <func-run>`
    - :ref:`type <func-type>`


.. _func-message_stringify:

message_stringify
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.message``

**File:** :file:`src/kimi_cli/utils/message.py` (line 5)

**Description:**

    Get a string representation of a message.

**Parameters:**

    - ``message`` (*Message*)

**Returns:** ``str``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`join <func-join>`

**Called by:**

    - :ref:`replay_recent_history <func-replay_recent_history>` (from ``kimi_cli.ui.shell.replay``)
    - :ref:`dispatch_wire_message <func-dispatch_wire_message>` (from ``kimi_cli.ui.shell.visualize._LiveView``)


.. _func-Metadata.get_work_dir_meta:

Metadata.get_work_dir_meta
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 62)

**Description:**

    Get the metadata for a work directory.

**Parameters:**

    - ``self``
    - ``path`` (*KaosPath*)

**Returns:** ``WorkDirMeta | None``

**Calls:**

    - :ref:`get_current_kaos <func-get_current_kaos>`
    - :ref:`str <func-str>`


.. _func-Metadata.new_work_dir_meta:

Metadata.new_work_dir_meta
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 69)

**Description:**

    Create a new work directory metadata.

**Parameters:**

    - ``self``
    - ``path`` (*KaosPath*)

**Returns:** ``WorkDirMeta``

**Calls:**

    - :ref:`WorkDirMeta <func-WorkDirMeta>`
    - :ref:`append <func-append>`
    - :ref:`get_current_kaos <func-get_current_kaos>`
    - :ref:`str <func-str>`


.. _func-model:

model
^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 140)

**Description:**

    Switch LLM model or thinking mode

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`ChoiceInput <func-ChoiceInput>`
    - :ref:`Reload <func-Reload>`
    - :ref:`append <func-append>`
    - :ref:`items <func-items>`
    - :ref:`get_platform_name_for_provider <func-get_platform_name_for_provider>`
    - :ref:`refresh_managed_models <func-refresh_managed_models>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`derive_model_capabilities <func-derive_model_capabilities>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`
    - :ref:`print <func-print>`
    - :ref:`prompt_async <func-prompt_async>`
    - :ref:`sorted <func-sorted>`


.. _func-model_display_name:

model_display_name
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.llm``

**File:** :file:`src/kimi_cli/llm.py` (line 93)

**Description:**

    Model Display Name.
    
    Args:
    model\_name: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``model_name`` (*str | None*)

**Returns:** ``str``

**Called by:**

    - :ref:`run_shell <func-run_shell>` (from ``kimi_cli.app.KimiCLI``)


.. _func-ModelInfo.capabilities:

ModelInfo.capabilities
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 24)

**Description:**

    Derive capabilities from model info.

**Parameters:**

    - ``self``

**Returns:** ``set[ModelCapability]``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`lower <func-lower>`
    - :ref:`set <func-set>`
    - :ref:`update <func-update>`


.. _func-MoonshotFetchConfig.dump_secret:

MoonshotFetchConfig.dump_secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 100)

**Parameters:**

    - ``self``
    - ``v`` (*SecretStr*)

**Calls:**

    - :ref:`field_serializer <func-field_serializer>`
    - :ref:`get_secret_value <func-get_secret_value>`


.. _func-MoonshotSearchConfig.dump_secret:

MoonshotSearchConfig.dump_secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 116)

**Parameters:**

    - ``self``
    - ``v`` (*SecretStr*)

**Calls:**

    - :ref:`field_serializer <func-field_serializer>`
    - :ref:`get_secret_value <func-get_secret_value>`



N
-

.. _func-new_client_session:

new_client_session
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.aiohttp``

**File:** :file:`src/kimi_cli/utils/aiohttp.py` (line 23)

**Description:**

    New Client Session.

**Returns:** ``aiohttp.ClientSession``

**Calls:**

    - :ref:`ClientSession <func-ClientSession>`
    - :ref:`TCPConnector <func-TCPConnector>`

**Called by:**

    - :ref:`_request_device_token <func-_request_device_token>` (from ``kimi_cli.auth.oauth``)
    - :ref:`refresh_token <func-refresh_token>` (from ``kimi_cli.auth.oauth``)
    - :ref:`request_device_authorization <func-request_device_authorization>` (from ``kimi_cli.auth.oauth``)
    - :ref:`list_models <func-list_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`_download_and_install_rg <func-_download_and_install_rg>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`_fetch_with_service <func-_fetch_with_service>` (from ``kimi_cli.tools.web.fetch.FetchURL``)
    - :ref:`fetch_with_http_get <func-fetch_with_http_get>` (from ``kimi_cli.tools.web.fetch.FetchURL``)
    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.web.search.SearchWeb``)
    - :ref:`_do_update <func-_do_update>` (from ``kimi_cli.ui.shell.update``)
    - :ref:`_fetch_usage <func-_fetch_usage>` (from ``kimi_cli.ui.shell.usage``)


.. _func-new_history_complete_message:

new_history_complete_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.messages``

**File:** :file:`src/kimi_cli/web/runner/messages.py` (line 43)

**Description:**

    Create a new history complete message.

**Returns:** ``JSONRPCHistoryCompleteMessage``

**Calls:**

    - :ref:`JSONRPCHistoryCompleteMessage <func-JSONRPCHistoryCompleteMessage>`
    - :ref:`str <func-str>`
    - :ref:`uuid4 <func-uuid4>`

**Called by:**

    - :ref:`send_history_complete <func-send_history_complete>` (from ``kimi_cli.web.runner.messages``)


.. _func-new_session_status_message:

new_session_status_message
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.messages``

**File:** :file:`src/kimi_cli/web/runner/messages.py` (line 47)

**Description:**

    Create a new session status message.

**Parameters:**

    - ``status`` (*SessionStatus*)

**Returns:** ``JSONRPCSessionStatusMessage``

**Calls:**

    - :ref:`JSONRPCSessionStatusMessage <func-JSONRPCSessionStatusMessage>`

**Called by:**

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_emit_status <func-_emit_status>` (from ``kimi_cli.web.runner.process.SessionProcess``)
    - :ref:`send_status_snapshot <func-send_status_snapshot>` (from ``kimi_cli.web.runner.process.SessionProcess``)


.. _func-next_available_rotation:

next_available_rotation
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.path``

**File:** :file:`src/kimi_cli/utils/path.py` (line 100)

**Description:**

    Return a reserved rotation path for \*path\* or \`\`None\`\` if parent is missing.

    The caller must overwrite/reuse the returned path immediately because this helper
    commits an empty placeholder fil
    ...

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

    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`revert_to <func-revert_to>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`_get_subagent_context_file <func-_get_subagent_context_file>` (from ``kimi_cli.tools.multiagent.task.Task``)


.. _func-normalize_allowed_origins:

normalize_allowed_origins
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 87)

**Description:**

    Parse comma-separated origins into a normalized list.

**Parameters:**

    - ``value`` (*str | None*)

**Returns:** ``list[str]``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`split <func-split>`

**Called by:**

    - :ref:`create_app <func-create_app>` (from ``kimi_cli.web.app``)
    - :ref:`run_web_server <func-run_web_server>` (from ``kimi_cli.web.app``)


.. _func-normalize_skill_name:

normalize_skill_name
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 134)

**Description:**

    Normalize a skill name for lookup.

**Parameters:**

    - ``name`` (*str*)

**Returns:** ``str``

**Calls:**

    - :ref:`casefold <func-casefold>`

**Called by:**

    - :ref:`discover_skills_from_roots <func-discover_skills_from_roots>` (from ``kimi_cli.skill.__init__``)
    - :ref:`index_skills <func-index_skills>` (from ``kimi_cli.skill.__init__``)



O
-

.. _func-OAuthEvent.json:

OAuthEvent.json
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 134)

**Parameters:**

    - ``self``

**Returns:** ``str``

**Calls:**

    - :ref:`dumps <func-dumps>`


.. _func-OAuthManager.common_headers:

OAuthManager.common_headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 839)

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`_common_headers <func-_common_headers>`


.. _func-OAuthManager.ensure_fresh:

OAuthManager.ensure_fresh
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 867)

**Parameters:**

    - ``self``
    - ``runtime`` (*Runtime*)

**Returns:** ``None``

**Calls:**

    - :ref:`_apply_access_token <func-_apply_access_token>`
    - :ref:`_cache_access_token <func-_cache_access_token>`
    - :ref:`_kimi_code_ref <func-_kimi_code_ref>`
    - :ref:`_refresh_tokens <func-_refresh_tokens>`
    - :ref:`load_tokens <func-load_tokens>`


.. _func-OAuthManager.refreshing:

OAuthManager.refreshing
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 879)

**Parameters:**

    - ``self``
    - ``runtime`` (*Runtime*)

**Returns:** ``AsyncIterator[None]``

**Calls:**

    - :ref:`Event <func-Event>`
    - :ref:`_runner <func-_runner>`
    - :ref:`cancel <func-cancel>`
    - :ref:`create_task <func-create_task>`
    - :ref:`ensure_fresh <func-ensure_fresh>`
    - :ref:`set <func-set>`
    - :ref:`suppress <func-suppress>`
    - :ref:`wait_for <func-wait_for>`
    - :ref:`warning <func-warning>`


.. _func-OAuthManager.resolve_api_key:

OAuthManager.resolve_api_key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 842)

**Parameters:**

    - ``self``
    - ``api_key`` (*SecretStr*)
    - ``oauth`` (*OAuthRef | None*)

**Returns:** ``str``

**Calls:**

    - :ref:`_cache_access_token <func-_cache_access_token>`
    - :ref:`get <func-get>`
    - :ref:`get_secret_value <func-get_secret_value>`
    - :ref:`load_tokens <func-load_tokens>`


.. _func-OAuthToken.from_dict:

OAuthToken.from_dict
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 172)

**Parameters:**

    - ``cls``
    - ``payload``

**Returns:** ``OAuthToken``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`float <func-float>`
    - :ref:`get <func-get>`
    - :ref:`str <func-str>`


.. _func-OAuthToken.from_response:

OAuthToken.from_response
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 152)

**Parameters:**

    - ``cls``
    - ``payload``

**Returns:** ``OAuthToken``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`float <func-float>`
    - :ref:`str <func-str>`
    - :ref:`time <func-time>`


.. _func-OAuthToken.to_dict:

OAuthToken.to_dict
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 162)

**Parameters:**

    - ``self``


.. _func-open_in:

open_in
^^^^^^^

**Module:** ``kimi_cli.web.api.open_in``

**File:** :file:`src/kimi_cli/web/api/open_in.py` (line 141)

**Description:**

    Open In.
    
    Args:
    request: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``request`` (*OpenInRequest*)

**Returns:** ``OpenInResponse``

**Calls:**

    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`OpenInResponse <func-OpenInResponse>`
    - :ref:`is_file <func-is_file>`
    - :ref:`_open_app <func-_open_app>`
    - :ref:`_open_iterm <func-_open_iterm>`
    - :ref:`_open_terminal <func-_open_terminal>`
    - :ref:`_resolve_path <func-_resolve_path>`
    - :ref:`_run_command <func-_run_command>`
    - :ref:`post <func-post>`
    - :ref:`str <func-str>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`


.. _func-open_original_stderr:

open_original_stderr
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 113)

**Description:**

    Open Original Stderr.

**Returns:** ``Iterator[IO[bytes] | None]``

**Calls:**

    - :ref:`close <func-close>`
    - :ref:`open_original_stderr_handle <func-open_original_stderr_handle>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)



P
-

.. _func-Paragraph.create:

Paragraph.create
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 181)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``Paragraph``

**Calls:**

    - :ref:`cls <func-cls>`


.. _func-parse_bearer_token:

parse_bearer_token
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 77)

**Description:**

    Extract bearer token from Authorization header.

**Parameters:**

    - ``value`` (*str | None*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`lower <func-lower>`
    - :ref:`partition <func-partition>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`extract_token_from_request <func-extract_token_from_request>` (from ``kimi_cli.web.auth``)


.. _func-parse_changelog:

parse_changelog
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.changelog``

**File:** :file:`src/kimi_cli/utils/changelog.py` (line 36)

**Description:**

    Parse a subset of Keep a Changelog-style markdown into a map:
    version -> (description, entries)

    Parsing rules:
    - Versions are denoted by level-2 headings starting with '## ['
      Exampl
    ...

**Parameters:**

    - ``md_text`` (*str*)

**Calls:**

    - :ref:`ReleaseEntry <func-ReleaseEntry>`
    - :ref:`append <func-append>`
    - :ref:`commit <func-commit>`
    - :ref:`find <func-find>`
    - :ref:`join <func-join>`
    - :ref:`lstrip <func-lstrip>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`startswith <func-startswith>`


.. _func-parse_choice:

parse_choice
^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.flow.__init__``

**File:** :file:`src/kimi_cli/skill/flow/__init__.py` (line 118)

**Description:**

    Parse Choice.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`findall <func-findall>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`_execute_flow_node <func-_execute_flow_node>` (from ``kimi_cli.soul.kimisoul.FlowRunner``)


.. _func-parse_d2_flowchart:

parse_d2_flowchart
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.flow.d2``

**File:** :file:`src/kimi_cli/skill/flow/d2.py` (line 90)

**Description:**

    Parse D2 Flowchart.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``Flow``

**Calls:**

    - :ref:`Flow <func-Flow>`
    - :ref:`items <func-items>`
    - :ref:`_has_unquoted_token <func-_has_unquoted_token>`
    - :ref:`_infer_decision_nodes <func-_infer_decision_nodes>`
    - :ref:`_iter_top_level_statements <func-_iter_top_level_statements>`
    - :ref:`_normalize_markdown_blocks <func-_normalize_markdown_blocks>`
    - :ref:`_parse_edge_statement <func-_parse_edge_statement>`
    - :ref:`_parse_node_statement <func-_parse_node_statement>`
    - :ref:`setdefault <func-setdefault>`
    - :ref:`validate_flow <func-validate_flow>`


.. _func-parse_frontmatter:

parse_frontmatter
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.frontmatter``

**File:** :file:`src/kimi_cli/utils/frontmatter.py` (line 6)

**Description:**

    Parse YAML frontmatter from a text blob.

    Raises:
        ValueError: If the frontmatter YAML is invalid.

**Parameters:**

    - ``text`` (*str*)

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`append <func-append>`
    - :ref:`cast <func-cast>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`join <func-join>`
    - :ref:`safe_load <func-safe_load>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`parse_skill_text <func-parse_skill_text>` (from ``kimi_cli.skill.__init__``)
    - :ref:`read_frontmatter <func-read_frontmatter>` (from ``kimi_cli.utils.frontmatter``)


.. _func-parse_managed_provider_key:

parse_managed_provider_key
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 153)

**Description:**

    Parse Managed Provider Key.
    
    Args:
    provider\_key: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``provider_key`` (*str*)

**Returns:** ``str | None``

**Calls:**

    - :ref:`removeprefix <func-removeprefix>`
    - :ref:`startswith <func-startswith>`

**Called by:**

    - :ref:`get_platform_name_for_provider <func-get_platform_name_for_provider>` (from ``kimi_cli.auth.platforms``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.ui.shell.oauth``)
    - :ref:`_usage_url <func-_usage_url>` (from ``kimi_cli.ui.shell.usage``)


.. _func-parse_mermaid_flowchart:

parse_mermaid_flowchart
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.flow.mermaid``

**File:** :file:`src/kimi_cli/skill/flow/mermaid.py` (line 79)

**Description:**

    Parse Mermaid Flowchart.
    
    Args:
    text: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``text`` (*str*)

**Returns:** ``Flow``

**Calls:**

    - :ref:`Flow <func-Flow>`
    - :ref:`FlowEdge <func-FlowEdge>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`items <func-items>`
    - :ref:`_add_node <func-_add_node>`
    - :ref:`_infer_decision_nodes <func-_infer_decision_nodes>`
    - :ref:`_is_style_line <func-_is_style_line>`
    - :ref:`_strip_comment <func-_strip_comment>`
    - :ref:`_strip_style_tokens <func-_strip_style_tokens>`
    - :ref:`_try_parse_edge_line <func-_try_parse_edge_line>`
    - :ref:`_try_parse_node_line <func-_try_parse_node_line>`
    - :ref:`match <func-match>`
    - :ref:`setdefault <func-setdefault>`
    - :ref:`splitlines <func-splitlines>`
    - :ref:`startswith <func-startswith>`
    - :ref:`validate_flow <func-validate_flow>`


.. _func-parse_skill_text:

parse_skill_text
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 196)

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

    - :ref:`discover_skills <func-discover_skills>` (from ``kimi_cli.skill.__init__``)


.. _func-parse_slash_command_call:

parse_slash_command_call
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.slashcmd``

**File:** :file:`src/kimi_cli/utils/slashcmd.py` (line 31)

**Description:**

    Parse a slash command call from user input.

    Returns:
        SlashCommandCall if a slash command is found, else None. The \`args\` field contains
        the raw argument string after the command n
    ...

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

    - :ref:`run <func-run>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_run_shell_command <func-_run_shell_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_is_clear_command_input <func-_is_clear_command_input>` (from ``kimi_cli.ui.shell.replay``)


.. _func-parse_wire_file_line:

parse_wire_file_line
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 72)

**Description:**

    Parse a wire file line into metadata or a message record.

**Parameters:**

    - ``line`` (*str*)

**Returns:** ``WireFileMetadata | WireMessageRecord``

**Calls:**

    - :ref:`parse_wire_file_metadata <func-parse_wire_file_metadata>`
    - :ref:`model_validate_json <func-model_validate_json>`

**Called by:**

    - :ref:`iter_records <func-iter_records>` (from ``kimi_cli.wire.file.WireFile``)


.. _func-parse_wire_file_metadata:

parse_wire_file_metadata
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 65)

**Description:**

    Parse a wire file metadata line; return None if the line is not metadata.

**Parameters:**

    - ``line`` (*str*)

**Returns:** ``WireFileMetadata | None``

**Calls:**

    - :ref:`model_validate_json <func-model_validate_json>`

**Called by:**

    - :ref:`is_empty <func-is_empty>` (from ``kimi_cli.wire.file.WireFile``)
    - :ref:`_load_protocol_version <func-_load_protocol_version>` (from ``kimi_cli.wire.file``)
    - :ref:`parse_wire_file_line <func-parse_wire_file_line>` (from ``kimi_cli.wire.file``)


.. _func-Print.run:

Print.run
^^^^^^^^^

**Module:** ``kimi_cli.ui.print.__init__``

**File:** :file:`src/kimi_cli/ui/print/__init__.py` (line 51)

**Parameters:**

    - ``self``
    - ``command`` (*str | None*) = ``None``

**Returns:** ``bool``

**Calls:**

    - :ref:`Event <func-Event>`
    - :ref:`_read_next_command <func-_read_next_command>`
    - :ref:`debug <func-debug>`
    - :ref:`error <func-error>`
    - :ref:`exception <func-exception>`
    - :ref:`get_running_loop <func-get_running_loop>`
    - :ref:`info <func-info>`
    - :ref:`isatty <func-isatty>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`install_sigint_handler <func-install_sigint_handler>`
    - :ref:`partial <func-partial>`
    - :ref:`print <func-print>`
    - :ref:`remove_sigint <func-remove_sigint>`
    - :ref:`run_soul <func-run_soul>`
    - :ref:`set <func-set>`
    - :ref:`strip <func-strip>`
    - :ref:`warning <func-warning>`


.. _func-Printer.feed:

Printer.feed
^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 23)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``


.. _func-Printer.flush:

Printer.flush
^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 24)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-PromptMode.toggle:

PromptMode.toggle
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 78)

**Parameters:**

    - ``self``

**Returns:** ``PromptMode``



R
-

.. _func-random_string:

random_string
^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.string``

**File:** :file:`src/kimi_cli/utils/string.py` (line 6)

**Description:**

    Generate a random string of fixed length.

**Parameters:**

    - ``length`` (*int*) = ``8``

**Returns:** ``str``

**Calls:**

    - :ref:`choice <func-choice>`
    - :ref:`join <func-join>`
    - :ref:`range <func-range>`

**Called by:**

    - :ref:`_reserve_id <func-_reserve_id>` (from ``kimi_cli.ui.shell.prompt.AttachmentCache``)


.. _func-read_frontmatter:

read_frontmatter
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.frontmatter``

**File:** :file:`src/kimi_cli/utils/frontmatter.py` (line 39)

**Description:**

    Read the YAML frontmatter at the start of a file.

    Args:
        path: Path to an existing file that may contain frontmatter.

**Parameters:**

    - ``path`` (*Path*)

**Calls:**

    - :ref:`parse_frontmatter <func-parse_frontmatter>`
    - :ref:`read_text <func-read_text>`


.. _func-read_skill_text:

read_skill_text
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 152)

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

    - :ref:`_make_skill_runner <func-_make_skill_runner>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)


.. _func-redirect_stderr_to_logger:

redirect_stderr_to_logger
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 97)

**Description:**

    Redirect Stderr To Logger.
    
    Args:
    level: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``level`` (*str*) = ``'ERROR'``

**Returns:** ``None``

**Calls:**

    - :ref:`StderrRedirector <func-StderrRedirector>`
    - :ref:`install <func-install>`

**Called by:**

    - :ref:`enable_logging <func-enable_logging>` (from ``kimi_cli.app``)
    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)


.. _func-refresh_managed_models:

refresh_managed_models
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.platforms``

**File:** :file:`src/kimi_cli/auth/platforms.py` (line 195)

**Description:**

    Refresh Managed Models.
    
    Args:
    config: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``config`` (*Config*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`error <func-error>`
    - :ref:`get_secret_value <func-get_secret_value>`
    - :ref:`items <func-items>`
    - :ref:`load_tokens <func-load_tokens>`
    - :ref:`_apply_models <func-_apply_models>`
    - :ref:`get_platform_by_id <func-get_platform_by_id>`
    - :ref:`is_managed_provider_key <func-is_managed_provider_key>`
    - :ref:`list_models <func-list_models>`
    - :ref:`parse_managed_provider_key <func-parse_managed_provider_key>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`model <func-model>` (from ``kimi_cli.ui.shell.slash``)


.. _func-refresh_token:

refresh_token
^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 507)

**Description:**

    Refresh Token.
    
    Args:
    refresh\_token: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``refresh_token`` (*str*)

**Returns:** ``OAuthToken``

**Calls:**

    - :ref:`OAuthError <func-OAuthError>`
    - :ref:`OAuthUnauthorized <func-OAuthUnauthorized>`
    - :ref:`from_response <func-from_response>`
    - :ref:`get <func-get>`
    - :ref:`json <func-json>`
    - :ref:`_common_headers <func-_common_headers>`
    - :ref:`_oauth_host <func-_oauth_host>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`post <func-post>`
    - :ref:`rstrip <func-rstrip>`

**Called by:**

    - :ref:`_refresh_tokens <func-_refresh_tokens>` (from ``kimi_cli.auth.oauth.OAuthManager``)


.. _func-register_terminal_tool_call_id:

register_terminal_tool_call_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 75)

**Description:**

    Register Terminal Tool Call Id.
    
    Args:
    tool\_call\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_call_id`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`get <func-get>`


.. _func-reload:

reload
^^^^^^

**Module:** ``kimi_cli.ui.shell.setup``

**File:** :file:`src/kimi_cli/ui/shell/setup.py` (line 31)

**Description:**

    Reload configuration

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)


.. _func-replace_tools:

replace_tools
^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.tools``

**File:** :file:`src/kimi_cli/acp/tools.py` (line 20)

**Description:**

    Replace Tools.
    
    Args:
    client\_capabilities: Description.
    acp\_conn: Description.
    acp\_session\_id: Description.
    toolset: Description.
    runtime: Description.
    
    Returns:
  
    ...

**Parameters:**

    - ``client_capabilities`` (*acp.schema.ClientCapabilities*)
    - ``acp_conn`` (*acp.Client*)
    - ``acp_session_id`` (*str*)
    - ``toolset`` (*KimiToolset*)
    - ``runtime`` (*Runtime*)

**Returns:** ``None``

**Calls:**

    - :ref:`Terminal <func-Terminal>`
    - :ref:`add <func-add>`
    - :ref:`find <func-find>`
    - :ref:`get_current_kaos <func-get_current_kaos>`

**Called by:**

    - :ref:`load_session <func-load_session>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`new_session <func-new_session>` (from ``kimi_cli.acp.server.ACPServer``)


.. _func-replay_history:

replay_history
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 473)

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

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)


.. _func-replay_recent_history:

replay_recent_history
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.replay``

**File:** :file:`src/kimi_cli/ui/shell/replay.py` (line 79)

**Description:**

    Replay the most recent user-initiated turns from the provided message history or wire file.

**Parameters:**

    - ``history`` (*Sequence[Message]*)
    - ``wire_file`` (*WireFile | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`Wire <func-Wire>`
    - :ref:`create_task <func-create_task>`
    - :ref:`getuser <func-getuser>`
    - :ref:`_build_replay_turns_from_history <func-_build_replay_turns_from_history>`
    - :ref:`_build_replay_turns_from_wire <func-_build_replay_turns_from_wire>`
    - :ref:`_find_replay_start <func-_find_replay_start>`
    - :ref:`visualize <func-visualize>`
    - :ref:`message_stringify <func-message_stringify>`
    - :ref:`print <func-print>`
    - :ref:`send <func-send>`
    - :ref:`shutdown <func-shutdown>`
    - :ref:`sleep <func-sleep>`
    - :ref:`suppress <func-suppress>`
    - :ref:`ui_side <func-ui_side>`

**Called by:**

    - :ref:`run <func-run>` (from ``kimi_cli.ui.shell.__init__.Shell``)


.. _func-request_device_authorization:

request_device_authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 448)

**Description:**

    Request Device Authorization.

**Returns:** ``DeviceAuthorization``

**Calls:**

    - :ref:`DeviceAuthorization <func-DeviceAuthorization>`
    - :ref:`OAuthError <func-OAuthError>`
    - :ref:`get <func-get>`
    - :ref:`int <func-int>`
    - :ref:`json <func-json>`
    - :ref:`_common_headers <func-_common_headers>`
    - :ref:`_oauth_host <func-_oauth_host>`
    - :ref:`new_client_session <func-new_client_session>`
    - :ref:`post <func-post>`
    - :ref:`rstrip <func-rstrip>`
    - :ref:`str <func-str>`

**Called by:**

    - :ref:`login_kimi_code <func-login_kimi_code>` (from ``kimi_cli.auth.oauth``)


.. _func-resolve_code_theme:

resolve_code_theme
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.syntax``

**File:** :file:`src/kimi_cli/utils/rich/syntax.py` (line 109)

**Description:**

    Resolve Code Theme.
    
    Args:
    theme: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``theme`` (*str | SyntaxTheme*)

**Returns:** ``str | SyntaxTheme``

**Calls:**

    - :ref:`isinstance <func-isinstance>`
    - :ref:`lower <func-lower>`

**Called by:**

    - :ref:`__init__ <func-__init__>` (from ``kimi_cli.utils.rich.markdown.Markdown``)


.. _func-resolve_skills_roots:

resolve_skills_roots
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 111)

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

    - :ref:`create <func-create>` (from ``kimi_cli.soul.agent.Runtime``)


.. _func-restore_stderr:

restore_stderr
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 128)

**Description:**

    Restore Stderr.

**Returns:** ``None``

**Calls:**

    - :ref:`uninstall <func-uninstall>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)


.. _func-restore_word_wrap:

restore_word_wrap
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.__init__``

**File:** :file:`src/kimi_cli/utils/rich/__init__.py` (line 40)

**Description:**

    Restore Rich's default word-based wrapping.

**Returns:** ``None``


.. _func-run_auto_archive:

run_auto_archive
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 365)

**Description:**

    Run auto-archive on old sessions.

    This function is designed to be called periodically (e.g., on app startup,
    or via a background task) rather than on every read operation.

    Returns:
     
    ...

**Returns:** ``int``

**Calls:**

    - :ref:`_build_sessions_index <func-_build_sessions_index>`
    - :ref:`_should_auto_archive <func-_should_auto_archive>`
    - :ref:`invalidate_sessions_cache <func-invalidate_sessions_cache>`
    - :ref:`save_session_metadata <func-save_session_metadata>`
    - :ref:`model_copy <func-model_copy>`
    - :ref:`time <func-time>`


.. _func-run_soul:

run_soul
^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 152)

**Description:**

    Run the soul with the given user input, connecting it to the UI loop with a \`Wire\`.

    \`cancel\_event\` is a outside handle that can be used to cancel the run. When the
    event is set, the run will 
    ...

**Parameters:**

    - ``soul`` (*Soul*)
    - ``user_input`` (*str | list[ContentPart]*)
    - ``ui_loop_fn`` (*UILoopFn*)
    - ``cancel_event`` (*asyncio.Event*)
    - ``wire_file`` (*WireFile | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`Wire <func-Wire>`
    - :ref:`cancel <func-cancel>`
    - :ref:`create_task <func-create_task>`
    - :ref:`debug <func-debug>`
    - :ref:`done <func-done>`
    - :ref:`is_set <func-is_set>`
    - :ref:`join <func-join>`
    - :ref:`reset <func-reset>`
    - :ref:`result <func-result>`
    - :ref:`run <func-run>`
    - :ref:`shutdown <func-shutdown>`
    - :ref:`suppress <func-suppress>`
    - :ref:`ui_loop_fn <func-ui_loop_fn>`
    - :ref:`wait <func-wait>`
    - :ref:`wait_for <func-wait_for>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`run <func-run>` (from ``kimi_cli.app.KimiCLI``)
    - :ref:`_run_subagent <func-_run_subagent>` (from ``kimi_cli.tools.multiagent.task.Task``)
    - :ref:`run <func-run>` (from ``kimi_cli.ui.print.__init__.Print``)
    - :ref:`run_soul_command <func-run_soul_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`_handle_prompt <func-_handle_prompt>` (from ``kimi_cli.wire.server.WireServer``)


.. _func-run_term:

run_term
^^^^^^^^

**Module:** ``kimi_cli.cli.toad``

**File:** :file:`src/kimi_cli/cli/toad.py` (line 88)

**Description:**

    Run Term.
    
    Args:
    ctx: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ctx`` (*typer.Context*)

**Returns:** ``None``

**Calls:**

    - :ref:`Exit <func-Exit>`
    - :ref:`append <func-append>`
    - :ref:`join <func-join>`
    - :ref:`_default_acp_command <func-_default_acp_command>`
    - :ref:`_default_toad_command <func-_default_toad_command>`
    - :ref:`_extract_project_dir <func-_extract_project_dir>`
    - :ref:`list <func-list>`
    - :ref:`run <func-run>`
    - :ref:`str <func-str>`

**Called by:**

    - :ref:`term <func-term>` (from ``kimi_cli.cli.__init__``)


.. _func-run_web_server:

run_web_server
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.app``

**File:** :file:`src/kimi_cli/web/app.py` (line 325)

**Description:**

    Run the web server.

**Parameters:**

    - ``host`` (*str*) = ``'127.0.0.1'``
    - ``port`` (*int*) = ``DEFAULT_PORT``
    - ``reload`` (*bool*) = ``False``
    - ``open_browser`` (*bool*) = ``True``
    - ``auth_token`` (*str | None*) = ``None``
    - ``allowed_origins`` (*str | None*) = ``None``
    - ``dangerously_omit_auth`` (*bool*) = ``False``
    - ``restrict_sensitive_apis`` (*bool | None*) = ``None``
    - ``lan_only`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`Thread <func-Thread>`
    - :ref:`append <func-append>`
    - :ref:`center <func-center>`
    - :ref:`extend <func-extend>`
    - :ref:`input <func-input>`
    - :ref:`isatty <func-isatty>`
    - :ref:`join <func-join>`
    - :ref:`_get_network_addresses <func-_get_network_addresses>`
    - :ref:`_get_private_addresses <func-_get_private_addresses>`
    - :ref:`_is_local_host <func-_is_local_host>`
    - :ref:`find_available_port <func-find_available_port>`
    - :ref:`normalize_allowed_origins <func-normalize_allowed_origins>`
    - :ref:`len <func-len>`
    - :ref:`ljust <func-ljust>`
    - :ref:`make_url <func-make_url>`
    - :ref:`max <func-max>`
    - :ref:`open <func-open>`
    - :ref:`pop <func-pop>`
    - :ref:`print <func-print>`
    - :ref:`print_banner <func-print_banner>`
    - :ref:`quote <func-quote>`
    - :ref:`removeprefix <func-removeprefix>`
    - :ref:`run <func-run>`
    - :ref:`sleep <func-sleep>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip_tags <func-strip_tags>`
    - :ref:`token_urlsafe <func-token_urlsafe>`
    - :ref:`wrap <func-wrap>`

**Called by:**

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`web <func-web>` (from ``kimi_cli.cli.web``)


.. _func-run_worker:

run_worker
^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.worker``

**File:** :file:`src/kimi_cli/web/runner/worker.py` (line 22)

**Description:**

    Run the KimiCLI worker for a session.

**Parameters:**

    - ``session_id`` (*UUID*)

**Returns:** ``None``

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`create <func-create>`
    - :ref:`exists <func-exists>`
    - :ref:`get_global_mcp_config_file <func-get_global_mcp_config_file>`
    - :ref:`load_session_by_id <func-load_session_by_id>`
    - :ref:`loads <func-loads>`
    - :ref:`read_text <func-read_text>`
    - :ref:`run_wire_stdio <func-run_wire_stdio>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`web_worker <func-web_worker>` (from ``kimi_cli.cli.__init__``)
    - :ref:`main <func-main>` (from ``kimi_cli.web.runner.worker``)


.. _func-Runtime.copy_for_dynamic_subagent:

Runtime.copy_for_dynamic_subagent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 177)

**Description:**

    Clone runtime for dynamic subagent.

**Parameters:**

    - ``self``

**Returns:** ``Runtime``

**Calls:**

    - :ref:`DenwaRenji <func-DenwaRenji>`
    - :ref:`Runtime <func-Runtime>`
    - :ref:`share <func-share>`


.. _func-Runtime.copy_for_fixed_subagent:

Runtime.copy_for_fixed_subagent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 162)

**Description:**

    Clone runtime for fixed subagent.

**Parameters:**

    - ``self``

**Returns:** ``Runtime``

**Calls:**

    - :ref:`DenwaRenji <func-DenwaRenji>`
    - :ref:`LaborMarket <func-LaborMarket>`
    - :ref:`Runtime <func-Runtime>`
    - :ref:`share <func-share>`


.. _func-Runtime.create:

Runtime.create
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.agent``

**File:** :file:`src/kimi_cli/soul/agent.py` (line 115)

**Parameters:**

    - ``config`` (*Config*)
    - ``oauth`` (*OAuthManager*)
    - ``llm`` (*LLM | None*)
    - ``session`` (*Session*)
    - ``yolo`` (*bool*)
    - ``skills_dir`` (*KaosPath | None*) = ``None``

**Returns:** ``Runtime``

**Calls:**

    - :ref:`Approval <func-Approval>`
    - :ref:`BuiltinSystemPromptArgs <func-BuiltinSystemPromptArgs>`
    - :ref:`DenwaRenji <func-DenwaRenji>`
    - :ref:`LaborMarket <func-LaborMarket>`
    - :ref:`Runtime <func-Runtime>`
    - :ref:`astimezone <func-astimezone>`
    - :ref:`detect <func-detect>`
    - :ref:`discover_skills_from_roots <func-discover_skills_from_roots>`
    - :ref:`gather <func-gather>`
    - :ref:`index_skills <func-index_skills>`
    - :ref:`info <func-info>`
    - :ref:`isoformat <func-isoformat>`
    - :ref:`join <func-join>`
    - :ref:`load_agents_md <func-load_agents_md>`
    - :ref:`list_directory <func-list_directory>`
    - :ref:`len <func-len>`
    - :ref:`now <func-now>`
    - :ref:`resolve_skills_roots <func-resolve_skills_roots>`



S
-

.. _func-sanitize_filename:

sanitize_filename
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 243)

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

    - :ref:`upload_session_file <func-upload_session_file>` (from ``kimi_cli.web.api.sessions``)


.. _func-save_config:

save_config
^^^^^^^^^^^

**Module:** ``kimi_cli.config``

**File:** :file:`src/kimi_cli/config.py` (line 259)

**Description:**

    Save configuration to config file.

    Args:
        config (Config): Config object to save.
        config\_file (Path | None): Path to the configuration file. If None, use default path.

**Parameters:**

    - ``config`` (*Config*)
    - ``config_file`` (*Path | None*) = ``None``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`dumps <func-dumps>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`lower <func-lower>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`model_dump <func-model_dump>`
    - :ref:`open <func-open>`
    - :ref:`write <func-write>`

**Called by:**

    - :ref:`set_session_model <func-set_session_model>` (from ``kimi_cli.acp.server.ACPServer``)
    - :ref:`_migrate_oauth_storage <func-_migrate_oauth_storage>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`login_kimi_code <func-login_kimi_code>` (from ``kimi_cli.auth.oauth``)
    - :ref:`logout_kimi_code <func-logout_kimi_code>` (from ``kimi_cli.auth.oauth``)
    - :ref:`refresh_managed_models <func-refresh_managed_models>` (from ``kimi_cli.auth.platforms``)
    - :ref:`_migrate_json_config_to_toml <func-_migrate_json_config_to_toml>` (from ``kimi_cli.config``)
    - :ref:`load_config <func-load_config>` (from ``kimi_cli.config``)
    - :ref:`logout <func-logout>` (from ``kimi_cli.ui.shell.oauth``)
    - :ref:`_apply_setup_result <func-_apply_setup_result>` (from ``kimi_cli.ui.shell.setup``)
    - :ref:`model <func-model>` (from ``kimi_cli.ui.shell.slash``)
    - :ref:`update_global_config <func-update_global_config>` (from ``kimi_cli.web.api.config``)


.. _func-save_metadata:

save_metadata
^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 18)

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

    - :ref:`kimi <func-kimi>` (from ``kimi_cli.cli.__init__``)
    - :ref:`create <func-create>` (from ``kimi_cli.session.Session``)
    - :ref:`_update_last_session_id <func-_update_last_session_id>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`delete_session <func-delete_session>` (from ``kimi_cli.web.api.sessions``)


.. _func-save_session_metadata:

save_session_metadata
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.store.sessions``

**File:** :file:`src/kimi_cli/web/store/sessions.py` (line 136)

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

    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`generate_session_title <func-generate_session_title>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`update_session <func-update_session>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`_ensure_title <func-_ensure_title>` (from ``kimi_cli.web.store.sessions``)
    - :ref:`run_auto_archive <func-run_auto_archive>` (from ``kimi_cli.web.store.sessions``)


.. _func-save_tokens:

save_tokens
^^^^^^^^^^^

**Module:** ``kimi_cli.auth.oauth``

**File:** :file:`src/kimi_cli/auth/oauth.py` (line 417)

**Description:**

    Save Tokens.
    
    Args:
    ref: Description.
    token: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``ref`` (*OAuthRef*)
    - ``token`` (*OAuthToken*)

**Returns:** ``OAuthRef``

**Calls:**

    - :ref:`OAuthRef <func-OAuthRef>`
    - :ref:`_save_to_file <func-_save_to_file>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`_refresh_tokens <func-_refresh_tokens>` (from ``kimi_cli.auth.oauth.OAuthManager``)
    - :ref:`login_kimi_code <func-login_kimi_code>` (from ``kimi_cli.auth.oauth``)


.. _func-select_platform:

select_platform
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.setup``

**File:** :file:`src/kimi_cli/ui/shell/setup.py` (line 111)

**Description:**

    Select Platform.

**Returns:** ``Platform | None``

**Calls:**

    - :ref:`get_platform_by_name <func-get_platform_by_name>`
    - :ref:`_prompt_choice <func-_prompt_choice>`
    - :ref:`print <func-print>`

**Called by:**

    - :ref:`login <func-login>` (from ``kimi_cli.ui.shell.oauth``)


.. _func-semver_tuple:

semver_tuple
^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.update``

**File:** :file:`src/kimi_cli/ui/shell/update.py` (line 26)

**Description:**

    Semver Tuple.
    
    Args:
    version: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``version`` (*str*)

**Calls:**

    - :ref:`group <func-group>`
    - :ref:`int <func-int>`
    - :ref:`match <func-match>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip <func-strip>`

**Called by:**

    - :ref:`_print_welcome_info <func-_print_welcome_info>` (from ``kimi_cli.ui.shell.__init__``)
    - :ref:`_do_update <func-_do_update>` (from ``kimi_cli.ui.shell.update``)


.. _func-send_history_complete:

send_history_complete
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.messages``

**File:** :file:`src/kimi_cli/web/runner/messages.py` (line 51)

**Description:**

    Send history complete message to a WebSocket.

    Returns:
        True if message was sent successfully, False if the send fails or the WebSocket is not
        connected.

**Parameters:**

    - ``ws`` (*WebSocket*)

**Returns:** ``bool``

**Calls:**

    - :ref:`new_history_complete_message <func-new_history_complete_message>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`send_text <func-send_text>`

**Called by:**

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)


.. _func-serialize_wire_message:

serialize_wire_message
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.serde``

**File:** :file:`src/kimi_cli/wire/serde.py` (line 16)

**Description:**

    Convert a \`WireMessage\` into a jsonifiable dict.

**Parameters:**

    - ``msg`` (*WireMessage*)

**Calls:**

    - :ref:`from_wire_message <func-from_wire_message>`
    - :ref:`model_dump <func-model_dump>`

**Called by:**

    - :ref:`_serialize_params <func-_serialize_params>` (from ``kimi_cli.wire.jsonrpc.JSONRPCEventMessage``)
    - :ref:`_serialize_params <func-_serialize_params>` (from ``kimi_cli.wire.jsonrpc.JSONRPCRequestMessage``)


.. _func-Session.continue_:

Session.continue_
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 227)

**Description:**

    Get the last session for a work directory.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``Session | None``

**Calls:**

    - :ref:`canonical <func-canonical>`
    - :ref:`debug <func-debug>`
    - :ref:`find <func-find>`
    - :ref:`get_work_dir_meta <func-get_work_dir_meta>`
    - :ref:`load_metadata <func-load_metadata>`


.. _func-Session.create:

Session.create
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 82)

**Description:**

    Create a new session for a work directory.

**Parameters:**

    - ``work_dir`` (*KaosPath*)
    - ``session_id`` (*str | None*) = ``None``
    - ``_context_file`` (*Path | None*) = ``None``

**Returns:** ``Session``

**Calls:**

    - :ref:`Session <func-Session>`
    - :ref:`WireFile <func-WireFile>`
    - :ref:`canonical <func-canonical>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`get_work_dir_meta <func-get_work_dir_meta>`
    - :ref:`is_file <func-is_file>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`save_metadata <func-save_metadata>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`new_work_dir_meta <func-new_work_dir_meta>`
    - :ref:`refresh <func-refresh>`
    - :ref:`str <func-str>`
    - :ref:`touch <func-touch>`
    - :ref:`unlink <func-unlink>`
    - :ref:`uuid4 <func-uuid4>`
    - :ref:`warning <func-warning>`


.. _func-Session.delete:

Session.delete
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 54)

**Description:**

    Delete the session directory.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`exists <func-exists>`
    - :ref:`to_thread <func-to_thread>`


.. _func-Session.dir:

Session.dir
^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 39)

**Description:**

    The absolute path of the session directory.

**Parameters:**

    - ``self``

**Returns:** ``Path``

**Calls:**

    - :ref:`mkdir <func-mkdir>`


.. _func-Session.find:

Session.find
^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 135)

**Description:**

    Find a session by work directory and session ID.

**Parameters:**

    - ``work_dir`` (*KaosPath*)
    - ``session_id`` (*str*)

**Returns:** ``Session | None``

**Calls:**

    - :ref:`Session <func-Session>`
    - :ref:`WireFile <func-WireFile>`
    - :ref:`canonical <func-canonical>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`get_work_dir_meta <func-get_work_dir_meta>`
    - :ref:`is_dir <func-is_dir>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`_migrate_session_context_file <func-_migrate_session_context_file>`
    - :ref:`refresh <func-refresh>`


.. _func-Session.is_empty:

Session.is_empty
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 45)

**Description:**

    Whether the session has any context history.

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`is_empty <func-is_empty>`
    - :ref:`stat <func-stat>`


.. _func-Session.list:

Session.list
^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 177)

**Description:**

    List all sessions for a work directory.

**Parameters:**

    - ``work_dir`` (*KaosPath*)

**Returns:** ``builtins.list[Session]``

**Calls:**

    - :ref:`Session <func-Session>`
    - :ref:`WireFile <func-WireFile>`
    - :ref:`append <func-append>`
    - :ref:`canonical <func-canonical>`
    - :ref:`debug <func-debug>`
    - :ref:`exists <func-exists>`
    - :ref:`get_work_dir_meta <func-get_work_dir_meta>`
    - :ref:`is_dir <func-is_dir>`
    - :ref:`is_empty <func-is_empty>`
    - :ref:`iterdir <func-iterdir>`
    - :ref:`load_metadata <func-load_metadata>`
    - :ref:`_migrate_session_context_file <func-_migrate_session_context_file>`
    - :ref:`refresh <func-refresh>`
    - :ref:`sort <func-sort>`


.. _func-Session.refresh:

Session.refresh
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.session``

**File:** :file:`src/kimi_cli/session.py` (line 61)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`exception <func-exception>`
    - :ref:`exists <func-exists>`
    - :ref:`extract_text <func-extract_text>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`iter_records <func-iter_records>`
    - :ref:`shorten <func-shorten>`
    - :ref:`stat <func-stat>`
    - :ref:`to_wire_message <func-to_wire_message>`


.. _func-session_stream:

session_stream
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 1237)

**Description:**

    WebSocket stream for a session.

    Flow:
    1. Accept the WebSocket connection
    2. If history exists, attach WebSocket in replay mode
    3. Replay history messages from wire.jsonl
    4. Start 
    ...

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
    - :ref:`get <func-get>`
    - :ref:`get_or_create_session <func-get_or_create_session>`
    - :ref:`getattr <func-getattr>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`replay_history <func-replay_history>`
    - :ref:`is_origin_allowed <func-is_origin_allowed>`
    - :ref:`is_private_ip <func-is_private_ip>`
    - :ref:`verify_token <func-verify_token>`
    - :ref:`new_session_status_message <func-new_session_status_message>`
    - :ref:`send_history_complete <func-send_history_complete>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`now <func-now>`
    - :ref:`receive_text <func-receive_text>`
    - :ref:`remove_websocket <func-remove_websocket>`
    - :ref:`send_message <func-send_message>`
    - :ref:`send_status_snapshot <func-send_status_snapshot>`
    - :ref:`send_text <func-send_text>`
    - :ref:`start <func-start>`
    - :ref:`str <func-str>`
    - :ref:`to_thread <func-to_thread>`
    - :ref:`validate_json <func-validate_json>`
    - :ref:`warning <func-warning>`


.. _func-SessionProcess.add_websocket_and_begin_replay:

SessionProcess.add_websocket_and_begin_replay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 564)

**Description:**

    Atomically attach a WebSocket and enter replay mode for it.

**Parameters:**

    - ``self``
    - ``ws`` (*WebSocket*)

**Returns:** ``None``

**Calls:**

    - :ref:`add <func-add>`
    - :ref:`debug <func-debug>`
    - :ref:`len <func-len>`
    - :ref:`setdefault <func-setdefault>`


.. _func-SessionProcess.end_replay:

SessionProcess.end_replay
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 573)

**Description:**

    Flush buffered live messages for a websocket after history replay.

**Parameters:**

    - ``self``
    - ``ws`` (*WebSocket*)

**Returns:** ``None``

**Calls:**

    - :ref:`clear <func-clear>`
    - :ref:`copy <func-copy>`
    - :ref:`get <func-get>`
    - :ref:`pop <func-pop>`
    - :ref:`send_text <func-send_text>`
    - :ref:`warning <func-warning>`


.. _func-SessionProcess.is_alive:

SessionProcess.is_alive
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 107)

**Description:**

    Whether the worker subprocess exists and has not exited.

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-SessionProcess.is_busy:

SessionProcess.is_busy
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 118)

**Description:**

    Whether the session is currently processing a prompt.

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`len <func-len>`


.. _func-SessionProcess.is_running:

SessionProcess.is_running
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 113)

**Description:**

    Backward-compatible name: indicates worker liveness.

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-SessionProcess.remove_websocket:

SessionProcess.remove_websocket
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 620)

**Description:**

    Remove a WebSocket connection from this session.

**Parameters:**

    - ``self``
    - ``ws`` (*WebSocket*)

**Returns:** ``None``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`discard <func-discard>`
    - :ref:`len <func-len>`
    - :ref:`pop <func-pop>`


.. _func-SessionProcess.restart_worker:

SessionProcess.restart_worker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 262)

**Description:**

    Restart the worker subprocess without disconnecting WebSockets.

**Parameters:**

    - ``self``
    - ``reason`` (*str | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`_emit_status <func-_emit_status>`
    - :ref:`perf_counter <func-perf_counter>`
    - :ref:`start <func-start>`
    - :ref:`stop_worker <func-stop_worker>`


.. _func-SessionProcess.send_message:

SessionProcess.send_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 629)

**Description:**

    Send a message to the subprocess stdin.

**Parameters:**

    - ``self``
    - ``message`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`JSONRPCSuccessResponse <func-JSONRPCSuccessResponse>`
    - :ref:`_broadcast <func-_broadcast>`
    - :ref:`_emit_status <func-_emit_status>`
    - :ref:`_handle_in_message <func-_handle_in_message>`
    - :ref:`add <func-add>`
    - :ref:`drain <func-drain>`
    - :ref:`encode <func-encode>`
    - :ref:`error <func-error>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`start <func-start>`
    - :ref:`validate_json <func-validate_json>`
    - :ref:`write <func-write>`


.. _func-SessionProcess.send_status_snapshot:

SessionProcess.send_status_snapshot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 132)

**Description:**

    Send the current status snapshot to a specific WebSocket.

**Parameters:**

    - ``self``
    - ``ws`` (*WebSocket*)

**Returns:** ``None``

**Calls:**

    - :ref:`new_session_status_message <func-new_session_status_message>`
    - :ref:`model_dump_json <func-model_dump_json>`
    - :ref:`send_text <func-send_text>`


.. _func-SessionProcess.start:

SessionProcess.start
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 177)

**Description:**

    Start the KimiCLI subprocess.

**Parameters:**

    - ``self``
    - ``reason`` (*str | None*) = ``None``
    - ``detail`` (*str | None*) = ``None``
    - ``restart_started_at`` (*float | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`_emit_restart_notice <func-_emit_restart_notice>`
    - :ref:`_emit_status <func-_emit_status>`
    - :ref:`_read_loop <func-_read_loop>`
    - :ref:`clear <func-clear>`
    - :ref:`create_subprocess_exec <func-create_subprocess_exec>`
    - :ref:`create_task <func-create_task>`
    - :ref:`done <func-done>`
    - :ref:`getattr <func-getattr>`
    - :ref:`int <func-int>`
    - :ref:`get_clean_env <func-get_clean_env>`
    - :ref:`perf_counter <func-perf_counter>`
    - :ref:`str <func-str>`
    - :ref:`uuid4 <func-uuid4>`


.. _func-SessionProcess.status:

SessionProcess.status
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 123)

**Description:**

    Current runtime status snapshot.

**Parameters:**

    - ``self``

**Returns:** ``SessionStatus``


.. _func-SessionProcess.stop:

SessionProcess.stop
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 226)

**Description:**

    Stop the session: terminate worker and close all WebSockets.

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`_close_all_websockets <func-_close_all_websockets>`
    - :ref:`stop_worker <func-stop_worker>`


.. _func-SessionProcess.stop_worker:

SessionProcess.stop_worker
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 231)

**Description:**

    Stop only the worker subprocess, keeping WebSockets connected.

**Parameters:**

    - ``self``
    - ``reason`` (*str | None*) = ``None``
    - ``emit_status`` (*bool*) = ``True``

**Returns:** ``None``

**Calls:**

    - :ref:`_emit_status <func-_emit_status>`
    - :ref:`cancel <func-cancel>`
    - :ref:`clear <func-clear>`
    - :ref:`kill <func-kill>`
    - :ref:`suppress <func-suppress>`
    - :ref:`terminate <func-terminate>`
    - :ref:`wait_for <func-wait_for>`


.. _func-SessionProcess.websocket_count:

SessionProcess.websocket_count
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.runner.process``

**File:** :file:`src/kimi_cli/web/runner/process.py` (line 128)

**Description:**

    Get the number of connected WebSockets.

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-setup_platform:

setup_platform
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.setup``

**File:** :file:`src/kimi_cli/ui/shell/setup.py` (line 129)

**Description:**

    Setup Platform.
    
    Args:
    platform: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``platform`` (*Platform*)

**Returns:** ``bool``

**Calls:**

    - :ref:`_apply_setup_result <func-_apply_setup_result>`
    - :ref:`_setup_platform <func-_setup_platform>`
    - :ref:`print <func-print>`

**Called by:**

    - :ref:`login <func-login>` (from ``kimi_cli.ui.shell.oauth``)


.. _func-Shell.available_slash_commands:

Shell.available_slash_commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.__init__``

**File:** :file:`src/kimi_cli/ui/shell/__init__.py` (line 135)

**Description:**

    Get all available slash commands, including shell-level and soul-level commands.

**Parameters:**

    - ``self``


.. _func-Shell.run:

Shell.run
^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.__init__``

**File:** :file:`src/kimi_cli/ui/shell/__init__.py` (line 139)

**Parameters:**

    - ``self``
    - ``command`` (*str | None*) = ``None``

**Returns:** ``bool``

**Calls:**

    - :ref:`CustomPromptSession <func-CustomPromptSession>`
    - :ref:`_auto_update <func-_auto_update>`
    - :ref:`_run_shell_command <func-_run_shell_command>`
    - :ref:`_run_slash_command <func-_run_slash_command>`
    - :ref:`_start_background_task <func-_start_background_task>`
    - :ref:`debug <func-debug>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_print_welcome_info <func-_print_welcome_info>`
    - :ref:`replay_recent_history <func-replay_recent_history>`
    - :ref:`get_env_bool <func-get_env_bool>`
    - :ref:`parse_slash_command_call <func-parse_slash_command_call>`
    - :ref:`ensure_new_line <func-ensure_new_line>`
    - :ref:`ensure_tty_sane <func-ensure_tty_sane>`
    - :ref:`list_commands <func-list_commands>`
    - :ref:`print <func-print>`
    - :ref:`prompt <func-prompt>`
    - :ref:`run_soul_command <func-run_soul_command>`
    - :ref:`set <func-set>`
    - :ref:`values <func-values>`


.. _func-Shell.run_soul_command:

Shell.run_soul_command
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.__init__``

**File:** :file:`src/kimi_cli/ui/shell/__init__.py` (line 302)

**Description:**

    Run the soul and handle any known exceptions.

        Returns:
            bool: Whether the run is successful.

**Parameters:**

    - ``self``
    - ``user_input`` (*str | list[ContentPart]*)

**Returns:** ``bool``

**Calls:**

    - :ref:`Event <func-Event>`
    - :ref:`StatusUpdate <func-StatusUpdate>`
    - :ref:`debug <func-debug>`
    - :ref:`exception <func-exception>`
    - :ref:`get_running_loop <func-get_running_loop>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`visualize <func-visualize>`
    - :ref:`install_sigint_handler <func-install_sigint_handler>`
    - :ref:`print <func-print>`
    - :ref:`remove_sigint <func-remove_sigint>`
    - :ref:`run_soul <func-run_soul>`
    - :ref:`set <func-set>`
    - :ref:`ui_side <func-ui_side>`
    - :ref:`warning <func-warning>`


.. _func-shorten_home:

shorten_home
^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.path``

**File:** :file:`src/kimi_cli/utils/path.py` (line 55)

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

    - :ref:`run_shell <func-run_shell>` (from ``kimi_cli.app.KimiCLI``)


.. _func-shorten_middle:

shorten_middle
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.string``

**File:** :file:`src/kimi_cli/utils/string.py` (line 28)

**Description:**

    Shorten the text by inserting ellipsis in the middle.

**Parameters:**

    - ``text`` (*str*)
    - ``width`` (*int*)
    - ``remove_newline`` (*bool*) = ``True``

**Returns:** ``str``

**Calls:**

    - :ref:`len <func-len>`
    - :ref:`sub <func-sub>`

**Called by:**

    - :ref:`extract_key_argument <func-extract_key_argument>` (from ``kimi_cli.tools.__init__``)


.. _func-should_hide_terminal_output:

should_hide_terminal_output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.session``

**File:** :file:`src/kimi_cli/acp/session.py` (line 62)

**Description:**

    Should Hide Terminal Output.
    
    Args:
    tool\_call\_id: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_call_id`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`get <func-get>`

**Called by:**

    - :ref:`_send_tool_result <func-_send_tool_result>` (from ``kimi_cli.acp.session.ACPSession``)


.. _func-SimpleCompaction.compact:

SimpleCompaction.compact
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.compaction``

**File:** :file:`src/kimi_cli/soul/compaction.py` (line 41)

**Parameters:**

    - ``self``
    - ``messages`` (*Sequence[Message]*)
    - ``llm`` (*LLM*)

**Returns:** ``Sequence[Message]``

**Calls:**

    - :ref:`EmptyToolset <func-EmptyToolset>`
    - :ref:`Message <func-Message>`
    - :ref:`debug <func-debug>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`system <func-system>`
    - :ref:`prepare <func-prepare>`
    - :ref:`step <func-step>`


.. _func-SimpleCompaction.prepare:

SimpleCompaction.prepare
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.compaction``

**File:** :file:`src/kimi_cli/soul/compaction.py` (line 77)

**Parameters:**

    - ``self``
    - ``messages`` (*Sequence[Message]*)

**Returns:** ``PrepareResult``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`PrepareResult <func-PrepareResult>`
    - :ref:`TextPart <func-TextPart>`
    - :ref:`append <func-append>`
    - :ref:`enumerate <func-enumerate>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`range <func-range>`


.. _func-Skill.skill_md_file:

Skill.skill_md_file
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.__init__``

**File:** :file:`src/kimi_cli/skill/__init__.py` (line 79)

**Description:**

    Path to the SKILL.md file.

**Parameters:**

    - ``self``

**Returns:** ``KaosPath``


.. _func-SlashCommand.slash_name:

SlashCommand.slash_name
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.slashcmd``

**File:** :file:`src/kimi_cli/utils/slashcmd.py` (line 16)

**Description:**

    /name (aliases)

**Parameters:**

    - ``self``

**Calls:**

    - :ref:`join <func-join>`


.. _func-SlashCommandCompleter.get_completions:

SlashCommandCompleter.get_completions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 214)

**Parameters:**

    - ``self``
    - ``document`` (*Document*)
    - ``complete_event`` (*CompleteEvent*)

**Returns:** ``Iterable[Completion]``

**Calls:**

    - :ref:`Completion <func-Completion>`
    - :ref:`Document <func-Document>`
    - :ref:`add <func-add>`
    - :ref:`get_completions <func-get_completions>`
    - :ref:`len <func-len>`
    - :ref:`list <func-list>`
    - :ref:`rfind <func-rfind>`
    - :ref:`set <func-set>`
    - :ref:`slash_name <func-slash_name>`
    - :ref:`startswith <func-startswith>`
    - :ref:`strip <func-strip>`


.. _func-SlashCommandRegistry.command:

SlashCommandRegistry.command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.slashcmd``

**File:** :file:`src/kimi_cli/utils/slashcmd.py` (line 74)

**Description:**

    Decorator to register a slash command with optional custom name and aliases.

        Usage examples:
          @registry.command
          def help(app: App, args: str): ...

          @registry.comm
    ...

**Parameters:**

    - ``self``
    - ``func`` (*F | None*) = ``None``
    - ``name`` (*str | None*) = ``None``
    - ``aliases`` (*Sequence[str] | None*) = ``None``

**Calls:**

    - :ref:`_register <func-_register>`
    - :ref:`list <func-list>`
    - :ref:`strip <func-strip>`


.. _func-SlashCommandRegistry.find_command:

SlashCommandRegistry.find_command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.slashcmd``

**File:** :file:`src/kimi_cli/utils/slashcmd.py` (line 121)

**Parameters:**

    - ``self``
    - ``name`` (*str*)

**Returns:** ``SlashCommand[F] | None``

**Calls:**

    - :ref:`get <func-get>`


.. _func-SlashCommandRegistry.list_commands:

SlashCommandRegistry.list_commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.slashcmd``

**File:** :file:`src/kimi_cli/utils/slashcmd.py` (line 124)

**Description:**

    Get all unique primary slash commands (without duplicating aliases).

**Parameters:**

    - ``self``

**Returns:** ``list[SlashCommand[F]]``

**Calls:**

    - :ref:`list <func-list>`
    - :ref:`values <func-values>`


.. _func-sniff_media_from_magic:

sniff_media_from_magic
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.file.utils``

**File:** :file:`src/kimi_cli/tools/file/utils.py` (line 217)

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

    - :ref:`detect_file_type <func-detect_file_type>` (from ``kimi_cli.tools.file.utils``)


.. _func-Soul.available_slash_commands:

Soul.available_slash_commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 85)

**Description:**

    List of available slash commands supported by the soul.

**Parameters:**

    - ``self``

**Returns:** ``list[SlashCommand[Any]]``


.. _func-Soul.model_capabilities:

Soul.model_capabilities
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 67)

**Description:**

    The capabilities of the LLM model used by the soul. None if LLM is not set.

**Parameters:**

    - ``self``

**Returns:** ``set[ModelCapability] | None``


.. _func-Soul.model_name:

Soul.model_name
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 62)

**Description:**

    The name of the LLM model used by the soul. Empty string if LLM is not set.

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-Soul.name:

Soul.name
^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 57)

**Description:**

    The name of the soul.

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-Soul.run:

Soul.run
^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 89)

**Description:**

    Run the agent with the given user input until the max steps or no more tool calls.

        Args:
            user\_input (str | list[ContentPart]): The user input to the agent.
                Can be 
    ...

**Parameters:**

    - ``self``
    - ``user_input`` (*str | list[ContentPart]*)


.. _func-Soul.status:

Soul.status
^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 80)

**Description:**

    The current status of the soul. The returned value is immutable.

**Parameters:**

    - ``self``

**Returns:** ``StatusSnapshot``


.. _func-Soul.thinking:

Soul.thinking
^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 72)

**Description:**

    Whether thinking mode is currently enabled.
        None if LLM is not set or thinking mode is not set explicitly.

**Parameters:**

    - ``self``

**Returns:** ``bool | None``


.. _func-StderrRedirector.install:

StderrRedirector.install
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 25)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Thread <func-Thread>`
    - :ref:`close <func-close>`
    - :ref:`dup2 <func-dup2>`
    - :ref:`flush <func-flush>`
    - :ref:`getpreferredencoding <func-getpreferredencoding>`
    - :ref:`pipe <func-pipe>`
    - :ref:`start <func-start>`
    - :ref:`suppress <func-suppress>`


.. _func-StderrRedirector.open_original_stderr_handle:

StderrRedirector.open_original_stderr_handle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 90)

**Parameters:**

    - ``self``

**Returns:** ``IO[bytes] | None``

**Calls:**

    - :ref:`dup <func-dup>`
    - :ref:`fdopen <func-fdopen>`
    - :ref:`set_inheritable <func-set_inheritable>`


.. _func-StderrRedirector.uninstall:

StderrRedirector.uninstall
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.logging``

**File:** :file:`src/kimi_cli/utils/logging.py` (line 48)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`dup2 <func-dup2>`
    - :ref:`join <func-join>`


.. _func-system:

system
^^^^^^

**Module:** ``kimi_cli.soul.message``

**File:** :file:`src/kimi_cli/soul/message.py` (line 53)

**Description:**

    System.
    
    Args:
    message: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``message`` (*str*)

**Returns:** ``ContentPart``

**Calls:**

    - :ref:`TextPart <func-TextPart>`

**Called by:**

    - :ref:`_device_model <func-_device_model>` (from ``kimi_cli.auth.oauth``)
    - :ref:`compact <func-compact>` (from ``kimi_cli.soul.compaction.SimpleCompaction``)
    - :ref:`checkpoint <func-checkpoint>` (from ``kimi_cli.soul.context.Context``)
    - :ref:`_step <func-_step>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`tool_result_to_message <func-tool_result_to_message>` (from ``kimi_cli.soul.message``)
    - :ref:`init <func-init>` (from ``kimi_cli.soul.slash``)
    - :ref:`_detect_target <func-_detect_target>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`_rg_binary_name <func-_rg_binary_name>` (from ``kimi_cli.tools.file.grep_local``)
    - :ref:`_detect_target <func-_detect_target>` (from ``kimi_cli.ui.shell.update``)
    - :ref:`detect <func-detect>` (from ``kimi_cli.utils.environment.Environment``)



T
-

.. _func-TableBodyElement.on_child_close:

TableBodyElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 330)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`isinstance <func-isinstance>`


.. _func-TableDataElement.create:

TableDataElement.create
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 351)

**Parameters:**

    - ``cls``
    - ``markdown`` (*Markdown*)
    - ``token`` (*Token*)

**Returns:** ``MarkdownElement``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`get_args <func-get_args>`
    - :ref:`str <func-str>`


.. _func-TableDataElement.on_text:

TableDataElement.on_text
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 371)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``text`` (*TextType*)

**Returns:** ``None``

**Calls:**

    - :ref:`Text <func-Text>`
    - :ref:`append_text <func-append_text>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`stylize <func-stylize>`


.. _func-TableElement.on_child_close:

TableElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 290)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`RuntimeError <func-RuntimeError>`
    - :ref:`isinstance <func-isinstance>`


.. _func-TableHeaderElement.on_child_close:

TableHeaderElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 319)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`isinstance <func-isinstance>`


.. _func-TableRowElement.on_child_close:

TableRowElement.on_child_close
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 341)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``child`` (*MarkdownElement*)

**Returns:** ``bool``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`isinstance <func-isinstance>`


.. _func-term:

term
^^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 143)

**Description:**

    Run Toad TUI backed by Kimi Code CLI ACP server.

**Parameters:**

    - ``ctx`` (*typer.Context*)

**Returns:** ``None``

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`run_term <func-run_term>`


.. _func-TextElement.on_enter:

TextElement.on_enter
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 164)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``

**Calls:**

    - :ref:`Text <func-Text>`
    - :ref:`enter_style <func-enter_style>`


.. _func-TextElement.on_leave:

TextElement.on_leave
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 171)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)

**Returns:** ``None``

**Calls:**

    - :ref:`leave_style <func-leave_style>`


.. _func-TextElement.on_text:

TextElement.on_text
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.rich.markdown``

**File:** :file:`src/kimi_cli/utils/rich/markdown.py` (line 168)

**Parameters:**

    - ``self``
    - ``context`` (*MarkdownContext*)
    - ``text`` (*TextType*)

**Returns:** ``None``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`isinstance <func-isinstance>`


.. _func-TextPrinter.feed:

TextPrinter.feed
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 59)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`print <func-print>`


.. _func-TextPrinter.flush:

TextPrinter.flush
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 62)

**Parameters:**

    - ``self``

**Returns:** ``None``


.. _func-timing_safe_compare:

timing_safe_compare
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 46)

**Description:**

    Timing-safe string comparison.

**Parameters:**

    - ``a`` (*str*)
    - ``b`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`compare_digest <func-compare_digest>`
    - :ref:`encode <func-encode>`

**Called by:**

    - :ref:`verify_token <func-verify_token>` (from ``kimi_cli.web.auth``)


.. _func-toast:

toast
^^^^^

**Module:** ``kimi_cli.ui.shell.prompt``

**File:** :file:`src/kimi_cli/ui/shell/prompt.py` (line 551)

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

    - :ref:`load_mcp_tools <func-load_mcp_tools>` (from ``kimi_cli.soul.toolset.KimiToolset``)
    - :ref:`_auto_update <func-_auto_update>` (from ``kimi_cli.ui.shell.__init__.Shell``)


.. _func-tool_result_to_acp_content:

tool_result_to_acp_content
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.acp.convert``

**File:** :file:`src/kimi_cli/acp/convert.py` (line 63)

**Description:**

    Tool Result To Acp Content.
    
    Args:
    tool\_ret: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``tool_ret`` (*ToolReturnValue*)

**Returns:** ``list[acp.schema.ContentToolCallContent | acp.schema.FileEditToolCallContent | acp.schema.TerminalToolCallContent]``

**Calls:**

    - :ref:`ContentToolCallContent <func-ContentToolCallContent>`
    - :ref:`TextContentBlock <func-TextContentBlock>`
    - :ref:`_to_text_block <func-_to_text_block>`
    - :ref:`append <func-append>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`display_block_to_acp_content <func-display_block_to_acp_content>`
    - :ref:`warning <func-warning>`

**Called by:**

    - :ref:`_send_tool_result <func-_send_tool_result>` (from ``kimi_cli.acp.session.ACPSession``)


.. _func-tool_result_to_message:

tool_result_to_message
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.soul.message``

**File:** :file:`src/kimi_cli/soul/message.py` (line 65)

**Description:**

    Convert a tool result to a message.

**Parameters:**

    - ``tool_result`` (*ToolResult*)

**Returns:** ``Message``

**Calls:**

    - :ref:`Message <func-Message>`
    - :ref:`append <func-append>`
    - :ref:`extend <func-extend>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_output_to_content_parts <func-_output_to_content_parts>`
    - :ref:`system <func-system>`

**Called by:**

    - :ref:`_grow_context <func-_grow_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`flush <func-flush>` (from ``kimi_cli.ui.print.visualize.JsonPrinter``)


.. _func-ToolCallRequest.from_tool_call:

ToolCallRequest.from_tool_call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 117)

**Parameters:**

    - ``tool_call`` (*ToolCall*)

**Returns:** ``ToolCallRequest``

**Calls:**

    - :ref:`ToolCallRequest <func-ToolCallRequest>`


.. _func-ToolCallRequest.resolve:

ToolCallRequest.resolve
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 133)

**Description:**

    Resolve the tool call with the given result.
        This will cause the \`wait()\` method to return the result.

**Parameters:**

    - ``self``
    - ``result`` (*ToolReturnValue*)

**Returns:** ``None``

**Calls:**

    - :ref:`_get_future <func-_get_future>`
    - :ref:`done <func-done>`
    - :ref:`set_result <func-set_result>`


.. _func-ToolCallRequest.resolved:

ToolCallRequest.resolved
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 143)

**Description:**

    Whether the tool call is resolved.

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`done <func-done>`


.. _func-ToolCallRequest.wait:

ToolCallRequest.wait
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 124)

**Description:**

    Wait for the tool call to be resolved or cancelled.

        Returns:
            ToolReturnValue: The tool execution result.

**Parameters:**

    - ``self``

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`_get_future <func-_get_future>`


.. _func-ToolResultBuilder.display:

ToolResultBuilder.display
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 155)

**Description:**

    Add display blocks to the tool result.

**Parameters:**

    - ``self``
    - ``*blocks`` (*DisplayBlock*)

**Returns:** ``None``

**Calls:**

    - :ref:`extend <func-extend>`


.. _func-ToolResultBuilder.error:

ToolResultBuilder.error
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 186)

**Description:**

    Create a ToolReturnValue with is\_error=True and the current output.

**Parameters:**

    - ``self``
    - ``message`` (*str*)
    - ``brief`` (*str*)

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`BriefDisplayBlock <func-BriefDisplayBlock>`
    - :ref:`ToolReturnValue <func-ToolReturnValue>`
    - :ref:`join <func-join>`


.. _func-ToolResultBuilder.extras:

ToolResultBuilder.extras
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 159)

**Description:**

    Add extra data to the tool result.

**Parameters:**

    - ``self``
    - ``**extras`` (*JsonType*)

**Returns:** ``None``

**Calls:**

    - :ref:`update <func-update>`


.. _func-ToolResultBuilder.is_full:

ToolResultBuilder.is_full
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 102)

**Description:**

    Check if output buffer is full due to character limit.

**Parameters:**

    - ``self``

**Returns:** ``bool``


.. _func-ToolResultBuilder.n_chars:

ToolResultBuilder.n_chars
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 107)

**Description:**

    Get current character count.

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-ToolResultBuilder.n_lines:

ToolResultBuilder.n_lines
^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 112)

**Description:**

    Get current line count.

**Parameters:**

    - ``self``

**Returns:** ``int``


.. _func-ToolResultBuilder.ok:

ToolResultBuilder.ok
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 165)

**Description:**

    Create a ToolReturnValue with is\_error=False and the current output.

**Parameters:**

    - ``self``
    - ``message`` (*str*) = ``''``
    - ``brief`` (*str*) = ``''``

**Returns:** ``ToolReturnValue``

**Calls:**

    - :ref:`BriefDisplayBlock <func-BriefDisplayBlock>`
    - :ref:`ToolReturnValue <func-ToolReturnValue>`
    - :ref:`endswith <func-endswith>`
    - :ref:`join <func-join>`


.. _func-ToolResultBuilder.write:

ToolResultBuilder.write
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 116)

**Description:**

    Write text to the output buffer.

        Returns:
            int: Number of characters actually written

**Parameters:**

    - ``self``
    - ``text`` (*str*)

**Returns:** ``int``

**Calls:**

    - :ref:`append <func-append>`
    - :ref:`endswith <func-endswith>`
    - :ref:`truncate_line <func-truncate_line>`
    - :ref:`len <func-len>`
    - :ref:`min <func-min>`
    - :ref:`splitlines <func-splitlines>`


.. _func-truncate_context_at_turn:

truncate_context_at_turn
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 955)

**Description:**

    Read context.jsonl and return all lines up to and including the given turn.

    Turn detection is based on real user messages, excluding synthetic checkpoint
    user entries like \`\`<system>CHECKPOIN
    ...

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

    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)


.. _func-truncate_line:

truncate_line
^^^^^^^^^^^^^

**Module:** ``kimi_cli.tools.utils``

**File:** :file:`src/kimi_cli/tools/utils.py` (line 64)

**Description:**

    Truncate a line if it exceeds \`max\_length\`, preserving the beginning and the line break.
    The output may be longer than \`max\_length\` if it is too short to fit the marker.

**Parameters:**

    - ``line`` (*str*)
    - ``max_length`` (*int*)
    - ``marker`` (*str*) = ``'...'``

**Returns:** ``str``

**Calls:**

    - :ref:`group <func-group>`
    - :ref:`len <func-len>`
    - :ref:`max <func-max>`
    - :ref:`search <func-search>`

**Called by:**

    - :ref:`__call__ <func-__call__>` (from ``kimi_cli.tools.file.read.ReadFile``)
    - :ref:`write <func-write>` (from ``kimi_cli.tools.utils.ToolResultBuilder``)


.. _func-truncate_wire_at_turn:

truncate_wire_at_turn
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 882)

**Description:**

    Read wire.jsonl and return all lines up to and including the given turn.

    Args:
        wire\_path: Path to the wire.jsonl file
        turn\_index: 0-based turn index. Returns turns 0..turn\_index i
    ...

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

    - :ref:`fork_session <func-fork_session>` (from ``kimi_cli.web.api.sessions``)



U
-

.. _func-update_config_toml:

update_config_toml
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.config``

**File:** :file:`src/kimi_cli/web/api/config.py` (line 92)

**Description:**

    Update kimi-cli config.toml.

**Parameters:**

    - ``request`` (*UpdateConfigTomlRequest*)
    - ``http_request`` (*Request*)

**Returns:** ``UpdateConfigTomlResponse``

**Calls:**

    - :ref:`UpdateConfigTomlResponse <func-UpdateConfigTomlResponse>`
    - :ref:`get_config_file <func-get_config_file>`
    - :ref:`load_config_from_string <func-load_config_from_string>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`put <func-put>`
    - :ref:`str <func-str>`
    - :ref:`warning <func-warning>`
    - :ref:`write_text <func-write_text>`


.. _func-update_global_config:

update_global_config
^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.config``

**File:** :file:`src/kimi_cli/web/api/config.py` (line 164)

**Description:**

    Update global (kimi-cli) default model/thinking.

**Parameters:**

    - ``request`` (*UpdateGlobalConfigRequest*)
    - ``http_request`` (*Request*)
    - ``runner`` (*KimiCLIRunner*)

**Returns:** ``UpdateGlobalConfigResponse``

**Calls:**

    - :ref:`Depends <func-Depends>`
    - :ref:`HTTPException <func-HTTPException>`
    - :ref:`UpdateGlobalConfigResponse <func-UpdateGlobalConfigResponse>`
    - :ref:`load_config <func-load_config>`
    - :ref:`save_config <func-save_config>`
    - :ref:`_build_global_config <func-_build_global_config>`
    - :ref:`_ensure_sensitive_apis_allowed <func-_ensure_sensitive_apis_allowed>`
    - :ref:`patch <func-patch>`
    - :ref:`restart_running_workers <func-restart_running_workers>`
    - :ref:`str <func-str>`


.. _func-update_session:

update_session
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 783)

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
    - :ref:`time <func-time>`


.. _func-upload_session_file:

upload_session_file
^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.web.api.sessions``

**File:** :file:`src/kimi_cli/web/api/sessions.py` (line 593)

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
    - :ref:`uuid4 <func-uuid4>`
    - :ref:`write_bytes <func-write_bytes>`


.. _func-usage:

usage
^^^^^

**Module:** ``kimi_cli.ui.shell.usage``

**File:** :file:`src/kimi_cli/ui/shell/usage.py` (line 166)

**Description:**

    Display API usage and quota information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`command <func-command>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`_build_usage_panel <func-_build_usage_panel>`
    - :ref:`_fetch_usage <func-_fetch_usage>`
    - :ref:`_parse_usage_payload <func-_parse_usage_payload>`
    - :ref:`_usage_url <func-_usage_url>`
    - :ref:`print <func-print>`
    - :ref:`resolve_api_key <func-resolve_api_key>`
    - :ref:`status <func-status>`



V
-

.. _func-validate_flow:

validate_flow
^^^^^^^^^^^^^

**Module:** ``kimi_cli.skill.flow.__init__``

**File:** :file:`src/kimi_cli/skill/flow/__init__.py` (line 46)

**Description:**

    Validate Flow.
    
    Args:
    nodes: Description.
    outgoing: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``nodes``
    - ``outgoing``

**Calls:**

    - :ref:`FlowValidationError <func-FlowValidationError>`
    - :ref:`add <func-add>`
    - :ref:`append <func-append>`
    - :ref:`get <func-get>`
    - :ref:`len <func-len>`
    - :ref:`pop <func-pop>`
    - :ref:`set <func-set>`
    - :ref:`strip <func-strip>`
    - :ref:`values <func-values>`

**Called by:**

    - :ref:`parse_d2_flowchart <func-parse_d2_flowchart>` (from ``kimi_cli.skill.flow.d2``)
    - :ref:`parse_mermaid_flowchart <func-parse_mermaid_flowchart>` (from ``kimi_cli.skill.flow.mermaid``)


.. _func-verify_token:

verify_token
^^^^^^^^^^^^

**Module:** ``kimi_cli.web.auth``

**File:** :file:`src/kimi_cli/web/auth.py` (line 136)

**Description:**

    Verify token using timing-safe comparison.

**Parameters:**

    - ``provided`` (*str | None*)
    - ``expected`` (*str*)

**Returns:** ``bool``

**Calls:**

    - :ref:`timing_safe_compare <func-timing_safe_compare>`

**Called by:**

    - :ref:`session_stream <func-session_stream>` (from ``kimi_cli.web.api.sessions``)
    - :ref:`dispatch <func-dispatch>` (from ``kimi_cli.web.auth.AuthMiddleware``)


.. _func-version:

version
^^^^^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 132)

**Description:**

    Show version information

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`print <func-print>`

**Called by:**

    - :ref:`_common_headers <func-_common_headers>` (from ``kimi_cli.auth.oauth``)
    - :ref:`detect <func-detect>` (from ``kimi_cli.utils.environment.Environment``)


.. _func-visualize:

visualize
^^^^^^^^^

**Module:** ``kimi_cli.ui.print.visualize``

**File:** :file:`src/kimi_cli/ui/print/visualize.py` (line 185)

**Description:**

    Visualize.
    
    Args:
    output\_format: Description.
    final\_only: Description.
    wire: Description.
    
    Returns:
        Description.

**Parameters:**

    - ``output_format`` (*OutputFormat*)
    - ``final_only`` (*bool*)
    - ``wire`` (*Wire*)

**Returns:** ``None``

**Calls:**

    - :ref:`FinalOnlyJsonPrinter <func-FinalOnlyJsonPrinter>`
    - :ref:`FinalOnlyTextPrinter <func-FinalOnlyTextPrinter>`
    - :ref:`TextPrinter <func-TextPrinter>`
    - :ref:`feed <func-feed>`
    - :ref:`flush <func-flush>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`receive <func-receive>`
    - :ref:`ui_side <func-ui_side>`


.. _func-visualize:

visualize
^^^^^^^^^

**Module:** ``kimi_cli.ui.shell.visualize``

**File:** :file:`src/kimi_cli/ui/shell/visualize.py` (line 150)

**Description:**

    A loop to consume agent events and visualize the agent behavior.

    Args:
        wire: Communication channel with the agent
        initial\_status: Initial status snapshot
        cancel\_event: Eve
    ...

**Parameters:**

    - ``wire`` (*WireUISide*)
    - ``initial_status`` (*StatusUpdate*)
    - ``cancel_event`` (*asyncio.Event | None*) = ``None``

**Calls:**

    - :ref:`_LiveView <func-_LiveView>`
    - :ref:`visualize_loop <func-visualize_loop>`

**Called by:**

    - :ref:`run_soul_command <func-run_soul_command>` (from ``kimi_cli.ui.shell.__init__.Shell``)
    - :ref:`replay_recent_history <func-replay_recent_history>` (from ``kimi_cli.ui.shell.replay``)



W
-

.. _func-web:

web
^^^

**Module:** ``kimi_cli.cli.web``

**File:** :file:`src/kimi_cli/cli/web.py` (line 9)

**Description:**

    Run Kimi Code CLI web interface.

**Parameters:**

    - ``ctx`` (*typer.Context*)
    - ``host`` = ``None``
    - ``network`` = ``False``
    - ``port`` = ``5494``
    - ``reload`` = ``False``
    - ``open_browser`` = ``True``
    - ``auth_token`` = ``None``
    - ``allowed_origins`` = ``None``
    - ``dangerously_omit_auth`` = ``False``
    - ``restrict_sensitive_apis`` = ``None``
    - ``lan_only`` = ``True``

**Calls:**

    - :ref:`Option <func-Option>`
    - :ref:`callback <func-callback>`
    - :ref:`run_web_server <func-run_web_server>`


.. _func-web:

web
^^^

**Module:** ``kimi_cli.ui.shell.slash``

**File:** :file:`src/kimi_cli/ui/shell/slash.py` (line 358)

**Description:**

    Open Kimi Code Web UI in browser

**Parameters:**

    - ``app`` (*Shell*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`SwitchToWeb <func-SwitchToWeb>`
    - :ref:`_ensure_kimi_soul <func-_ensure_kimi_soul>`


.. _func-web_worker:

web_worker
^^^^^^^^^^

**Module:** ``kimi_cli.cli.__init__``

**File:** :file:`src/kimi_cli/cli/__init__.py` (line 765)

**Description:**

    Run web worker subprocess (internal).

**Parameters:**

    - ``session_id`` (*str*)

**Returns:** ``None``

**Calls:**

    - :ref:`BadParameter <func-BadParameter>`
    - :ref:`UUID <func-UUID>`
    - :ref:`command <func-command>`
    - :ref:`enable_logging <func-enable_logging>`
    - :ref:`run_worker <func-run_worker>`


.. _func-Wire.join:

Wire.join
^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 153)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`exception <func-exception>`
    - :ref:`join <func-join>`


.. _func-Wire.shutdown:

Wire.shutdown
^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 147)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`flush <func-flush>`
    - :ref:`shutdown <func-shutdown>`


.. _func-Wire.soul_side:

Wire.soul_side
^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 132)

**Parameters:**

    - ``self``

**Returns:** ``WireSoulSide``


.. _func-Wire.ui_side:

Wire.ui_side
^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 135)

**Description:**

    Create a UI side of the \`Wire\`.

        Args:
            merge: Whether to merge \`Wire\` messages as much as possible.

**Parameters:**

    - ``self``
    - ``merge`` (*bool*)

**Returns:** ``WireUISide``

**Calls:**

    - :ref:`WireUISide <func-WireUISide>`
    - :ref:`subscribe <func-subscribe>`


.. _func-wire_send:

wire_send
^^^^^^^^^

**Module:** ``kimi_cli.soul.__init__``

**File:** :file:`src/kimi_cli/soul/__init__.py` (line 142)

**Description:**

    Send a wire message to the current wire.
    Take this as \`print\` and \`input\` for souls.
    Souls should always use this function to send wire messages.

**Parameters:**

    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`get_wire_or_none <func-get_wire_or_none>`
    - :ref:`send <func-send>`

**Called by:**

    - :ref:`_flow_turn <func-_flow_turn>` (from ``kimi_cli.soul.kimisoul.FlowRunner``)
    - :ref:`_agent_loop <func-_agent_loop>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_make_skill_runner <func-_make_skill_runner>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`_step <func-_step>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`compact_context <func-compact_context>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`run <func-run>` (from ``kimi_cli.soul.kimisoul.KimiSoul``)
    - :ref:`clear <func-clear>` (from ``kimi_cli.soul.slash``)
    - :ref:`compact <func-compact>` (from ``kimi_cli.soul.slash``)
    - :ref:`yolo <func-yolo>` (from ``kimi_cli.soul.slash``)


.. _func-WireFile.append_message:

WireFile.append_message
^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 140)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)
    - ``timestamp`` (*float | None*) = ``None``

**Returns:** ``None``

**Calls:**

    - :ref:`append_record <func-append_record>`
    - :ref:`from_wire_message <func-from_wire_message>`
    - :ref:`time <func-time>`


.. _func-WireFile.append_record:

WireFile.append_record
^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 147)

**Parameters:**

    - ``self``
    - ``record`` (*WireMessageRecord*)

**Returns:** ``None``

**Calls:**

    - :ref:`WireFileMetadata <func-WireFileMetadata>`
    - :ref:`exists <func-exists>`
    - :ref:`_dump_line <func-_dump_line>`
    - :ref:`mkdir <func-mkdir>`
    - :ref:`open <func-open>`
    - :ref:`stat <func-stat>`
    - :ref:`write <func-write>`


.. _func-WireFile.is_empty:

WireFile.is_empty
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 101)

**Parameters:**

    - ``self``

**Returns:** ``bool``

**Calls:**

    - :ref:`exception <func-exception>`
    - :ref:`exists <func-exists>`
    - :ref:`parse_wire_file_metadata <func-parse_wire_file_metadata>`
    - :ref:`open <func-open>`
    - :ref:`strip <func-strip>`


.. _func-WireFile.iter_records:

WireFile.iter_records
^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 118)

**Parameters:**

    - ``self``

**Returns:** ``AsyncIterator[WireMessageRecord]``

**Calls:**

    - :ref:`exception <func-exception>`
    - :ref:`exists <func-exists>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`parse_wire_file_line <func-parse_wire_file_line>`
    - :ref:`open <func-open>`
    - :ref:`strip <func-strip>`


.. _func-WireFile.version:

WireFile.version
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 98)

**Parameters:**

    - ``self``

**Returns:** ``str``


.. _func-WireMessageEnvelope.from_wire_message:

WireMessageEnvelope.from_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 359)

**Parameters:**

    - ``cls``
    - ``msg`` (*WireMessage*)

**Returns:** ``WireMessageEnvelope``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`issubclass <func-issubclass>`
    - :ref:`items <func-items>`
    - :ref:`model_dump <func-model_dump>`
    - :ref:`type <func-type>`


.. _func-WireMessageEnvelope.to_wire_message:

WireMessageEnvelope.to_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.types``

**File:** :file:`src/kimi_cli/wire/types.py` (line 371)

**Description:**

    Convert the envelope back into a \`WireMessage\`.

        Raises:
            ValueError: If the message type is unknown or the payload is invalid.

**Parameters:**

    - ``self``

**Returns:** ``WireMessage``

**Calls:**

    - :ref:`ValueError <func-ValueError>`
    - :ref:`get <func-get>`
    - :ref:`model_validate <func-model_validate>`


.. _func-WireMessageRecord.from_wire_message:

WireMessageRecord.from_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 31)

**Parameters:**

    - ``cls``
    - ``msg`` (*WireMessage*)
    - ``timestamp`` (*float*)

**Returns:** ``WireMessageRecord``

**Calls:**

    - :ref:`cls <func-cls>`
    - :ref:`from_wire_message <func-from_wire_message>`


.. _func-WireMessageRecord.to_wire_message:

WireMessageRecord.to_wire_message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.file``

**File:** :file:`src/kimi_cli/wire/file.py` (line 34)

**Parameters:**

    - ``self``

**Returns:** ``WireMessage``

**Calls:**

    - :ref:`to_wire_message <func-to_wire_message>`


.. _func-WireServer.serve:

WireServer.serve
^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.server``

**File:** :file:`src/kimi_cli/wire/server.py` (line 70)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`Event <func-Event>`
    - :ref:`_read_loop <func-_read_loop>`
    - :ref:`_shutdown <func-_shutdown>`
    - :ref:`_write_loop <func-_write_loop>`
    - :ref:`cancel <func-cancel>`
    - :ref:`create_task <func-create_task>`
    - :ref:`done <func-done>`
    - :ref:`get_running_loop <func-get_running_loop>`
    - :ref:`info <func-info>`
    - :ref:`is_set <func-is_set>`
    - :ref:`install_sigint_handler <func-install_sigint_handler>`
    - :ref:`remove_sigint <func-remove_sigint>`
    - :ref:`result <func-result>`
    - :ref:`stdio_streams <func-stdio_streams>`
    - :ref:`suppress <func-suppress>`
    - :ref:`wait <func-wait>`


.. _func-WireSoulSide.flush:

WireSoulSide.flush
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 86)

**Parameters:**

    - ``self``

**Returns:** ``None``

**Calls:**

    - :ref:`_send_merged <func-_send_merged>`
    - :ref:`is_wire_message <func-is_wire_message>`


.. _func-WireSoulSide.send:

WireSoulSide.send
^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 62)

**Parameters:**

    - ``self``
    - ``msg`` (*WireMessage*)

**Returns:** ``None``

**Calls:**

    - :ref:`_send_merged <func-_send_merged>`
    - :ref:`debug <func-debug>`
    - :ref:`deepcopy <func-deepcopy>`
    - :ref:`flush <func-flush>`
    - :ref:`info <func-info>`
    - :ref:`isinstance <func-isinstance>`
    - :ref:`merge_in_place <func-merge_in_place>`
    - :ref:`publish_nowait <func-publish_nowait>`


.. _func-WireUISide.receive:

WireUISide.receive
^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.wire.__init__``

**File:** :file:`src/kimi_cli/wire/__init__.py` (line 108)

**Parameters:**

    - ``self``

**Returns:** ``WireMessage``

**Calls:**

    - :ref:`debug <func-debug>`
    - :ref:`get <func-get>`
    - :ref:`isinstance <func-isinstance>`


.. _func-WorkDirMeta.sessions_dir:

WorkDirMeta.sessions_dir
^^^^^^^^^^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.metadata``

**File:** :file:`src/kimi_cli/metadata.py` (line 46)

**Description:**

    The directory to store sessions for this work directory.

**Parameters:**

    - ``self``

**Returns:** ``Path``

**Calls:**

    - :ref:`encode <func-encode>`
    - :ref:`hexdigest <func-hexdigest>`
    - :ref:`get_share_dir <func-get_share_dir>`
    - :ref:`md5 <func-md5>`
    - :ref:`mkdir <func-mkdir>`


.. _func-wrap_media_part:

wrap_media_part
^^^^^^^^^^^^^^^

**Module:** ``kimi_cli.utils.media_tags``

**File:** :file:`src/kimi_cli/utils/media_tags.py` (line 43)

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

    - :ref:`_read_media <func-_read_media>` (from ``kimi_cli.tools.file.read_media.ReadMediaFile``)
    - :ref:`load_content_parts <func-load_content_parts>` (from ``kimi_cli.ui.shell.prompt.AttachmentCache``)



Y
-

.. _func-yolo:

yolo
^^^^

**Module:** ``kimi_cli.soul.slash``

**File:** :file:`src/kimi_cli/soul/slash.py` (line 69)

**Description:**

    Toggle YOLO mode (auto-approve all actions)

**Parameters:**

    - ``soul`` (*KimiSoul*)
    - ``args`` (*str*)

**Calls:**

    - :ref:`TextPart <func-TextPart>`
    - :ref:`is_yolo <func-is_yolo>`
    - :ref:`set_yolo <func-set_yolo>`
    - :ref:`wire_send <func-wire_send>`

