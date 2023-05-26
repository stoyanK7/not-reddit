import json
from fastapi import Request

from src.main.award.model import Award as AwardModel

from src.main.award.settings import settings


def determine_stripe_product(award_type: str):
    match award_type:
        case "silver":
            return settings.STRIPE_SILVER_AWARD_PRICE
        case "gold":
            return settings.STRIPE_GOLD_AWARD_PRICE
        case "platinum":
            return settings.STRIPE_PLATINUM_AWARD_PRICE


async def emit_award_given_event(request: Request, award: AwardModel):
    body = json.dumps({
        "award_type": award.award_type,
        "subject_id": award.subject_id,
    })
    if award.subject_type == "post":
        await request.app.post_awarded_amqp_publisher.send_message(str(body))
    elif award.subject_type == "comment":
        await request.app.comment_awarded_amqp_publisher.send_message(str(body))
