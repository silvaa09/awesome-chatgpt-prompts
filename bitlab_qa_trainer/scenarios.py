"""System scenario simulator for QA/DPU style troubleshooting."""

from __future__ import annotations

import random
from typing import Dict, List

SCENARIOS: List[Dict[str, object]] = [
    {
        "name": "Packet Drop Under Load",
        "logs": {"cpu": "85%", "memory": "stable", "packet_drop": "12%"},
        "question": "What is root cause?",
        "answer": "Queue overflow or CPU bottleneck",
        "keywords": ["queue", "overflow", "cpu", "bottleneck"],
    },
    {
        "name": "Latency Spike During Backup",
        "logs": {"cpu": "62%", "memory": "78%", "disk_io": "95%"},
        "question": "What subsystem is likely impacted first?",
        "answer": "Disk I/O saturation impacts packet processing latency",
        "keywords": ["disk", "io", "saturation", "latency"],
    },
    {
        "name": "Intermittent Link Flaps",
        "logs": {"cpu": "38%", "memory": "40%", "link_errors": "rising"},
        "question": "What should QA validate next?",
        "answer": "Validate cable/transceiver health and firmware compatibility",
        "keywords": ["cable", "transceiver", "firmware", "compatibility"],
    },
]


def generate_scenario() -> Dict[str, object]:
    return random.choice(SCENARIOS)


def evaluate_answer(user_input: str, expected_keywords: list[str]) -> Dict[str, object]:
    normalized = user_input.lower().strip()
    matches = [k for k in expected_keywords if k.lower() in normalized]
    score = len(matches) / len(expected_keywords) if expected_keywords else 0.0
    return {
        "passed": score >= 0.5,
        "score": round(score, 2),
        "matched_keywords": matches,
        "missing_keywords": [k for k in expected_keywords if k not in matches],
    }
