import stripe

from fastapi import APIRouter, Request
from stripe.error import SignatureVerificationError
from starlette.responses import RedirectResponse

from src.main.award.settings import settings

router = APIRouter(prefix=settings.SERVICE_PREFIX)

stripe.api_key = settings.STRIPE_API_KEY


@router.post("/stripe_webhooks")
async def webhook(request: Request):
    event = None
    payload = await request.body()

    if settings.STRIPE_ENDPOINT_SECRET:
        sig_header = request.headers['stripe-signature']
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return {"success": False}

    event_type = event['type']
    if event_type == 'checkout.session.completed':
        print('checkout session completed')
    elif event_type == 'invoice.paid':
        print('invoice paid')
    elif event_type == 'invoice.payment_failed':
        print('invoice payment failed')
    else:
        print(f'unhandled event: {event_type}')

    # Handle the event
    print('Handled event type {}'.format(event['type']))

    return {"success": True}


@router.post("/session")
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NBcsqHMj8LggMg2UidsD64r',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.UI_URL + '/award?success=true',
            cancel_url=settings.UI_URL + '/award?canceled=true',
        )
        return RedirectResponse(url=checkout_session.url, status_code=303)
    except Exception as e:
        return str(e)
