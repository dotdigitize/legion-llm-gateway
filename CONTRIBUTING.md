# Contributing

Contributions should preserve the gateway's local-first behavior and keep tests independent of Ollama, MariaDB, or external services.

## Development

```bash
python -m pytest
npm install
npm run build
```

## Guidelines

- Keep database access parameterized.
- Do not add raw SQL execution endpoints.
- Preserve deterministic fallback behavior.
- Add focused tests for cache, routing, telemetry, and API behavior.
- Keep frontend changes consistent with a clean professional infrastructure UI.

## License

By contributing, you agree that your contributions are licensed under the Apache License 2.0.
