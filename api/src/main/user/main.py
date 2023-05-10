from src.main.user.router import router
from src.main.user.lifespan import lifespan
from src.main.user.service import UserService
from src.main.shared.cors.cors import middleware

app = UserService(lifespan=lifespan, middleware=middleware)
app.include_router(router)
