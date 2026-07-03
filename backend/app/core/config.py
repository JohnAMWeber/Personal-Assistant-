"""
Configurações globais do Personal Assistant.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    APP_NAME: str = "Personal Assistant"
    VERSION: str = "0.1.0-alpha.1"
    AUTHOR: str = "John"


settings = Settings()