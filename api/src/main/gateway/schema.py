"""This module contains the Auth schemas."""

from pydantic import BaseModel


class Token(BaseModel):
    """
    Token model.

    By the spec, a JSON with the following fields is expected:
    - access_token
    - token_type
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
