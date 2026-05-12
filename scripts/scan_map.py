#!/usr/bin/env python3
"""
AST-based project map generator for Fantareal.

Scans all .py files, extracts every function/class definition with exact line
numbers, docstrings, route decorators, and nesting relationships.  Outputs
Markdown ready for AI consumption — each function gets a precise [name](file#LNN)
anchor so tools can jump straight to the code.

Usage:
    python scripts/scan_map.py --source ../Fantareal --output maps/说明书_auto.md
    python scripts/scan_map.py --source ../Fantareal  # prints to stdout
"""

from __future__ import annotations

import ast
import argparse
import sys
from pathlib import Path
from dataclasses import dataclass, field

HTTP_METHODS = frozenset({"get", "post", "put", "delete", "patch", "head", "options", "websocket"})
ROUTE_FILE_PREFIXES = frozenset({"chat_api", "config_api", "mod_api", "page"})


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class Param:
    name: str
    type_hint: str = ""
    default: str = ""


@dataclass
class Func:
    name: str
    line: int
    is_async: bool = False
    params: list[Param] = field(default_factory=list)
    return_type: str = ""
    docstring: str = ""
    route: str = ""          # e.g. "POST /api/chat"
    nested_in: str = ""       # parent function or class name
    nested: list[Func] = field(default_factory=list)


@dataclass
class Field:
    name: str
    type_hint: str = ""
    default: str = ""


@dataclass
class Cls:
    name: str
    line: int
    docstring: str = ""
    bases: list[str] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    methods: list[Func] = field(default_factory=list)
    is_pydantic: bool = False


@dataclass
class File:
    rel_path: str
    functions: list[Func] = field(default_factory=list)
    classes: list[Cls] = field(default_factory=list)


# ---------------------------------------------------------------------------
# AST helpers
# ---------------------------------------------------------------------------


def _get_text(node: ast.AST | None) -> str:
    """Best-effort source text from an AST node."""
    if node is None:
        return ""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return ast.unparse(node) if hasattr(ast, "unparse") else ""


def _type_hint(node: ast.AST | None) -> str:
    if node is None:
        return ""
    if isinstance(node, ast.Constant) and node.value is None:
        return "None"
    return ast.unparse(node)


def _extract_docstring(body: list[ast.stmt]) -> str:
    """Return the first Expr/Constant docstring from a function or class body."""
    if not body:
        return ""
    first = body[0]
    if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
        if isinstance(first.value.value, str):
            return first.value.value.strip()
    return ""


def _extract_route(decorator_list: list[ast.expr]) -> str:
    """Try to extract HTTP method + path from decorators like @app.post('/foo')."""
    for dec in decorator_list:
        if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
            method = dec.func.attr
            if method in HTTP_METHODS and dec.args:
                path = _get_text(dec.args[0])
                return f"{method.upper()} {path}"
    return ""


def _params_from_function(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[Param]:
    """Extract parameter list, skipping 'self'."""
    result: list[Param] = []
    for arg in node.args.args:
        if arg.arg == "self":
            continue
        p = Param(name=arg.arg)
        if arg.annotation:
            p.type_hint = _type_hint(arg.annotation)
        result.append(p)
    # defaults (trailing params only)
    defaults = node.args.defaults
    if defaults:
        offset = len(result) - len(defaults)
        for i, d in enumerate(defaults):
            result[offset + i].default = _get_text(d)
    return result


# ---------------------------------------------------------------------------
# Core scanner
# ---------------------------------------------------------------------------


class Scanner:
    """Walk a directory tree and extract structured info from every .py file."""

    def __init__(self, source: Path):
        self.source = source.resolve()
        self.warnings: list[str] = []

    # -- per-file -----------------------------------------------------------

    def scan_file(self, filepath: Path) -> File:
        rel = str(filepath.resolve().relative_to(self.source)).replace("\\", "/")
        info = File(rel_path=rel)

        try:
            source_text = filepath.read_text(encoding="utf-8")
            tree = ast.parse(source_text, filename=str(filepath))
        except SyntaxError as e:
            self.warnings.append(f"SKIP {rel}: syntax error — {e}")
            return info

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                info.functions.append(self._scan_func(node, source_text))
            elif isinstance(node, ast.ClassDef):
                info.classes.append(self._scan_class(node))

        return info

    # -- class --------------------------------------------------------------

    def _scan_class(self, node: ast.ClassDef) -> Cls:
        bases = [ast.unparse(b) for b in node.bases] if hasattr(ast, "unparse") else []
        is_pydantic = _is_pydantic(node)
        c = Cls(
            name=node.name,
            line=node.lineno,
            docstring=_extract_docstring(node.body),
            bases=bases,
            is_pydantic=is_pydantic,
        )
        for child in node.body:
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                f = self._scan_func(child, "")
                f.nested_in = node.name
                c.methods.append(f)
            elif is_pydantic and isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name):
                # Pydantic model field: `name: type = default`
                fld = Field(name=child.target.id, type_hint=_type_hint(child.annotation))
                if child.value:
                    fld.default = _get_text(child.value)
                c.fields.append(fld)
        return c

    # -- function (recursive) -----------------------------------------------

    def _scan_func(
        self,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
        source_text: str,
    ) -> Func:
        f = Func(
            name=node.name,
            line=node.lineno,
            is_async=isinstance(node, ast.AsyncFunctionDef),
            params=_params_from_function(node),
            return_type=_type_hint(node.returns),
            docstring=_extract_docstring(node.body),
            route=_extract_route(node.decorator_list),
        )
        # Recurse into nested functions
        for child in node.body:
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                nested = self._scan_func(child, source_text)
                nested.nested_in = node.name
                f.nested.append(nested)
        return f


