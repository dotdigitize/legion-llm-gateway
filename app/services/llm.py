from __future__ import annotations

import hashlib

import httpx

from app.config import get_settings


async def generate_response(prompt: str, model: str) -> str:
    settings = get_settings()
    if not settings.enable_ollama:
        return deterministic_response(prompt, model)

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(
                f"{settings.ollama_base_url.rstrip('/')}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
            )
            response.raise_for_status()
            data = response.json()
            return str(data.get("response", deterministic_response(prompt, model)))
    except httpx.HTTPError:
        return deterministic_response(prompt, model)


def deterministic_response(prompt: str, model: str) -> str:
    digest = hashlib.sha256(f"{model}:{prompt.strip()}".encode("utf-8")).hexdigest()[:16]
    return f"Legion deterministic response [{model}:{digest}]"
