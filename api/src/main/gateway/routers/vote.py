from fastapi import APIRouter, Request, Response
from fastapi_gateway import route

from src.main.gateway.settings import settings

router = APIRouter()


@route(
    request_method=router.post,
    service_url=settings.VOTE_SERVICE_URL,
    gateway_path='/vote',
    service_path='/',
    body_params=['body'],
)
async def cast_vote(body: dict, request: Request, response: Response):
    pass