def _is_pydantic(node: ast.ClassDef) -> bool:
    """Check if class inherits from pydantic.BaseModel (by name)."""
    for base in node.bases:
        if isinstance(base, ast.Attribute) and base.attr == "BaseModel":
            return True
        if isinstance(base, ast.Name) and base.id == "BaseModel":
            return True
    return False


# ---------------------------------------------------------------------------
# Markdown generator
# ---------------------------------------------------------------------------


def _signature(f: Func) -> str:
    """Reconstruct a compact function signature for the heading."""
    parts = []
    for p in f.params:
        s = p.name
        if p.type_hint:
            s += f": {p.type_hint}"
        if p.default:
            s += f" = {p.default}"
        parts.append(s)
    sig = f"{f.name}({', '.join(parts)})"
    if f.return_type:
        sig += f" -> {f.return_type}"
    return sig


def _nesting_label(f: Func) -> str:
    if not f.nested_in:
        return ""
    return f"（嵌套在 {f.nested_in} 内）"


def _describe(f: Func) -> str:
    """Generate a one-line description for a function."""
    if f.docstring:
        # Use first sentence/line of docstring
        return f.docstring.split("\n")[0].rstrip("。. ")
    if f.route:
        method, path = f.route.split(" ", 1)
        return f"{f.route} 端点。"
    # Heuristic: split camelCase/snake_case into readable words
    name = f.name
    if name.startswith("_"):
        name = name.lstrip("_")
        prefix = "内部函数。"
    else:
        prefix = ""
    return prefix + "参见源码。"


def _related_functions(f: Func) -> str:
    """Auto-detect related functions: nested children + siblings hint."""
    related: list[str] = []
    if f.nested:
        related.extend(n.name for n in f.nested)
    if not related:
        return "[待补充]"
    return ", ".join(related)


def generate_markdown(files: list[File], title: str = "Fantareal 项目函数地图") -> str:
    """Generate a complete Markdown document from scanned file info."""
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("> 本文档由 `scripts/scan_map.py` 自动生成。")
    lines.append("> 行号由 AST 实时提取，始终与代码同步。")
    lines.append("> 标记为 `[待补充]` 的字段需要在对应函数的 docstring 中补充。")
    lines.append("")

    # Table of contents
    lines.append("## 目录")
    lines.append("")
    for i, f in enumerate(files, 1):
        func_count = sum(1 for _ in _iter_file_funcs(f))
        class_count = len(f.classes)
        parts: list[str] = []
        if func_count:
            parts.append(f"{func_count} 个函数")
        if class_count:
            parts.append(f"{class_count} 个类")
        if not parts:
            continue
        lines.append(f"- **第 {i} 节** [{f.rel_path}](#{_anchor(f.rel_path)})（{', '.join(parts)}）")
    lines.append("")

    # Per-file sections
    section = 0
    for f in files:
        all_funcs: list[tuple[Func, str]] = _flatten_file(f)
        has_classes = bool(f.classes)
        if not all_funcs and not has_classes:
            continue
        section += 1
        lines.append(f"## 第 {section} 节 {f.rel_path}")
        lines.append("")

        # -- Overview --
        lines.append("### 一览")
        lines.append("")

        if f.classes:
            for c in f.classes:
                tag = " (Pydantic BaseModel)" if c.is_pydantic else ""
                parts = [f"- **class {c.name}**{tag} — 第 {c.line} 行"]
                if c.fields:
                    field_strs = [f"`{fd.name}: {fd.type_hint or 'Any'}`" for fd in c.fields[:6]]
                    parts.append("  - 字段: " + ", ".join(field_strs))
                    if len(c.fields) > 6:
                        parts[-1] += f" ... 共 {len(c.fields)} 个字段"
                lines.extend(parts)
        if f.functions:
            if f.classes:
                lines.append("")
            for func in f.functions:
                lines.append(f"- `{func.name}()` — 第 {func.line} 行")
        lines.append("")

        # -- Function details --
        if all_funcs:
            lines.append("### 函数详情")
            lines.append("")
            for func, parent_path in all_funcs:
                header = f"#### [{_signature(func)}{_nesting_label(func)}]({f.rel_path}#L{func.line})（第 {func.line} 行）"
                lines.append(header)

                desc = _describe(func)
                if func.route:
                    lines.append(f"{func.route} 端点。{desc}" if not desc.startswith(func.route) else desc)
                else:
                    lines.append(desc)

                lines.append("- **常见坑**：[待补充]")
                lines.append("- **改动建议**：[待补充]")
                lines.append(f"- **相关函数**：{_related_functions(func)}")
                lines.append("")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


