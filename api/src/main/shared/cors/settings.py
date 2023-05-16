from pydantic import BaseSettings


class CorsSettings(BaseSettings):
    CORS_ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "https://notredditui.switzerlandnorth.cloudapp.azure.com"
    ]


settings = CorsSettings()
