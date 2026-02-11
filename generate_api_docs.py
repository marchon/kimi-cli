#!/usr/bin/env python3
"""
Generate Sphinx API documentation with cross-referenced function indexes.

This script:
1. Parses all Python files to extract function/class information
2. Builds a call graph (who calls whom)
3. Generates Sphinx .rst files with:
   - Alphabetical index of all public functions
   - Per-module function indexes
   - Cross-references showing callers and callees
"""

from __future__ import annotations

import ast
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class FunctionInfo:
    """Information about a function or method."""
    name: str
    module: str  # Full module path (e.g., "kimi_cli.app")
    file_path: Path
    line_number: int
    is_public: bool
    is_class: bool
    is_method: bool
    docstring: str | None
    parameters: list[dict[str, Any]]
    return_type: str | None
    calls: set[str] = field(default_factory=set)  # Functions this function calls
    called_by: set[str] = field(default_factory=set)  # Functions that call this one


@dataclass
class ModuleInfo:
    """Information about a module."""
    name: str  # Full module path
    file_path: Path
    functions: dict[str, FunctionInfo] = field(default_factory=dict)
    classes: dict[str, FunctionInfo] = field(default_factory=dict)
    imports: set[str] = field(default_factory=set)


def extract_type(annotation: ast.AST | None) -> str | None:
    """Extract type annotation as string."""
    if annotation is None:
        return None
    if isinstance(annotation, ast.Name):
        return annotation.id
    if isinstance(annotation, ast.Constant):
        return repr(annotation.value)
    if isinstance(annotation, ast.Subscript):
        value = extract_type(annotation.value)
        slice_val = extract_type(annotation.slice)
        if value and slice_val:
            return f"{value}[{slice_val}]"
    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        left = extract_type(annotation.left)
        right = extract_type(annotation.right)
        if left and right:
            return f"{left} | {right}"
    if isinstance(annotation, ast.Attribute):
        parts = []
        node = annotation
        while isinstance(node, ast.Attribute):
            parts.append(node.attr)
            node = node.value
        if isinstance(node, ast.Name):
            parts.append(node.id)
        return ".".join(reversed(parts))
    return None


