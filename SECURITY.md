# Security

## Scope

Legion LLM Gateway is designed as an internal inference gateway. Deployments should place it behind trusted network controls, authentication, and TLS termination appropriate for the environment.

## Database Safety

- Database access must use parameterized SQL.
- The service does not expose raw SQL execution endpoints.
- When `ENABLE_DATABASE=false`, database-backed paths must fail gracefully and continue with read-only sample operational data or in-memory runtime state.

## Prompt and Response Data

Prompts and responses can contain sensitive information. Operators should configure retention, logging, and database access controls before using persistent storage.

## Upstream Inference

Ollama integration is optional. If enabled, validate `OLLAMA_BASE_URL` and restrict network egress to trusted upstream services.

## Reporting Issues

Please report security concerns privately to the project maintainer before public disclosure.
