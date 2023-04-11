from fastapi import APIRouter, Request, Response
from fastapi_gateway import route

from src.main.gateway.settings import settings

router = APIRouter()


@route(
    request_method=router.get,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post',
    service_path='/',
    body_params=['body'],
)
def get_10_posts(body: dict, request: Request, response: Response):
    pass


@route(
    request_method=router.get,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post/{post_id}',
    service_path='/{post_id}',
    body_params=['body'],
)
async def get_post(body: dict, post_id: int, request: Request, response: Response):
    pass


@route(
    request_method=router.post,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post',
    service_path='/',
    body_params=['body'],
)
async def create_post(body: dict, request: Request, response: Response):
    pass


@route(
    request_method=router.delete,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post/{post_id}',
    service_path='/{post_id}',
    body_params=['body'],
)
async def delete_post(body: dict, post_id: int, request: Request, response: Response):
    pass