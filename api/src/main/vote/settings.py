from pydantic.env_settings import BaseSettings


class VoteServiceSettings(BaseSettings):
    SERVICE_PREFIX: str = "/api/vote"


settings = VoteServiceSettings()
