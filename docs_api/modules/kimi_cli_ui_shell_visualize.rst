kimi_cli.ui.shell.visualize
===========================

.. module:: kimi_cli.ui.shell.visualize

Source: :file:`src/kimi_cli/ui/shell/visualize.py`

Functions
---------

.. _kimi_cli.ui.shell.visualize.visualize:

visualize
^^^^^^^^^

**Line:** 150

**Description:**

    A loop to consume agent events and visualize the agent behavior.

    Args:
        wire: Communication channel with the agent
        initial\_status: Initial status snapshot
        cancel\_event: Eve

**Parameters:**

    - ``wire`` (*WireUISide*)
    - ``initial_status`` (*StatusUpdate*)
    - ``cancel_event`` (*asyncio.Event | None*) = ``None``

**Calls:**

    - :ref:`_LiveView <func-_LiveView>`
    - :ref:`visualize_loop <func-visualize_loop>`

**Called by:**

    - ``kimi_cli.ui.shell.__init__.Shell.run_soul_command``
    - ``kimi_cli.ui.shell.replay.replay_recent_history``


Methods
-------

- ``_ApprovalRequestPanel.get_selected_response`` - Line 473
- ``_ApprovalRequestPanel.move_down`` - Line 469
- ``_ApprovalRequestPanel.move_up`` - Line 465
- ``_ApprovalRequestPanel.render`` - Line 411
- ``_ApprovalRequestPanel.render_full`` - Line 461
- ``_ContentBlock.append`` - Line 188
- ``_ContentBlock.compose`` - Line 176
- ``_ContentBlock.compose_final`` - Line 179
- ``_LiveView.append_content`` - Line 712
- ``_LiveView.append_tool_call`` - Line 730
- ``_LiveView.append_tool_call_part`` - Line 736
- ``_LiveView.append_tool_result`` - Line 744
- ``_LiveView.cleanup`` - Line 670
- ``_LiveView.compose`` - Line 562
- ``_LiveView.dispatch_keyboard_event`` - Line 631
- ``_LiveView.dispatch_wire_message`` - Line 579
- ``_LiveView.flush_content`` - Line 691
- ``_LiveView.flush_finished_tool_calls`` - Line 698
- ``_LiveView.handle_subagent_event`` - Line 782
- ``_LiveView.refresh_soon`` - Line 559
- ``_LiveView.request_approval`` - Line 750
- ``_LiveView.show_next_approval_request`` - Line 762
- ``_LiveView.visualize_loop`` - Line 507
- ``_StatusBlock.render`` - Line 143
- ``_StatusBlock.update`` - Line 146
- ``_ToolCallBlock.append_args_part`` - Line 225
- ``_ToolCallBlock.append_sub_tool_call`` - Line 242
- ``_ToolCallBlock.append_sub_tool_call_part`` - Line 246
- ``_ToolCallBlock.compose`` - Line 218
- ``_ToolCallBlock.finish`` - Line 238
- ``_ToolCallBlock.finish_sub_tool_call`` - Line 256
- ``_ToolCallBlock.finished`` - Line 222

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_keyboard_listener`` - Line 89
- ``_show_approval_in_pager`` - Line 118
