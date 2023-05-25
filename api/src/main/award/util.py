from src.main.award.settings import settings


def determine_stripe_product(award_type: str):
    match award_type:
        case "silver":
            return settings.STRIPE_SILVER_AWARD_PRICE
        case "gold":
            return settings.STRIPE_GOLD_AWARD_PRICE
        case "platinum":
            return settings.STRIPE_PLATINUM_AWARD_PRICE
