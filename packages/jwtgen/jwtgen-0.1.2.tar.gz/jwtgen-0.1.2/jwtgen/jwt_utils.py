import jwt

def create_jwt(secret: str, algorithm: str, payload: dict[str, str]) -> str:
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

def decode_jwt(secret: str, token: str) -> dict[str, str]:
    payload = jwt.decode(token, secret, algorithms=["HS256"])
    return payload
