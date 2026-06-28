from __future__ import annotations

import hashlib
import math


VECTOR_SIZE = 32


def deterministic_embedding(text: str) -> list[float]:
    normalized = text.strip().lower().encode("utf-8")
    digest = hashlib.sha256(normalized).digest()
    values = [((digest[i % len(digest)] / 255.0) * 2.0) - 1.0 for i in range(VECTOR_SIZE)]
    magnitude = math.sqrt(sum(value * value for value in values)) or 1.0
    return [value / magnitude for value in values]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("Vectors must have equal length")
    return sum(a * b for a, b in zip(left, right))
