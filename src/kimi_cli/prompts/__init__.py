from __future__ import annotations
from pathlib import Path

COMPACT = (Path(__file__).parent / "compact.md").read_text(encoding="utf-8")

INIT = (Path(__file__).parent / "init.md").read_text(encoding="utf-8")
