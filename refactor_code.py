#!/usr/bin/env python3
"""
Code refactoring script for Kimi Code CLI.

This script refactors Python files to:
1. Move public functions/classes to the top with proper documentation
2. Move internal functions (starting with _) to the bottom in alphabetical order
3. Add internal function indexes
4. Add Sphinx-compatible docstrings where missing
5. Handle forward references correctly via dependency analysis
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class CodeBlock:
    """Represents a block of code (function, class, import, etc.)."""

    name: str
    node: ast.AST
    source: str
    is_public: bool
    is_class: bool
    is_import: bool
    docstring: str | None = None
    defined_names: set[str] = field(default_factory=set)
    used_names: set[str] = field(default_factory=set)


def get_docstring(node: ast.AST, source_lines: list[str]) -> str | None:
    """Extract docstring from an AST node."""
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
        if node.body and isinstance(node.body[0], ast.Expr):
            if isinstance(node.body[0].value, ast.Constant) and isinstance(
                node.body[0].value.value, str
            ):
                return node.body[0].value.value
    return None


def is_public(name: str) -> bool:
    """Check if a name is public (doesn't start with underscore)."""
    return not name.startswith("_")


def extract_node_source(node: ast.AST, source_lines: list[str]) -> str:
    """Extract source code for an AST node."""
    start_line = node.lineno - 1
    end_line = node.end_lineno
    
    # For decorated classes/functions, include the decorators
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        if node.decorator_list:
            # Find the line of the first decorator
            first_decorator_line = min(d.lineno for d in node.decorator_list)
            start_line = first_decorator_line - 1
    
    return "\n".join(source_lines[start_line:end_line])


class NameAnalyzer(ast.NodeVisitor):
    """Analyze which names are defined and used in a code block."""

    def __init__(self):
        self.defined: set[str] = set()
        self.used: set[str] = set()
        self.in_annotation = False

    def visit_Name(self, node: ast.Name):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            if not self.in_annotation:
                self.used.add(node.id)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Function name is defined
        self.defined.add(node.name)
        # Don't visit decorators and defaults as "used" in the function body
        # Just analyze the body
        for stmt in node.body:
            self.visit(stmt)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.defined.add(node.name)
        for stmt in node.body:
            self.visit(stmt)

    def visit_ClassDef(self, node: ast.ClassDef):
        # Class name is defined
        self.defined.add(node.name)
        # Analyze class body
        for stmt in node.body:
            self.visit(stmt)

    def visit_Assign(self, node: ast.Assign):
        # For assignments, names on the left are defined, everything on right is used
        # For subscript assignments like obj[key] = value, obj is used, not defined
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined.add(target.id)
            elif isinstance(target, ast.Tuple):
                for elt in target.elts:
                    if isinstance(elt, ast.Name):
                        self.defined.add(elt.id)
            elif isinstance(target, ast.Subscript):
                # For subscript assignment, the subscripted object is used, not defined
                if isinstance(target.value, ast.Name):
                    self.used.add(target.value.id)
                # Visit the slice (which may contain names)
                self.visit(target.slice)
        self.visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        # For annotated assignments, target is defined
        if isinstance(node.target, ast.Name):
            self.defined.add(node.target.id)
        if node.value:
            self.visit(node.value)
        # Visit annotation but mark as annotation context
        old_in_annotation = self.in_annotation
        self.in_annotation = True
        self.visit(node.annotation)
        self.in_annotation = old_in_annotation

    def visit_Arg(self, node: ast.arg):
        # Argument names are defined in the scope
        self.defined.add(node.arg)
        if node.annotation:
            old_in_annotation = self.in_annotation
            self.in_annotation = True
            self.visit(node.annotation)
            self.in_annotation = old_in_annotation

    def visit_TypeAlias(self, node: ast.TypeAlias):
        # Type alias name is defined
        if isinstance(node.name, ast.Name):
            self.defined.add(node.name.id)
        # Visit the value
        self.visit(node.value)

    def visit_arg(self, node: ast.arg):
        self.visit_Arg(node)


def analyze_names(node: ast.AST) -> tuple[set[str], set[str]]:
    """Analyze which names are defined and used in a node."""
    analyzer = NameAnalyzer()
    analyzer.visit(node)
    return analyzer.defined, analyzer.used


def get_default_value_names(node: ast.AST) -> set[str]:
    """Get names used in default argument values and decorators."""
    names: set[str] = set()

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        # Check default values
        for default in node.args.defaults:
            for child in ast.walk(default):
                if isinstance(child, ast.Name):
                    names.add(child.id)
        for default in node.args.kw_defaults:
            if default:
                for child in ast.walk(default):
                    if isinstance(child, ast.Name):
                        names.add(child.id)
        # Check decorators
        for decorator in node.decorator_list:
            for child in ast.walk(decorator):
                if isinstance(child, ast.Name):
                    names.add(child.id)

    elif isinstance(node, ast.ClassDef):
        # Check base classes
        for base in node.bases:
            for child in ast.walk(base):
                if isinstance(child, ast.Name):
                    names.add(child.id)
        # Check decorators
        for decorator in node.decorator_list:
            for child in ast.walk(decorator):
                if isinstance(child, ast.Name):
                    names.add(child.id)

    elif isinstance(node, ast.AnnAssign):
        # Check annotation
        for child in ast.walk(node.annotation):
            if isinstance(child, ast.Name):
                names.add(child.id)

    elif isinstance(node, ast.Assign):
        # Check the value being assigned
        for child in ast.walk(node.value):
            if isinstance(child, ast.Name):
                names.add(child.id)

    return names


def parse_file(filepath: Path) -> list[CodeBlock]:
    """Parse a Python file and extract code blocks with dependency info."""
    source = filepath.read_text(encoding="utf-8")
    source_lines = source.split("\n")

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return []

    blocks: list[CodeBlock] = []

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            block_source = extract_node_source(node, source_lines)
            blocks.append(
                CodeBlock(
                    name="__imports__",
                    node=node,
                    source=block_source,
                    is_public=True,
                    is_class=False,
                    is_import=True,
                )
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            docstring = get_docstring(node, source_lines)
            block_source = extract_node_source(node, source_lines)
            defined, used = analyze_names(node)
            # Also get names from default values and decorators
            default_names = get_default_value_names(node)
            used.update(default_names)
            blocks.append(
                CodeBlock(
                    name=name,
                    node=node,
                    source=block_source,
                    is_public=is_public(name),
                    is_class=False,
                    is_import=False,
                    docstring=docstring,
                    defined_names=defined,
                    used_names=used,
                )
            )
        elif isinstance(node, ast.ClassDef):
            name = node.name
            docstring = get_docstring(node, source_lines)
            block_source = extract_node_source(node, source_lines)
            defined, used = analyze_names(node)
            # Also get names from base classes and decorators
            default_names = get_default_value_names(node)
            used.update(default_names)
            blocks.append(
                CodeBlock(
                    name=name,
                    node=node,
                    source=block_source,
                    is_public=is_public(name),
                    is_class=True,
                    is_import=False,
                    docstring=docstring,
                    defined_names=defined,
                    used_names=used,
                )
            )
        elif isinstance(node, ast.Assign):
            block_source = extract_node_source(node, source_lines)
            name = "__assign__"
            if node.targets and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
            defined, used = analyze_names(node)
            default_names = get_default_value_names(node)
            used.update(default_names)
            blocks.append(
                CodeBlock(
                    name=name,
                    node=node,
                    source=block_source,
                    is_public=is_public(name),
                    is_class=False,
                    is_import=False,
                    defined_names=defined,
                    used_names=used,
                )
            )
        elif isinstance(node, ast.AnnAssign):
            block_source = extract_node_source(node, source_lines)
            name = "__assign__"
            if isinstance(node.target, ast.Name):
                name = node.target.id
            defined, used = analyze_names(node)
            default_names = get_default_value_names(node)
            used.update(default_names)
            blocks.append(
                CodeBlock(
                    name=name,
                    node=node,
                    source=block_source,
                    is_public=is_public(name),
                    is_class=False,
                    is_import=False,
                    defined_names=defined,
                    used_names=used,
                )
            )
        elif isinstance(node, ast.Expr):
            block_source = extract_node_source(node, source_lines)
            # Check if this is a docstring (just a string literal)
            is_docstring = isinstance(node.value, ast.Constant) and isinstance(
                node.value.value, str
            )
            if is_docstring:
                # Docstrings don't need dependency analysis
                blocks.append(
                    CodeBlock(
                        name="__expr__",
                        node=node,
                        source=block_source,
                        is_public=True,
                        is_class=False,
                        is_import=False,
                    )
                )
            else:
                # Other expressions (like cli.add_typer(...)) need dependency analysis
                defined, used = analyze_names(node)
                # Generate a unique name for this expression block
                expr_name = f"__stmt_{len(blocks)}__"
                blocks.append(
                    CodeBlock(
                        name=expr_name,
                        node=node,
                        source=block_source,
                        is_public=True,
                        is_class=False,
                        is_import=False,
                        defined_names=defined,
                        used_names=used,
                    )
                )
        elif isinstance(node, ast.TypeAlias):
            block_source = extract_node_source(node, source_lines)
            name = node.name.id if isinstance(node.name, ast.Name) else "__type_alias__"
            defined, used = analyze_names(node)
            blocks.append(
                CodeBlock(
                    name=name,
                    node=node,
                    source=block_source,
                    is_public=is_public(name),
                    is_class=False,
                    is_import=False,
                    defined_names=defined,
                    used_names=used,
                )
            )
        elif isinstance(node, ast.If):
            # Handle if statements (e.g., version checks with class definitions)
            # Treat the entire if block as a single unit
            block_source = extract_node_source(node, source_lines)
            # Analyze all names defined and used within the if block
            defined: set[str] = set()
            used: set[str] = set()
            for child in ast.walk(node):
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    defined.add(child.name)
                elif isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load):
                    used.add(child.id)
                elif isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            defined.add(target.id)
                elif isinstance(child, ast.AnnAssign):
                    if isinstance(child.target, ast.Name):
                        defined.add(child.target.id)
            # Remove defined names from used (they're local to the if block)
            used -= defined
            blocks.append(
                CodeBlock(
                    name=f"__if_{len(blocks)}__",
                    node=node,
                    source=block_source,
                    is_public=True,  # If blocks are typically public
                    is_class=False,
                    is_import=False,
                    defined_names=defined,
                    used_names=used,
                )
            )

    return blocks


def build_dependency_graph(blocks: list[CodeBlock]) -> dict[str, set[str]]:
    """Build a dependency graph showing which blocks depend on which."""
    # Map from name to block that defines it
    name_to_block: dict[str, CodeBlock] = {}
    for block in blocks:
        for name in block.defined_names:
            name_to_block[name] = block

    # Build dependency graph: block -> set of blocks it depends on
    graph: dict[str, set[str]] = {}
    for block in blocks:
        deps: set[str] = set()
        for used_name in block.used_names:
            if used_name in name_to_block:
                dep_block = name_to_block[used_name]
                if dep_block.name != block.name:
                    deps.add(dep_block.name)
        graph[block.name] = deps

    return graph


def topological_sort_with_priority(
    blocks: list[CodeBlock], graph: dict[str, set[str]]
) -> list[CodeBlock]:
    """
    Topological sort with priority: public first, then internal alphabetically.

    Respects dependencies: if A depends on B, B must come before A.
    Within dependency constraints, tries to put public before internal,
    and sorts alphabetically within each group.
    """
    block_map = {b.name: b for b in blocks}

    # Track which blocks have been visited
    visited: set[str] = set()
    result: list[CodeBlock] = []

    # Build in-degree map
    in_degree: dict[str, int] = {}
    for block in blocks:
        in_degree[block.name] = len(graph.get(block.name, set()))

    # Build reverse graph (who depends on me)
    reverse_graph: dict[str, set[str]] = {b.name: set() for b in blocks}
    for block_name, deps in graph.items():
        for dep in deps:
            if dep in reverse_graph:
                reverse_graph[dep].add(block_name)

    def get_priority_key(block: CodeBlock) -> tuple:
        """
        Return sort key for a block.
        Lower values = higher priority.
        """
        # Public comes before internal
        is_public_val = 0 if block.is_public else 1
        # Within same visibility, sort alphabetically
        return (is_public_val, block.name.lower())

    # Kahn's algorithm with priority queue
    available = [b for b in blocks if in_degree[b.name] == 0]

    while available:
        # Sort available by priority
        available.sort(key=get_priority_key)

        # Take the highest priority block
        block = available.pop(0)
        result.append(block)
        visited.add(block.name)

        # Update in-degrees for blocks that depend on this one
        for dependent in reverse_graph.get(block.name, set()):
            if dependent not in visited:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    dep_block = block_map.get(dependent)
                    if dep_block:
                        available.append(dep_block)

    # Check for cycles
    if len(result) != len(blocks):
        # There are cycles, add remaining blocks in original order
        for block in blocks:
            if block.name not in visited:
                result.append(block)

    return result


def generate_docstring(name: str, node: ast.AST, is_class: bool = False) -> str:
    """Generate a Sphinx-compatible docstring for a function or class."""
    if is_class:
        return f'"""\n    {name} class.\n    """'

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        params = []
        for arg in node.args.args:
            if arg.arg != "self" and arg.arg != "cls":
                params.append(arg.arg)
        for arg in node.args.kwonlyargs:
            params.append(arg.arg)
        if node.args.vararg:
            params.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            params.append(f"**{node.args.kwarg.arg}")

        if params:
            args_doc = "\n    ".join([f"{p}: Description." for p in params])
            return f'''"""\n    {name.replace("_", " ").title()}.\n    \n    Args:\n    {args_doc}\n    \n    Returns:\n        Description.\n    """'''
        else:
            return f'"""\n    {name.replace("_", " ").title()}.\n    """'

    return f'"""\n    {name.replace("_", " ").title()}.\n    """'


def add_docstring_to_block(block: CodeBlock) -> str:
    """Add a docstring to a block if it doesn't have one."""
    if block.docstring or block.is_import:
        return block.source

    # Skip adding docstrings to assignments (constants, __all__, etc.)
    if block.name.startswith("__") and block.name.endswith("__"):
        return block.source
    # Skip assignments (constants) - check by node type
    if isinstance(block.node, (ast.Assign, ast.AnnAssign)):
        return block.source
    # Skip type aliases
    if isinstance(block.node, ast.TypeAlias):
        return block.source

    new_docstring = generate_docstring(block.name, block.node, block.is_class)

    lines = block.source.split("\n")
    if lines:
        # Find the line where the function/class body starts
        # This is after the colon that ends the signature
        def_line_idx = 0
        for i, line in enumerate(lines):
            if line.strip().startswith(("def ", "class ", "async def ")):
                def_line_idx = i
                break

        # Find where the signature ends (line ending with colon)
        insert_idx = def_line_idx
        paren_depth = 0
        found_colon = False
        while insert_idx < len(lines):
            stripped = lines[insert_idx].strip()
            # Track parentheses depth for multi-line signatures
            for char in lines[insert_idx]:
                if char == '(':
                    paren_depth += 1
                elif char == ')':
                    paren_depth -= 1
            # Check if this line ends the signature
            if stripped.endswith(':') and paren_depth == 0:
                found_colon = True
                insert_idx += 1
                break
            insert_idx += 1

        # Skip blank lines after the signature
        while insert_idx < len(lines) and not lines[insert_idx].strip():
            insert_idx += 1

        if insert_idx < len(lines) and lines[insert_idx].strip().startswith('"""'):
            return block.source

        indent = "    "
        lines.insert(insert_idx, f"{indent}{new_docstring}")
        return "\n".join(lines)

    return block.source


def reorganize_blocks(blocks: list[CodeBlock]) -> list[CodeBlock]:
    """Reorganize blocks respecting dependencies, with public first where possible."""
    # Group blocks by type
    imports = [b for b in blocks if b.is_import]
    module_docstrings = [b for b in blocks if b.name == "__expr__" and not b.is_import]
    # Get non-import, non-expr blocks (assignments, classes, functions)
    code_blocks = [b for b in blocks if not b.is_import and b.name != "__expr__"]

    # Build dependency graph and sort
    if code_blocks:
        graph = build_dependency_graph(code_blocks)
        sorted_code_blocks = topological_sort_with_priority(code_blocks, graph)
    else:
        sorted_code_blocks = []

    # Build new order
    new_order: list[CodeBlock] = []

    # 1. Imports
    if imports:
        import_source = "\n".join(b.source for b in imports)
        new_order.append(
            CodeBlock(
                name="__imports__",
                node=imports[0].node,
                source=import_source,
                is_public=True,
                is_class=False,
                is_import=True,
            )
        )

    # 2. Module docstring (if any)
    new_order.extend(module_docstrings)

    # 3. Find where to insert the separator (first internal block in sorted order)
    first_internal_idx = None
    for i, block in enumerate(sorted_code_blocks):
        if not block.is_public:
            first_internal_idx = i
            break

    # 4. Add blocks before the separator (public section)
    if first_internal_idx is not None:
        before_separator = sorted_code_blocks[:first_internal_idx]
    else:
        before_separator = sorted_code_blocks

    for block in before_separator:
        block.source = add_docstring_to_block(block)
    new_order.extend(before_separator)

    # 5. Add separator and remaining blocks (internal section)
    if first_internal_idx is not None:
        separator = CodeBlock(
            name="__separator__",
            node=ast.Expr(value=ast.Constant(value="")),
            source='\n\n# ==============================================================================\n# INTERNAL API\n# ==============================================================================\n\n# The following functions and classes are for internal use only and may change\n# without notice. They are organized alphabetically for easier navigation.\n',
            is_public=False,
            is_class=False,
            is_import=False,
        )
        new_order.append(separator)

        after_separator = sorted_code_blocks[first_internal_idx:]
        for block in after_separator:
            block.source = add_docstring_to_block(block)
        new_order.extend(after_separator)

    return new_order


def generate_internal_index(blocks: list[CodeBlock]) -> str:
    """Generate an index comment for internal functions."""
    internal_blocks = [b for b in blocks if not b.is_public and not b.is_import]
    if not internal_blocks:
        return ""

    index_lines = ["# Internal Function Index:", "#"]
    for block in internal_blocks:
        kind = "class" if block.is_class else "func"
        index_lines.append(f"#   [{kind}] {block.name}")

    return "\n".join(index_lines) + "\n"


def refactor_file(filepath: Path, dry_run: bool = True) -> bool:
    """Refactor a single Python file."""
    print(f"Processing: {filepath}")

    blocks = parse_file(filepath)
    if not blocks:
        return False

    reorganized = reorganize_blocks(blocks)

    output_parts = []

    for i, block in enumerate(reorganized):
        if block.name == "__separator__":
            internal_index = generate_internal_index(blocks)
            if internal_index:
                output_parts.append(internal_index)
            output_parts.append(block.source)
        else:
            output_parts.append(block.source)

    output = "\n\n".join(output_parts)

    if not output.endswith("\n"):
        output += "\n"

    if dry_run:
        print(f"  Would refactor (dry run)")
        return True
    else:
        filepath.write_text(output, encoding="utf-8")
        print(f"  Refactored")
        return True


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Refactor Kimi Code CLI source files")
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=Path("src/kimi_cli"),
        help="Source directory to process",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without making changes",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        help="Specific files to process (default: all .py files)",
    )

    args = parser.parse_args()

    src_dir = args.src_dir

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = list(src_dir.rglob("*.py"))

    print(f"Found {len(files)} Python files to process")
    print(f"Mode: {'dry run' if args.dry_run else 'live'}")
    print()

    success_count = 0
    for filepath in files:
        if refactor_file(filepath, dry_run=args.dry_run):
            success_count += 1

    print()
    print(f"Processed {success_count}/{len(files)} files successfully")

    return 0


if __name__ == "__main__":
    sys.exit(main())
