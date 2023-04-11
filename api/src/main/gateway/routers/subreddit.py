from fastapi import APIRouter, Request, Response
from fastapi_gateway import route

from src.main.gateway.settings import settings

router = APIRouter()


@route(
    request_method=router.post,
    service_url=settings.SUBREDDIT_SERVICE_URL,
    gateway_path='/subreddit',
    service_path='/',
    body_params=['body'],
)
async def create_subreddit(body: dict, request: Request, response: Response):
    pass
