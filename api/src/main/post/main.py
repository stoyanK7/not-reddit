from src.main.post.lifespan import lifespan
from src.main.post.router import router
from src.main.post.service import PostService
from src.main.shared.cors.cors import middleware

app = PostService(lifespan=lifespan, middleware=middleware)
app.include_router(router)
