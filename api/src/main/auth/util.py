from fastapi_azure_auth import MultiTenantAzureAuthorizationCodeBearer

from src.main.auth.settings import settings
from src.main.shared.logger import logger


azure_scheme = MultiTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.APP_CLIENT_ID,
    scopes={
        f'api://{settings.APP_CLIENT_ID}/user_impersonation': 'user_impersonation',
    },
    validate_iss=False
)


async def load_openid_config() -> None:
    await azure_scheme.openid_config.load_config()
    logger.info("OpenID config is loaded.")
