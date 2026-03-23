"""Coding challenge execution engine with basic safety guards."""

from __future__ import annotations

import ast
import contextlib
import io
from typing import Any, Dict

DISALLOWED_NODES = (ast.Import, ast.ImportFrom, ast.With, ast.AsyncWith, ast.Try, ast.Raise)
DISALLOWED_CALLS = {"open", "exec", "eval", "compile", "__import__", "input"}
ALLOWED_BUILTINS = {
    "print": print,
    "len": len,
    "range": range,
    "sum": sum,
    "min": min,
    "max": max,
    "sorted": sorted,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
    "set": set,
    "tuple": tuple,
    "enumerate": enumerate,
}


def _validate_ast(tree: ast.AST) -> None:
    for node in ast.walk(tree):
        if isinstance(node, DISALLOWED_NODES):
            raise ValueError(f"Disallowed syntax: {node.__class__.__name__}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in DISALLOWED_CALLS:
                raise ValueError(f"Disallowed function call: {node.func.id}")


def run_challenge(user_code: str, expected_output: str) -> Dict[str, Any]:
    """Run user code with restricted builtins and compare stdout against expectation."""
    if not isinstance(user_code, str) or not user_code.strip():
        return {"passed": False, "output": "", "error": "user_code must be a non-empty string"}

    try:
        tree = ast.parse(user_code, mode="exec")
        _validate_ast(tree)
        compiled = compile(tree, "<challenge>", "exec")
    except Exception as exc:
        return {"passed": False, "output": "", "error": str(exc)}

    safe_globals = {"__builtins__": ALLOWED_BUILTINS}
    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout):
            exec(compiled, safe_globals, {})
    except Exception as exc:
        return {"passed": False, "output": stdout.getvalue().strip(), "error": str(exc)}

    output = stdout.getvalue().strip()
    return {"passed": output == expected_output.strip(), "output": output, "error": ""}
