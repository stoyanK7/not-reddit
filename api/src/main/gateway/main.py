from fastapi import Depends, FastAPI

from src.main.gateway.config import configure_cors, azure_scheme, load_openid_config_on_startup
from src.main.gateway.routers.user import router as user_router
from src.main.gateway.routers.comment import router as comment_router
from src.main.gateway.routers.post import router as post_router
from src.main.gateway.routers.subreddit import router as subreddit_router
from src.main.gateway.routers.vote import router as vote_router
from src.main.gateway.settings import settings

app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': settings.OPENAPI_CLIENT_ID,
    },
)

configure_cors(app)
load_openid_config_on_startup(app)


@app.get("/", dependencies=[Depends(azure_scheme)])
async def root():
    return {"message": "Hello World"}


app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(subreddit_router)
app.include_router(vote_router)
