"""
Gerenciamento do banco de dados do Personal Assistant.
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Caminho até a pasta storage/database
BASE_DIR = Path(__file__).resolve().parents[3]
DATABASE_DIR = BASE_DIR / "storage" / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "assistant.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass