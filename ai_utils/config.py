from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    log_level: str = "INFO"
    max_input_tokens: int = 4000
    model_name: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()