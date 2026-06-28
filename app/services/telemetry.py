from __future__ import annotations

from dataclasses import dataclass
from threading import Lock


@dataclass
class RequestRecord:
    latency_ms: float
    cache_hit: bool
    model: str
    route: str


class TelemetryStore:
    def __init__(self) -> None:
        self._records: list[RequestRecord] = []
        self._lock = Lock()

    def add(self, record: RequestRecord) -> None:
        with self._lock:
            self._records.append(record)

    def snapshot(self, active_routing_rules: int) -> dict[str, float | int]:
        with self._lock:
            records = list(self._records)
        total = len(records)
        hits = sum(1 for record in records if record.cache_hit)
        avg = sum(record.latency_ms for record in records) / total if total else 0.0
        return {
            "total_requests": total,
            "cache_hit_rate": round(hits / total, 4) if total else 0.0,
            "average_latency_ms": round(avg, 2),
            "active_routing_rules": active_routing_rules,
        }
