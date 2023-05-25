from src.main.shared.env import get_env


class AwardServiceSettings:
    SERVICE_PREFIX: str = "/api/award"
    STRIPE_API_KEY = get_env("STRIPE_API_KEY")
    STRIPE_SILVER_AWARD_PRICE = get_env("STRIPE_SILVER_AWARD_PRICE")
    STRIPE_GOLD_AWARD_PRICE = get_env("STRIPE_GOLD_AWARD_PRICE")
    STRIPE_PLATINUM_AWARD_PRICE = get_env("STRIPE_PLATINUM_AWARD_PRICE")
    UI_URL = get_env("UI_URL")


settings = AwardServiceSettings()
