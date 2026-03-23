"""Debug & fix exercises for common Python mistakes."""

from __future__ import annotations

from typing import Dict


def debug_challenge(code: str) -> Dict[str, str]:
    """Analyze known bug patterns and provide guided fix details."""
    if "return num & (1 << n)" in code:
        fixed = code.replace("return num & (1 << n)", "return num ^ (1 << n)")
        return {
            "issue": "Bit flip uses AND, which only masks a bit instead of toggling it.",
            "fix": "Use XOR operator to toggle the target bit.",
            "corrected_code": fixed,
        }

    return {
        "issue": "No known bug pattern detected.",
        "fix": "Review operator intent and add tests to validate expected behavior.",
        "corrected_code": code,
    }
