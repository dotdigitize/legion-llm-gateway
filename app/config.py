from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Legion LLM Gateway"
    enable_database: bool = False
    enable_ollama: bool = False
    ollama_base_url: str = "http://localhost:11434"
    default_general_model: str = "llama3.1"
    default_code_model: str = "codellama"
    semantic_cache_threshold: float = 0.92
    database_url: str = "sqlite:///./legion_gateway.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
