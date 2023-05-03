from src.main.vote.lifespan import lifespan
from src.main.vote.router import router
from src.main.vote.service import VoteService

app = VoteService(lifespan=lifespan)
app.include_router(router)
