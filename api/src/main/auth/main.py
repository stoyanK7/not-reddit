from fastapi import FastAPI, Depends
from starlette.status import HTTP_202_ACCEPTED

from src.main.auth.util import configure_cors, azure_scheme

app = FastAPI()
configure_cors(app)


@app.get("/auth", status_code=HTTP_202_ACCEPTED, dependencies=[Depends(azure_scheme)])
def authenticate():
    return None
