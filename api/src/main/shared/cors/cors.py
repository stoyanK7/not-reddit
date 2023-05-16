from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from src.main.shared.cors.settings import settings

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
