from src.main.vote.lifespan import lifespan
from src.main.vote.router import router
from src.main.vote.service import VoteService
from src.main.shared.cors.cors import middleware

app = VoteService(lifespan=lifespan, middleware=middleware)
app.include_router(router)
