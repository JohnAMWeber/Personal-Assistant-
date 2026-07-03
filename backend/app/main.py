"""
Ponto de entrada do Personal Assistant.
"""

from app.core.config import settings
from app.core.logger import logger
from app.memory.database import DATABASE_FILE


def start():
    logger.info("=" * 40)
    logger.info(settings.APP_NAME)
    logger.info(f"Versão: {settings.VERSION}")
    logger.info("=" * 40)

    logger.info(f"Banco: {DATABASE_FILE}")

    logger.success("Sistema iniciado com sucesso.")


if __name__ == "__main__":
    start()