# Legion LLM Gateway

Legion LLM Gateway is a high-throughput semantic caching, routing, and observability gateway for local LLM inference.

Creator and author: Jose Perez  
GitHub: dotdigitize  
License: Apache License 2.0, Copyright 2026 Jose Perez

## Overview

The gateway intercepts LLM API requests, computes deterministic local embeddings when external inference is disabled, checks a vector-similarity semantic cache, routes prompts to target models, and exposes operational telemetry through a FastAPI backend and React dashboard.

## Capabilities

- FastAPI reverse-proxy foundation for Ollama-compatible local inference.
- Semantic cache with cosine similarity matching.
- Deterministic fallback responses and embeddings when Ollama is disabled.
- Prompt routing rules for code and general requests.
- MariaDB-ready schema with sample fixtures and seed data.
- React, TypeScript, Vite, and Tailwind CSS dashboard.
- Tests that pass without Ollama, MariaDB, or external services.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest
uvicorn app.main:app --reload
```

In a second shell:

```bash
npm install
npm run dev
```

The API defaults to deterministic local behavior. Set `ENABLE_OLLAMA=true` to call Ollama at `OLLAMA_BASE_URL`.

## API

- `POST /v1/chat` routes a prompt, checks semantic cache, and returns a response.
- `GET /metrics` returns total requests, cache hit rate, average latency, and active routing rules.
- `GET /routing-rules` returns active sample routing configuration.
- `GET /health` reports service health and database mode.

## Project Status

This repository is structured as a serious open-source engineering project with production-oriented boundaries, testable local behavior, and MariaDB-ready persistence assets.
