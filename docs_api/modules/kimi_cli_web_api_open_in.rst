kimi_cli.web.api.open_in
========================

.. module:: kimi_cli.web.api.open_in

Source: :file:`src/kimi_cli/web/api/open_in.py`

Classes
-------

.. _class-OpenInRequest:

OpenInRequest
^^^^^^^^^^^^^

Open path in a local app.


.. _class-OpenInResponse:

OpenInResponse
^^^^^^^^^^^^^^

Open path response.


Functions
---------

.. _kimi_cli.web.api.open_in.open_in:

open_in
^^^^^^^

**Line:** 141

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
    - ... and 2 more


Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_open_app`` - Line 80
- ``_open_iterm`` - Line 114
- ``_open_terminal`` - Line 101
- ``_resolve_path`` - Line 62
- ``_run_command`` - Line 45
