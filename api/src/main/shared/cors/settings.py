from pydantic import BaseSettings


class CorsSettings(BaseSettings):
    ALLOWED_ORIGINS: list[str] = [
        'http://localhost:8000',
        "http://localhost:8080",
        "http://localhost:3000",
        "https://notredditui.switzerlandnorth.cloudapp.azure.com",
        "https://notredditapi.switzerlandnorth.cloudapp.azure.com",
    ]


settings = CorsSettings()
