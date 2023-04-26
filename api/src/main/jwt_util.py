from jwt import decode

from fastapi import Request


def get_jwt_token(request: Request):
    jwt_token = extract_token_from_authorization_header(request.headers['Authorization'])
    return decode(jwt_token, options={"verify_signature": False})


def extract_token_from_authorization_header(authorization_header: str):
    """Extracts the token from the authorization header by removing the 'Bearer ' part."""
    return authorization_header[7:]
