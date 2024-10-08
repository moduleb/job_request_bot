import logging

from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    TOKEN: str
    ADMIN_ID: int
    LOG_LEVEL: str = "ERROR"

settings = Settings()

# Устанавливаем уровень логирования
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
