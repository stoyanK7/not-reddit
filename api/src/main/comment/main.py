from src.main.comment.lifespan import lifespan
from src.main.comment.router import router
from src.main.comment.service import CommentService

app = CommentService(lifespan=lifespan)
app.include_router(router)
