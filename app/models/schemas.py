from __future__ import annotations

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    model: str | None = None
    temperature: float = 0.0


class ChatResponse(BaseModel):
    model: str
    response: str
    cache_hit: bool
    latency_ms: float
    route: str


class MetricSnapshot(BaseModel):
    total_requests: int
    cache_hit_rate: float
    average_latency_ms: float
    active_routing_rules: int


class RoutingRule(BaseModel):
    name: str
    match_type: str
    pattern: str
    model: str
    priority: int
    active: bool = True
