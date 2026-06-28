from app.services.cache import SemanticCache
from app.services.embeddings import cosine_similarity, deterministic_embedding


def test_deterministic_embedding_is_stable() -> None:
    first = deterministic_embedding("Explain cache routing")
    second = deterministic_embedding("Explain cache routing")
    assert first == second
    assert round(cosine_similarity(first, second), 6) == 1.0


def test_semantic_cache_returns_exact_prompt_match() -> None:
    cache = SemanticCache(threshold=0.99)
    cache.store("Explain FastAPI middleware", "cached response", "llama3.1")
    hit = cache.lookup("Explain FastAPI middleware", "llama3.1")
    assert hit is not None
    assert hit.response == "cached response"


def test_semantic_cache_is_model_scoped() -> None:
    cache = SemanticCache(threshold=0.99)
    cache.store("Explain FastAPI middleware", "cached response", "llama3.1")
    assert cache.lookup("Explain FastAPI middleware", "codellama") is None
