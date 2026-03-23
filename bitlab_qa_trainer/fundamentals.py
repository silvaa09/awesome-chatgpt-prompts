"""Python fundamentals scenarios and exercises."""

from typing import Dict


def get_fundamentals_content() -> Dict[str, Dict[str, str]]:
    return {
        "data_types": {
            "scenario": "A telemetry system receives packet_count as text from a CSV feed.",
            "example": "packet_count = int('128')",
            "exercise": "Convert '256' to an integer and add 44.",
            "solution": "result = int('256') + 44  # 300",
        },
        "operators": {
            "scenario": "You must compute utilization ratio from used/total buffers.",
            "example": "ratio = used / total",
            "exercise": "Given used=84 and total=120, compute ratio rounded to 2 decimals.",
            "solution": "ratio = round(84 / 120, 2)  # 0.7",
        },
        "data_structures": {
            "scenario": "Store per-port error counters and read one quickly.",
            "example": "errors = {'eth0': 3, 'eth1': 0}",
            "exercise": "Create a dict with keys rx and tx and values 14 and 9.",
            "solution": "counters = {'rx': 14, 'tx': 9}",
        },
        "control_flow": {
            "scenario": "Flag systems as overloaded only when CPU exceeds threshold.",
            "example": "status = 'overloaded' if cpu > 80 else 'healthy'",
            "exercise": "Set status to critical if drops > 10 else normal.",
            "solution": "status = 'critical' if drops > 10 else 'normal'",
        },
        "functions": {
            "scenario": "Normalize packet rates using a reusable helper.",
            "example": "def normalize(rate, max_rate): return rate / max_rate",
            "exercise": "Write a function add(a, b) that returns their sum.",
            "solution": "def add(a, b):\n    return a + b",
        },
        "io": {
            "scenario": "Read operator input for target packet rate.",
            "example": "target = int(input('Target rate: '))",
            "exercise": "Read name input and print a greeting.",
            "solution": "name = input('Name: ')\nprint(f'Hello {name}')",
        },
        "error_handling": {
            "scenario": "User may type invalid integers while setting queue depth.",
            "example": "try:\n    depth = int(text)\nexcept ValueError:\n    depth = 0",
            "exercise": "Safely divide 10 by user-supplied denominator.",
            "solution": "try:\n    result = 10 / int(value)\nexcept (ValueError, ZeroDivisionError):\n    result = None",
        },
    }