def extract_parameters(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[dict[str, Any]]:
    """Extract parameter information from a function node."""
    params = []
    
    # Regular args
    for i, arg in enumerate(node.args.args):
        default_idx = len(node.args.defaults) - len(node.args.args) + i
        has_default = default_idx >= 0
        default = None
        if has_default:
            default_node = node.args.defaults[default_idx]
            if isinstance(default_node, ast.Constant):
                default = repr(default_node.value)
            # NameConstant was merged into Constant in Python 3.8+
            elif isinstance(default_node, ast.Name):
                default = default_node.id
        
        params.append({
            "name": arg.arg,
            "type": extract_type(arg.annotation),
            "default": default,
            "kind": "positional",
        })
    
    # *args
    if node.args.vararg:
        params.append({
            "name": f"*{node.args.vararg.arg}",
            "type": extract_type(node.args.vararg.annotation),
            "default": None,
            "kind": "var_positional",
        })
    
    # Keyword-only args
    for i, arg in enumerate(node.args.kwonlyargs):
        default = None
        if i < len(node.args.kw_defaults) and node.args.kw_defaults[i]:
            default_node = node.args.kw_defaults[i]
            if isinstance(default_node, ast.Constant):
                default = repr(default_node.value)
            elif isinstance(default_node, ast.Name):
                default = default_node.id
        
        params.append({
            "name": arg.arg,
            "type": extract_type(arg.annotation),
            "default": default,
            "kind": "keyword_only",
        })
    
    # **kwargs
    if node.args.kwarg:
        params.append({
            "name": f"**{node.args.kwarg.arg}",
            "type": extract_type(node.args.kwarg.annotation),
            "default": None,
            "kind": "var_keyword",
        })
    
    return params


def get_docstring(node: ast.FunctionDef | ast.ClassDef | ast.AsyncFunctionDef) -> str | None:
    """Extract docstring from a node."""
    if node.body and isinstance(node.body[0], ast.Expr):
        if isinstance(node.body[0].value, ast.Constant) and isinstance(
            node.body[0].value.value, str
        ):
            return node.body[0].value.value.strip()
    return None


class CallVisitor(ast.NodeVisitor):
    """Visitor to find all function calls within a function."""
    
    def __init__(self):
        self.calls: set[str] = set()
    
    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            self.calls.add(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            # For method calls like obj.method(), store as method name
            self.calls.add(node.func.attr)
        self.generic_visit(node)


def parse_module(file_path: Path, src_root: Path) -> ModuleInfo | None:
    """Parse a Python file and extract module information."""
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"Error parsing {file_path}: {e}")
        return None
    
    # Calculate module name from file path
    rel_path = file_path.relative_to(src_root)
    module_name = str(rel_path.with_suffix("")).replace("/", ".")
    
    module = ModuleInfo(name=module_name, file_path=file_path)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module.imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                module.imports.add(node.module)
    
    # Extract functions and classes at module level
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            is_public = not node.name.startswith("_")
            func_info = FunctionInfo(
                name=node.name,
                module=module_name,
                file_path=file_path,
                line_number=node.lineno,
                is_public=is_public,
                is_class=False,
                is_method=False,
                docstring=get_docstring(node),
                parameters=extract_parameters(node),
                return_type=extract_type(node.returns),
            )
            
            # Find calls within this function
            visitor = CallVisitor()
            visitor.visit(node)
            func_info.calls = visitor.calls
            
            module.functions[node.name] = func_info
        
        elif isinstance(node, ast.ClassDef):
            is_public = not node.name.startswith("_")
            class_info = FunctionInfo(
                name=node.name,
                module=module_name,
                file_path=file_path,
                line_number=node.lineno,
                is_public=is_public,
                is_class=True,
                is_method=False,
                docstring=get_docstring(node),
                parameters=[],
                return_type=None,
            )
            module.classes[node.name] = class_info
            
            # Extract methods
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    is_method_public = not item.name.startswith("_")
                    method_info = FunctionInfo(
                        name=f"{node.name}.{item.name}",
                        module=module_name,
                        file_path=file_path,
                        line_number=item.lineno,
                        is_public=is_method_public,
                        is_class=False,
                        is_method=True,
                        docstring=get_docstring(item),
                        parameters=extract_parameters(item),
                        return_type=extract_type(item.returns),
                    )
                    
                    visitor = CallVisitor()
                    visitor.visit(item)
                    method_info.calls = visitor.calls
                    
                    module.functions[method_info.name] = method_info
    
    return module


def build_call_graph(modules: dict[str, ModuleInfo]) -> None:
    """Build the called_by relationships for all functions."""
    # Create a map of function name -> FunctionInfo
    all_functions: dict[str, FunctionInfo] = {}
    for module in modules.values():
        for func in module.functions.values():
            # Store by full name: module.function
            full_name = f"{func.module}.{func.name}"
            all_functions[full_name] = func
            # Also store by just function name for local references
            all_functions[func.name] = func
    
    # For each function, resolve its calls to full names
    for module in modules.values():
        for func in module.functions.values():
            resolved_calls: set[str] = set()
            for call in func.calls:
                # Try to find the called function
                # 1. Look in same module
                if call in module.functions:
                    resolved_calls.add(f"{module.name}.{call}")
                # 2. Look in imports
                else:
                    for imp in module.imports:
                        full_call = f"{imp}.{call}"
                        if full_call in all_functions:
                            resolved_calls.add(full_call)
                # 3. Keep as-is if we can't resolve
                if not any(call in c for c in resolved_calls):
                    resolved_calls.add(call)
            
            func.calls = resolved_calls
    
    # Build called_by relationships
    for module in modules.values():
        for func in module.functions.values():
            full_name = f"{func.module}.{func.name}"
            for call in func.calls:
                if call in all_functions:
                    all_functions[call].called_by.add(full_name)


def escape_rst(text: str | None) -> str:
    """Escape special RST characters."""
    if text is None:
        return ""
    # Escape backslashes first, then other special chars
    text = text.replace("\\", "\\\\")
    text = text.replace("*", "\\*")
    text = text.replace("_", "\\_")
    text = text.replace("`", "\\`")
    return text


def generate_global_function_index(modules: dict[str, ModuleInfo], output_dir: Path) -> None:
    """Generate a global alphabetical index of all public functions."""
    output_file = output_dir / "api_function_index.rst"
    
    # Collect all public functions
    all_functions: list[FunctionInfo] = []
    for module in modules.values():
        for func in module.functions.values():
            if func.is_public:
                all_functions.append(func)
    
    # Sort alphabetically by name
    all_functions.sort(key=lambda f: f.name.lower())
    
    lines = [
        "API Function Index",
        "==================",
        "",
        "This page provides an alphabetical index of all public functions in the codebase.",
        "Each function entry shows:",
        "",
        "- **Module**: Where the function is defined",
        "- **Line**: Line number in the source file",
        "- **Parameters**: Function parameters with types and defaults",
        "- **Returns**: Return type",
        "- **Calls**: Functions this function calls",
        "- **Called by**: Functions that call this one",
        "",
        ".. contents::",
        "   :local:",
        "   :depth: 2",
        "",
    ]
    
    # Group by first letter for easier navigation
    current_letter = ""
    for func in all_functions:
        first_letter = func.name[0].upper()
        if first_letter != current_letter:
            current_letter = first_letter
            lines.append(f"")
            lines.append(f"{current_letter}")
            lines.append("-" * len(current_letter))
            lines.append("")
        
        # Function header with cross-reference
        lines.append(f".. _func-{func.name}:")
        lines.append("")
        lines.append(f"{func.name}")
        lines.append("^" * len(func.name))
        lines.append("")
        
        # Module info
        lines.append(f"**Module:** ``{func.module}``")
        lines.append("")
        lines.append(f"**File:** :file:`{func.file_path}` (line {func.line_number})")
        lines.append("")
        
        # Docstring
        if func.docstring:
            lines.append("**Description:**")
            lines.append("")
            lines.append(f"    {escape_rst(func.docstring[:200])}")
            if len(func.docstring) > 200:
                lines.append("    ...")
            lines.append("")
        
        # Parameters
        if func.parameters:
            lines.append("**Parameters:**")
            lines.append("")
            for param in func.parameters:
                param_str = f"    - ``{param['name']}``"
                if param["type"]:
                    param_str += f" (*{escape_rst(param['type'])}*)"
                if param["default"]:
                    param_str += f" = ``{param['default']}``"
                lines.append(param_str)
            lines.append("")
        
        # Return type
        if func.return_type:
            lines.append(f"**Returns:** ``{escape_rst(func.return_type)}``")
            lines.append("")
        
        # Calls
        if func.calls:
            lines.append("**Calls:**")
            lines.append("")
            for call in sorted(func.calls):
                # Try to link to the function if we know about it
                call_name = call.split(".")[-1]
                lines.append(f"    - :ref:`{call_name} <func-{call_name}>`")
            lines.append("")
        
        # Called by
        if func.called_by:
            lines.append("**Called by:**")
            lines.append("")
            for caller in sorted(func.called_by):
                caller_name = caller.split(".")[-1]
                caller_module = ".".join(caller.split(".")[:-1])
                lines.append(f"    - :ref:`{caller_name} <func-{caller_name}>` (from ``{caller_module}``)")
            lines.append("")
        
        lines.append("")
    
    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {output_file}")


def generate_module_indexes(modules: dict[str, ModuleInfo], output_dir: Path) -> None:
    """Generate per-module documentation with function indexes."""
    modules_dir = output_dir / "modules"
    modules_dir.mkdir(exist_ok=True)
    
    # Generate toctree index
    toctree_lines = [
        "Module Reference",
        "================",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ]
    
    for module_name in sorted(modules.keys()):
        safe_name = module_name.replace(".", "_")
        toctree_lines.append(f"   modules/{safe_name}")
    
    (output_dir / "modules.rst").write_text("\n".join(toctree_lines), encoding="utf-8")
    
    # Generate individual module files
    for module_name, module in sorted(modules.items()):
        safe_name = module_name.replace(".", "_")
        output_file = modules_dir / f"{safe_name}.rst"
        
        lines = [
            f"{module_name}",
            "=" * len(module_name),
            "",
            f".. module:: {module_name}",
            "",
            f"Source: :file:`{module.file_path}`",
            "",
        ]
        
        # Classes section
        if module.classes:
            public_classes = [c for c in module.classes.values() if c.is_public]
            if public_classes:
                lines.append("Classes")
                lines.append("-------")
                lines.append("")
                
                for cls in sorted(public_classes, key=lambda c: c.name):
                    lines.append(f".. _class-{cls.name}:")
                    lines.append("")
                    lines.append(f"{cls.name}")
                    lines.append("^" * len(cls.name))
                    lines.append("")
                    
                    if cls.docstring:
                        lines.append(escape_rst(cls.docstring[:300]))
                        if len(cls.docstring) > 300:
                            lines.append("...")
                        lines.append("")
                    
                    lines.append("")
        
        # Functions section
        if module.functions:
            # Separate module-level functions and methods
            module_funcs = [f for f in module.functions.values() 
                          if f.is_public and not f.is_method and not f.name.startswith("_")]
            methods = [f for f in module.functions.values() 
                      if f.is_public and f.is_method]
            
            if module_funcs:
                lines.append("Functions")
                lines.append("---------")
                lines.append("")
                
                for func in sorted(module_funcs, key=lambda f: f.name):
                    lines.append(f".. _{module_name}.{func.name}:")
                    lines.append("")
                    lines.append(f"{func.name}")
                    lines.append("^" * len(func.name))
                    lines.append("")
                    lines.append(f"**Line:** {func.line_number}")
                    lines.append("")
                    
                    if func.docstring:
                        lines.append("**Description:**")
                        lines.append("")
                        lines.append(f"    {escape_rst(func.docstring[:200])}")
                        lines.append("")
                    
                    if func.parameters:
                        lines.append("**Parameters:**")
                        lines.append("")
                        for param in func.parameters:
                            param_str = f"    - ``{param['name']}``"
                            if param["type"]:
                                param_str += f" (*{escape_rst(param['type'])}*)"
                            if param["default"]:
                                param_str += f" = ``{param['default']}``"
                            lines.append(param_str)
                        lines.append("")
                    
                    if func.return_type:
                        lines.append(f"**Returns:** ``{escape_rst(func.return_type)}``")
                        lines.append("")
                    
                    if func.calls:
                        lines.append("**Calls:**")
                        lines.append("")
                        for call in sorted(func.calls)[:10]:  # Limit to 10
                            call_name = call.split(".")[-1]
                            lines.append(f"    - :ref:`{call_name} <func-{call_name}>`")
                        if len(func.calls) > 10:
                            lines.append(f"    - ... and {len(func.calls) - 10} more")
                        lines.append("")
                    
                    if func.called_by:
                        lines.append("**Called by:**")
                        lines.append("")
                        for caller in sorted(func.called_by)[:10]:
                            caller_name = caller.split(".")[-1]
                            caller_mod = ".".join(caller.split(".")[:-1])
                            lines.append(f"    - ``{caller_mod}.{caller_name}``")
                        if len(func.called_by) > 10:
                            lines.append(f"    - ... and {len(func.called_by) - 10} more")
                        lines.append("")
                    
                    lines.append("")
            
            # Methods section
            if methods:
                lines.append("Methods")
                lines.append("-------")
                lines.append("")
                
                for method in sorted(methods, key=lambda m: m.name):
                    lines.append(f"- ``{method.name}`` - Line {method.line_number}")
                
                lines.append("")
        
        # Internal functions section
        internal_funcs = [f for f in module.functions.values() 
                         if not f.is_public and not f.is_method]
        if internal_funcs:
            lines.append("Internal Functions")
            lines.append("------------------")
            lines.append("")
            lines.append(".. note::")
            lines.append("   These functions are for internal use only and may change without notice.")
            lines.append("")
            
            for func in sorted(internal_funcs, key=lambda f: f.name):
                lines.append(f"- ``{func.name}`` - Line {func.line_number}")
            
            lines.append("")
        
        output_file.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"Generated module docs in: {modules_dir}")


