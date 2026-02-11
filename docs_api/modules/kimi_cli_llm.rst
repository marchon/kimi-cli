kimi_cli.llm
============

.. module:: kimi_cli.llm

Source: :file:`src/kimi_cli/llm.py`

Classes
-------

.. _class-LLM:

LLM
^^^

LLM class.


Functions
---------

.. _kimi_cli.llm.augment_provider_with_env_vars:

augment_provider_with_env_vars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 53

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

    - ``kimi_cli.app.KimiCLI.create``


.. _kimi_cli.llm.create_llm:

create_llm
^^^^^^^^^^

**Line:** 183

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
    - ... and 12 more

**Called by:**

    - ``kimi_cli.acp.server.ACPServer.set_session_model``
    - ``kimi_cli.app.KimiCLI.create``
    - ``kimi_cli.web.api.sessions.generate_session_title``


.. _kimi_cli.llm.derive_model_capabilities:

derive_model_capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^

**Line:** 15

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

    - ``kimi_cli.acp.server._expand_llm_models``
    - ``kimi_cli.llm.create_llm``
    - ``kimi_cli.ui.shell.slash.model``
    - ``kimi_cli.web.api.config._build_global_config``


.. _kimi_cli.llm.model_display_name:

model_display_name
^^^^^^^^^^^^^^^^^^

**Line:** 93

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

    - ``kimi_cli.app.KimiCLI.run_shell``


Methods
-------

- ``LLM.model_name`` - Line 46

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_kimi_default_headers`` - Line 138
- ``_load_scripted_echo_scripts`` - Line 156
