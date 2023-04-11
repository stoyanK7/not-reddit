from fastapi import APIRouter, Request, Response
from fastapi_gateway import route

from src.main.gateway.settings import settings

router = APIRouter()


@route(
    request_method=router.get,
    service_url=settings.COMMENT_SERVICE_URL,
    gateway_path='/comment',
    service_path='/',
    body_params=['body'],
    query_params=['page'],
)
async def get_10_comments(body: dict, page: int, request: Request, response: Response):
    pass


@route(
    request_method=router.post,
    service_url=settings.COMMENT_SERVICE_URL,
    gateway_path='/comment',
    service_path='/',
    body_params=['body'],
)
async def create_comment(body: dict, request: Request, response: Response):
    pass


@route(
    request_method=router.delete,
    service_url=settings.COMMENT_SERVICE_URL,
    gateway_path='/comment/{comment_id}',
    service_path='/{comment_id}',
    body_params=['body'],
)
async def delete_comment(body: dict, comment_id: int, request: Request, response: Response):
    pass
