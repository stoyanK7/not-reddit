from fastapi import FastAPI
from fastapi_azure_auth import MultiTenantAzureAuthorizationCodeBearer
from starlette.middleware.cors import CORSMiddleware

from src.main.auth_settings import settings
from src.main.logger import logger


def configure_cors(app: FastAPI) -> None:
    if settings.CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
        logger.info('CORS is configured.')


azure_scheme = MultiTenantAzureAuthorizationCodeBearer(
    # Endpoints should depend on this value. For example,
    # @app.get("/", dependencies=[Depends(azure_scheme)])
    app_client_id=settings.APP_CLIENT_ID,
    scopes={
        f'api://{settings.APP_CLIENT_ID}/user_impersonation': 'user_impersonation',
    },
    validate_iss=False
)


async def load_openid_config() -> None:
    await azure_scheme.openid_config.load_config()
    logger.info("OpenID config is loaded.")


def load_openid_config_on_startup(app: FastAPI) -> None:
    app.add_event_handler('startup', load_openid_config)
