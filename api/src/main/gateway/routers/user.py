from fastapi import APIRouter, Request, Response, Depends
from fastapi_gateway import route

from src.main.gateway.settings import settings
from src.main.gateway.config import azure_scheme
from pydantic import BaseModel

router = APIRouter()


@route(
    request_method=router.post,
    service_url=settings.USER_SERVICE_URL,
    gateway_path='/user',
    service_path='/',
    body_params=['body'],
    dependencies=[Depends(azure_scheme)]
)
async def create_user(body: dict, request: Request, response: Response):
    pass

class UserCheckIfRegistered(BaseModel):
    email: str


@route(
    request_method=router.post,
    service_url=settings.USER_SERVICE_URL,
    gateway_path='/user/registered',
    service_path='/registered',
    body_params=['body'],
)
async def check_if_registered(body: dict, request: Request, response: Response):
    pass
