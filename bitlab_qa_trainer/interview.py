"""Interview question generation and scoring support."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict


def generate_interview() -> Dict[str, str]:
    return {
        "system": "How would you triage a sudden packet drop increase after a firmware release?",
        "coding": "Implement a function that returns the index of the highest set bit in an integer.",
        "debugging": "Given failing bit-flip logic using AND, explain and patch the bug.",
    }


def initialize_interview_state() -> Dict[str, object]:
    return {
        "started_at": datetime.now(timezone.utc),
        "answers": {},
        "score": 0,
    }


def score_interview_answer(answer: str, keywords: list[str]) -> int:
    normalized = answer.lower()
    matched = sum(1 for keyword in keywords if keyword.lower() in normalized)
    return int((matched / len(keywords)) * 100) if keywords else 0
