from fastapi import FastAPI


class AuthService(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
