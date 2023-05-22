from fastapi import APIRouter
from starlette.status import HTTP_202_ACCEPTED

from src.main.auth.settings import settings

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_202_ACCEPTED)
def authenticate():
    return True
