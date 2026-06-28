from __future__ import annotations

from dataclasses import dataclass, field
from threading import Lock

from app.services.embeddings import cosine_similarity, deterministic_embedding


@dataclass
class CacheEntry:
    prompt: str
    response: str
    model: str
    embedding: list[float]


@dataclass
class SemanticCache:
    threshold: float = 0.92
    entries: list[CacheEntry] = field(default_factory=list)
    _lock: Lock = field(default_factory=Lock)

    def lookup(self, prompt: str, model: str) -> CacheEntry | None:
        embedding = deterministic_embedding(prompt)
        with self._lock:
            candidates = [
                (cosine_similarity(embedding, entry.embedding), entry)
                for entry in self.entries
                if entry.model == model
            ]
        if not candidates:
            return None
        score, entry = max(candidates, key=lambda item: item[0])
        return entry if score >= self.threshold else None

    def store(self, prompt: str, response: str, model: str) -> CacheEntry:
        entry = CacheEntry(
            prompt=prompt,
            response=response,
            model=model,
            embedding=deterministic_embedding(prompt),
        )
        with self._lock:
            self.entries.append(entry)
        return entry
