from fastapi.middleware.cors import CORSMiddleware

from src.main.shared.cors.settings import settings as cors_settings
from src.main.auth.lifespan import lifespan
from src.main.auth.router import router
from src.main.auth.service import AuthService

app = AuthService(lifespan=lifespan)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
