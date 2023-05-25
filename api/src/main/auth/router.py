from fastapi import APIRouter, Depends
from starlette.status import HTTP_202_ACCEPTED

from src.main.auth.settings import settings
from src.main.auth.util import azure_scheme

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_202_ACCEPTED, dependencies=[Depends(azure_scheme)])
def authenticate():
    return None
