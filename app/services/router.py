from __future__ import annotations

import re
from dataclasses import dataclass

from app.config import get_settings
from app.models.schemas import RoutingRule


CODE_TERMS = ("python", "typescript", "javascript", "sql", "function", "class", "bug", "stack trace", "api")


@dataclass(frozen=True)
class RouteDecision:
    model: str
    route: str


def sample_routing_rules() -> list[RoutingRule]:
    settings = get_settings()
    return [
        RoutingRule(
            name="code-prompts",
            match_type="keyword",
            pattern=", ".join(CODE_TERMS),
            model=settings.default_code_model,
            priority=100,
        ),
        RoutingRule(
            name="general-prompts",
            match_type="fallback",
            pattern="*",
            model=settings.default_general_model,
            priority=10,
        ),
    ]


def route_prompt(prompt: str, requested_model: str | None = None) -> RouteDecision:
    if requested_model:
        return RouteDecision(model=requested_model, route="explicit-model")

    settings = get_settings()
    lowered = prompt.lower()
    if any(re.search(rf"\b{re.escape(term)}\b", lowered) for term in CODE_TERMS):
        return RouteDecision(model=settings.default_code_model, route="code-prompts")
    return RouteDecision(model=settings.default_general_model, route="general-prompts")
