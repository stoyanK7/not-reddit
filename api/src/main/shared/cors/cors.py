from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.main.shared.cors.settings import settings
from src.main.shared.logger import logger


def configure_cors(app: FastAPI) -> None:
    if settings.ALLOWED_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_ORIGINS,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
        logger.info('CORS is configured.')
