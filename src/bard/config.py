from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    llm_provider: str = "openai"
    llm_api_key: str = ""
    llm_model: str = "gpt-4o"

    image_api_key: str = ""
    tts_api_key: str = ""

    data_dir: Path = Path("data")
    summary_interval: int = 5
    last_n_turns: int = 8


settings = Settings()
