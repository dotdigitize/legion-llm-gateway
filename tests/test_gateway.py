from fastapi.testclient import TestClient

from app.main import create_app
from app.services.router import route_prompt


def test_code_prompt_routes_to_code_model() -> None:
    decision = route_prompt("Write a Python function for retries")
    assert decision.route == "code-prompts"
    assert decision.model == "codellama"


def test_general_prompt_routes_to_general_model() -> None:
    decision = route_prompt("Summarize the benefits of semantic caching")
    assert decision.route == "general-prompts"
    assert decision.model == "llama3.1"


def test_chat_endpoint_uses_cache_without_external_services() -> None:
    client = TestClient(create_app())
    payload = {"prompt": "Summarize gateway telemetry"}

    first = client.post("/v1/chat", json=payload)
    second = client.post("/v1/chat", json=payload)

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["cache_hit"] is False
    assert second.json()["cache_hit"] is True
    assert first.json()["response"] == second.json()["response"]


def test_ops_endpoints_return_sample_read_only_data() -> None:
    client = TestClient(create_app())
    rules = client.get("/routing-rules")
    metrics = client.get("/metrics")
    health = client.get("/health")

    assert rules.status_code == 200
    assert metrics.status_code == 200
    assert health.json()["database_enabled"] is False
    assert len(rules.json()) >= 2
