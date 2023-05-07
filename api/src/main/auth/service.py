from fastapi import FastAPI

from src.main.shared.cors.cors import configure_cors


class AuthService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        configure_cors(self)
