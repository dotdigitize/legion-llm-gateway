from __future__ import annotations

import time

from fastapi import APIRouter, Request

from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm import generate_response
from app.services.router import route_prompt
from app.services.telemetry import RequestRecord

router = APIRouter(prefix="/v1", tags=["gateway"])


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest, request: Request) -> ChatResponse:
    started = time.perf_counter()
    decision = route_prompt(payload.prompt, payload.model)
    cache = request.app.state.semantic_cache
    telemetry = request.app.state.telemetry

    cached = cache.lookup(payload.prompt, decision.model)
    if cached:
        latency_ms = (time.perf_counter() - started) * 1000
        telemetry.add(RequestRecord(latency_ms, True, decision.model, decision.route))
        return ChatResponse(
            model=decision.model,
            response=cached.response,
            cache_hit=True,
            latency_ms=round(latency_ms, 2),
            route=decision.route,
        )

    response_text = await generate_response(payload.prompt, decision.model)
    cache.store(payload.prompt, response_text, decision.model)
    latency_ms = (time.perf_counter() - started) * 1000
    telemetry.add(RequestRecord(latency_ms, False, decision.model, decision.route))
    return ChatResponse(
        model=decision.model,
        response=response_text,
        cache_hit=False,
        latency_ms=round(latency_ms, 2),
        route=decision.route,
    )
