kimi_cli.utils.rich.markdown
============================

.. module:: kimi_cli.utils.rich.markdown

Source: :file:`src/kimi_cli/utils/rich/markdown.py`

Classes
-------

.. _class-BlockQuote:

BlockQuote
^^^^^^^^^^

A block quote.


.. _class-CodeBlock:

CodeBlock
^^^^^^^^^

A code block with syntax highlighting.


.. _class-Heading:

Heading
^^^^^^^

A heading.


.. _class-HorizontalRule:

HorizontalRule
^^^^^^^^^^^^^^

A horizontal rule to divide sections.


.. _class-ImageItem:

ImageItem
^^^^^^^^^

Renders a placeholder for an image.


.. _class-Link:

Link
^^^^

Link class.


.. _class-ListElement:

ListElement
^^^^^^^^^^^

A list element.


.. _class-ListItem:

ListItem
^^^^^^^^

An item in a list.


.. _class-Markdown:

Markdown
^^^^^^^^

A Markdown renderable.

    Args:
        markup (str): A string containing markdown.
        code\_theme (str, optional): Pygments theme for code blocks. Defaults to "kimi-ansi".
            See https://pygments.org/styles/ for code themes.
        justify (JustifyMethod, optional): Justify value fo
...


.. _class-MarkdownContext:

MarkdownContext
^^^^^^^^^^^^^^^

Manages the console render state.


.. _class-MarkdownElement:

MarkdownElement
^^^^^^^^^^^^^^^

MarkdownElement class.


.. _class-Paragraph:

Paragraph
^^^^^^^^^

A Paragraph.


.. _class-TableBodyElement:

TableBodyElement
^^^^^^^^^^^^^^^^

MarkdownElement corresponding to \`tbody\_open\` and \`tbody\_close\`.


.. _class-TableDataElement:

TableDataElement
^^^^^^^^^^^^^^^^

MarkdownElement corresponding to \`td\_open\` and \`td\_close\`
    and \`th\_open\` and \`th\_close\`.


.. _class-TableElement:

TableElement
^^^^^^^^^^^^

MarkdownElement corresponding to \`table\_open\`.


.. _class-TableHeaderElement:

TableHeaderElement
^^^^^^^^^^^^^^^^^^

MarkdownElement corresponding to \`thead\_open\` and \`thead\_close\`.


.. _class-TableRowElement:

TableRowElement
^^^^^^^^^^^^^^^

MarkdownElement corresponding to \`tr\_open\` and \`tr\_close\`.


.. _class-TextElement:

TextElement
^^^^^^^^^^^

Base class for elements that render text.


.. _class-UnknownElement:

UnknownElement
^^^^^^^^^^^^^^

An unknown element.

    Hopefully there will be no unknown elements, and we will have a MarkdownElement for
    everything in the document.


Methods
-------

- ``BlockQuote.on_child_close`` - Line 259
- ``CodeBlock.create`` - Line 226
- ``Heading.create`` - Line 195
- ``Heading.on_enter`` - Line 198
- ``ImageItem.create`` - Line 512
- ``ImageItem.on_enter`` - Line 530
- ``Link.create`` - Line 498
- ``ListElement.create`` - Line 380
- ``ListElement.on_child_close`` - Line 388
- ``ListItem.create`` - Line 425
- ``ListItem.on_child_close`` - Line 434
- ``ListItem.render_bullet`` - Line 438
- ``ListItem.render_number`` - Line 464
- ``MarkdownContext.current_style`` - Line 566
- ``MarkdownContext.enter_style`` - Line 581
- ``MarkdownContext.leave_style`` - Line 601
- ``MarkdownContext.on_text`` - Line 570
- ``MarkdownElement.create`` - Line 30
- ``MarkdownElement.on_child_close`` - Line 63
- ``MarkdownElement.on_enter`` - Line 42
- ``MarkdownElement.on_leave`` - Line 56
- ``MarkdownElement.on_text`` - Line 49
- ``Paragraph.create`` - Line 181
- ``TableBodyElement.on_child_close`` - Line 330
- ``TableDataElement.create`` - Line 351
- ``TableDataElement.on_text`` - Line 371
- ``TableElement.on_child_close`` - Line 290
- ``TableHeaderElement.on_child_close`` - Line 319
- ``TableRowElement.on_child_close`` - Line 341
- ``TextElement.on_enter`` - Line 164
- ``TextElement.on_leave`` - Line 171
- ``TextElement.on_text`` - Line 168

Internal Functions
------------------

.. note::
   These functions are for internal use only and may change without notice.

- ``_strip_background`` - Line 127
