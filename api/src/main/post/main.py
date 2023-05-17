from src.main.post.lifespan import lifespan
from src.main.post.router import router
from src.main.post.service import PostService

app = PostService(lifespan=lifespan)
app.include_router(router)