def generate_main_index(output_dir: Path) -> None:
    """Generate the main index.rst file."""
    lines = [
        "Kimi Code CLI API Documentation",
        "================================",
        "",
        "This documentation provides a comprehensive reference for the Kimi Code CLI codebase.",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
        "   api_function_index",
        "   modules",
        "",
        "Quick Reference",
        "---------------",
        "",
        "- :doc:`api_function_index` - Alphabetical list of all public functions",
        "- :doc:`modules` - Documentation organized by module",
        "",
        "Navigation Tips",
        "---------------",
        "",
        "- Each function page shows what module it's in, what it calls, and what calls it",
        "- Use the function index to find functions alphabetically",
        "- Use the module pages to see all functions in a specific module",
        "",
    ]
    
    (output_dir / "index.rst").write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {output_dir / 'index.rst'}")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Sphinx API documentation")
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=Path("src/kimi_cli"),
        help="Source directory to scan",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("docs_api"),
        help="Output directory for generated documentation",
    )
    
    args = parser.parse_args()
    
    src_root = args.src_dir.parent  # Parent of kimi_cli
    output_dir = args.output_dir
    output_dir.mkdir(exist_ok=True)
    
    print(f"Scanning {args.src_dir}...")
    
    # Parse all Python files
    modules: dict[str, ModuleInfo] = {}
    py_files = list(args.src_dir.rglob("*.py"))
    
    for file_path in py_files:
        if file_path.name == "__init__.py" and not any(
            file_path.read_text(encoding="utf-8").strip()
        ):
            continue  # Skip empty __init__.py files
        
        module = parse_module(file_path, src_root)
        if module:
            modules[module.name] = module
    
    print(f"Parsed {len(modules)} modules")
    
    # Build call graph
    print("Building call graph...")
    build_call_graph(modules)
    
    # Generate documentation
    print("Generating documentation...")
    generate_global_function_index(modules, output_dir)
    generate_module_indexes(modules, output_dir)
    generate_main_index(output_dir)
    
    print(f"\nDocumentation generated in: {output_dir}")
    print("To build HTML: cd docs_api && make html")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
