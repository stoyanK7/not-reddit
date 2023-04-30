from jwt import decode

from fastapi import Request


def get_jwt_token(request: Request):
    jwt_token = extract_token_from_authorization_header(request.headers['Authorization'])
    return decode(jwt_token, options={"verify_signature": False})


def extract_token_from_authorization_header(authorization_header: str):
    """Extracts the token from the authorization header by removing the 'Bearer ' part."""
    return authorization_header[7:]


def get_access_token_oid(request: Request) -> str:
    return get_access_token_claim(request, 'oid')


def get_access_token_preferred_username(request: Request) -> str:
    return get_access_token_claim(request, 'preferred_username')


def get_access_token_claim(request: Request, claim: str) -> str:
    token = get_jwt_token(request)
    return token.get(claim)
