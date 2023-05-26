from typing import Annotated

import stripe

from fastapi import APIRouter, Request, Form, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from stripe.error import SignatureVerificationError
from starlette.responses import RedirectResponse

from src.main.shared.database.main import get_db
from src.main.award import crud
from src.main.award.util import determine_stripe_product, emit_award_given_event
from src.main.award.settings import settings

router = APIRouter(prefix=settings.SERVICE_PREFIX)

stripe.api_key = settings.STRIPE_API_KEY


@router.post("/webhooks")
async def webhook(request: Request, background_tasks: BackgroundTasks,
                  db: Session = Depends(get_db)):
    event = None
    payload = await request.body()

    if settings.STRIPE_ENDPOINT_SECRET:
        sig_header = request.headers['stripe-signature']
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
            )
        except SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return {"success": False}

    event_type = event['type']
    if event_type == "checkout.session.completed":
        metadata = event['data']['object']['metadata']
        payment_intent = event['data']['object']['payment_intent']
        crud.create_award(
            db=db, payment_intent=payment_intent, award_type=metadata['award_type'],
            subject_type=metadata['subject_type'], subject_id=metadata['subject_id']
        )
    elif event_type == "payment_intent.succeeded":
        payment_intent = event['data']['object']['id']
        award = crud.get_award_by_payment_intent(db=db, payment_intent=payment_intent)
        crud.set_award_to_paid(db=db, award=award)
        background_tasks.add_task(emit_award_given_event, request=request, award=award)

    return {"success": True}


@router.post("/session")
def create_checkout_session(subject_type: Annotated[str, Form()],
                            subject_id: Annotated[int, Form()],
                            award_type: Annotated[str, Form()]):
    try:
        url = f"{settings.UI_URL}/award?subject_id={subject_id}&subject_type={subject_type}"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': determine_stripe_product(award_type),
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f"{url}&success=true",
            cancel_url=f"{url}&canceled=true",
            metadata={
                'subject_type': subject_type,
                'subject_id': subject_id,
                'award_type': award_type
            }
        )
        return RedirectResponse(url=checkout_session.url, status_code=303)
    except Exception as e:
        return str(e)
