# Architecture

Legion LLM Gateway is organized around four runtime concerns:

1. Request interception through FastAPI.
2. Semantic cache lookup using deterministic embeddings and cosine similarity.
3. Model routing based on explicit model requests or prompt classification rules.
4. Telemetry reporting for request volume, latency, hit rate, and routing state.

## Backend

`app/main.py` creates the FastAPI application and initializes in-memory cache and telemetry stores. `app/routers/gateway.py` exposes the chat endpoint. `app/routers/ops.py` exposes health, metrics, routing rules, and cache inspection endpoints.

## Cache

`app/services/cache.py` stores prompt, response, model, and embedding data. The cache is model-scoped so responses generated for one model are not reused for another.

## Routing

`app/services/router.py` sends code-oriented prompts to the configured code model and general prompts to the configured general model. Explicit model selection takes precedence.

## LLM Integration

`app/services/llm.py` calls Ollama only when enabled. Otherwise, it returns deterministic hash-based responses to support repeatable tests and local operation.

## Persistence

The `db/` directory contains MariaDB-ready SQL for cache entries, routing rules, and request logs. Runtime tests do not depend on MariaDB.

## Dashboard

The React dashboard presents operational metrics and active routing rules in a clean infrastructure UI.
