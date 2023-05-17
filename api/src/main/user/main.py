from src.main.user.router import router
from src.main.user.lifespan import lifespan
from src.main.user.service import UserService

app = UserService(lifespan=lifespan)
app.include_router(router)
