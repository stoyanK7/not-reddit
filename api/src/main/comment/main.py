from src.main.comment.lifespan import lifespan
from src.main.comment.router import router
from src.main.comment.service import CommentService
from src.main.shared.cors.cors import middleware

app = CommentService(lifespan=lifespan, middleware=middleware)
app.include_router(router)