def _flatten_file(f: File) -> list[tuple[Func, str]]:
    """Return all functions in file-order with their nesting context."""
    result: list[tuple[Func, str]] = []

    def walk(funcs: list[Func], parents: list[str]) -> None:
        for func in funcs:
            result.append((func, " → ".join(parents) if parents else ""))
            if func.nested:
                walk(func.nested, parents + [func.name])

    walk(f.functions, [])

    for cls in f.classes:
        for m in cls.methods:
            result.append((m, cls.name))
            if m.nested:
                walk(m.nested, [cls.name, m.name])

    # sort by line number
    result.sort(key=lambda x: x[0].line)
    return result


def _iter_file_funcs(f: File):
    """Yield all functions in a file (module-level + class methods + nested)."""
    def walk(funcs):
        for func in funcs:
            yield func
            yield from walk(func.nested)
    yield from walk(f.functions)
    for cls in f.classes:
        yield from walk(cls.methods)


def _class_total(c: Cls) -> int:
    """Count functions in a class (including methods and nested)."""
    n = len(c.methods)
    for m in c.methods:
        n += _func_tree_size(m)
    return n


def _func_tree_size(f: Func) -> int:
    """Count nested functions recursively."""
    return len(f.nested) + sum(_func_tree_size(n) for n in f.nested)


def _anchor(rel_path: str) -> str:
    return rel_path.replace("/", "-").replace(".", "-").replace(" ", "-").lower()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AST-based project map generator for Fantareal"
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parent.parent.parent / "Fantareal",
        help="Path to the main Fantareal repo (default: ../Fantareal)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write output to file instead of stdout",
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="Glob patterns to exclude",
    )
    args = parser.parse_args()

    source: Path = args.source
    if not source.is_dir():
        print(f"ERROR: {source} is not a directory", file=sys.stderr)
        sys.exit(1)

    scanner = Scanner(source)

    # Collect .py files.
    # Approach: include everything, then apply exclusions.
    # Exclusions are based on naming *conventions*, not a hardcoded file list,
    # so the scanner adapts automatically as the project grows.
    py_files: list[Path] = []

    # Directories that are never project source code
    skip_dirs = {
        "__pycache__", ".venv", "venv", ".git", "node_modules",
        "data", "Android APK", ".obsidian", ".mypy_cache", ".pytest_cache",
        ".tox", "dist", "build", "egg-info", "htmlcov",
    }
    # Files that are clearly one-off / helper, not project source
    skip_prefixes = ("_custom_", "_gen_", "_merge_", "_generated_")
    # File names that are never project entry points (editor temp, etc.)
    skip_exact = {"__init__.py"}

    for py_file in sorted(source.rglob("*.py")):
        parts = set(py_file.relative_to(source).parts)
        if parts & skip_dirs:
            continue
        if py_file.name.startswith(skip_prefixes):
            continue
        # Include __init__.py only if it has actual content beyond a docstring
        if py_file.name in skip_exact:
            # __init__.py usually just re-exports — include it only if it defines functions/classes
            try:
                tree = ast.parse(py_file.read_text(encoding="utf-8"))
                has_defs = any(
                    isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
                    for n in ast.iter_child_nodes(tree)
                )
                if not has_defs:
                    continue
            except SyntaxError:
                continue

        py_files.append(py_file)

    if not py_files:
        print(f"ERROR: No .py files found in {source}", file=sys.stderr)
        sys.exit(1)

    # Scan
    files: list[File] = []
    for py_file in py_files:
        info = scanner.scan_file(py_file)
        # Only include files that have something worth documenting
        has_content = info.functions or info.classes
        if has_content:
            files.append(info)

    # Generate
    md = generate_markdown(files)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {len(files)} files → {args.output}")
    else:
        print(md)

    if scanner.warnings:
        print(f"\n{len(scanner.warnings)} warning(s):", file=sys.stderr)
        for w in scanner.warnings:
            print(f"  {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
