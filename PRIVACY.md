# Privacy

Legion LLM Gateway can process prompts, responses, routing decisions, cache entries, and request metadata.

## Default Local Mode

With `ENABLE_DATABASE=false` and `ENABLE_OLLAMA=false`, runtime data remains in process memory and deterministic responses are generated locally.

## Persistence

When database persistence is enabled, prompt text, response text, prompt hashes, model names, route names, cache hit state, and latency metrics may be stored. Operators are responsible for retention policies and access controls.

## Telemetry

The built-in telemetry is operational and limited to gateway metrics. Avoid sending sensitive prompt contents to external monitoring systems unless policies permit it.
