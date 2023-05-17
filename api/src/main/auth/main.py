from src.main.auth.lifespan import lifespan
from src.main.auth.router import router
from src.main.auth.service import AuthService

app = AuthService(lifespan=lifespan)
app.include_router(router)
