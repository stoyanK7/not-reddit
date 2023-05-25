import stripe

from fastapi import APIRouter, Request
from stripe.error import SignatureVerificationError
from starlette.responses import RedirectResponse

from src.main.award.settings import settings

router = APIRouter(prefix=settings.SERVICE_PREFIX)

stripe.api_key = settings.STRIPE_API_KEY


@router.post("/stripe_webhooks")
def webhook(request: Request, body: dict):
    event = None
    payload = body

    if settings.EDNPOINT_SECRET:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers['stripe-signature']
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.EDNPOINT_SECRET
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return {"success": False}

        # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
    elif event['type'] == 'payment_method.attached':
        payment_method = event['data']['object']  # contains a stripe.PaymentMethod
        # Then define and call a method to handle the successful attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

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
