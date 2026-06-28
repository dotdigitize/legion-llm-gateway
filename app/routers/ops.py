from __future__ import annotations

from fastapi import APIRouter, Request

from app.database import database_enabled
from app.models.schemas import MetricSnapshot, RoutingRule
from app.services.router import sample_routing_rules

router = APIRouter(tags=["operations"])


@router.get("/health")
async def health() -> dict[str, str | bool]:
    return {"status": "ok", "database_enabled": database_enabled()}


@router.get("/metrics", response_model=MetricSnapshot)
async def metrics(request: Request) -> dict[str, float | int]:
    active_rules = len([rule for rule in sample_routing_rules() if rule.active])
    return request.app.state.telemetry.snapshot(active_rules)


@router.get("/routing-rules", response_model=list[RoutingRule])
async def routing_rules() -> list[RoutingRule]:
    return sample_routing_rules()


@router.get("/cache-entries")
async def cache_entries(request: Request) -> list[dict[str, str]]:
    return [
        {"prompt": entry.prompt, "model": entry.model, "response": entry.response}
        for entry in request.app.state.semantic_cache.entries
    ]
