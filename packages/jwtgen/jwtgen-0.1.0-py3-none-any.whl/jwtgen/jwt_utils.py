import jwt

def create_jwt(secret: str, algorithm: str, payload: dict[str, str]) -> str:
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token
