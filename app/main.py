from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import gateway, ops
from app.services.cache import SemanticCache
from app.services.telemetry import TelemetryStore


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.1.0")
    app.state.semantic_cache = SemanticCache(threshold=settings.semantic_cache_threshold)
    app.state.telemetry = TelemetryStore()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(gateway.router)
    app.include_router(ops.router)
    return app


app = create_app()
