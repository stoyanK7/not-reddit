from fastapi import APIRouter, Request, Response, Security
from fastapi_gateway import route

from src.main.gateway.settings import settings
from src.main.gateway.config import azure_scheme

router = APIRouter()


@route(
    request_method=router.get,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post',
    service_path='/',
)
def get_10_posts(request: Request, response: Response):
    pass


@route(
    request_method=router.get,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post/{post_id}',
    service_path='/{post_id}',
)
async def get_post(post_id: int, request: Request, response: Response):
    pass


@route(
    request_method=router.post,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post',
    service_path='/',
    body_params=['body'],
    dependencies=[Security(azure_scheme)]
)
async def create_post(body: dict, request: Request, response: Response):
    pass


@route(
    request_method=router.delete,
    service_url=settings.POST_SERVICE_URL,
    gateway_path='/post/{post_id}',
    service_path='/{post_id}',
)
async def delete_post(post_id: int, request: Request, response: Response):
    pass
