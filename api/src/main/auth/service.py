from fastapi import FastAPI

from src.main.auth.util import configure_cors


class AuthService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        configure_cors(self)
