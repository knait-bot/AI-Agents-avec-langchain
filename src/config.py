from pathlib import Path
from pydantic import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
NOTES_FILE = DATA_DIR / "notes.txt"


class Settings(BaseSettings):
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_model_simple: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    temperature: float = 0.2
    tavily_api_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

DATA_DIR.mkdir(parents=True, exist_ok=True)
if not NOTES_FILE.exists():
    NOTES_FILE.write_text("", encoding="utf-8")