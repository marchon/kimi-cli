from typing import Literal
from kosong.tooling import DisplayBlock
from pydantic import BaseModel

class DiffDisplayBlock(DisplayBlock):
    """Display block describing a file diff."""

    type: str = "diff"
    path: str
    old_text: str
    new_text: str

class ShellDisplayBlock(DisplayBlock):
    """Display block describing a shell command."""

    type: str = "shell"
    language: str
    command: str

class TodoDisplayBlock(DisplayBlock):
    """Display block describing a todo list update."""

    type: str = "todo"
    items: list[TodoDisplayItem]

class TodoDisplayItem(BaseModel):
    """
    TodoDisplayItem class.
    """
    title: str
    status: Literal["pending", "in_progress", "done"]
