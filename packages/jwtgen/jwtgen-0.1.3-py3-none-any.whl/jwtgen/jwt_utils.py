import base64
import json
from typing import Any
import jwt

def create_jwt(secret: str, algorithm: str, payload: dict[str, Any]) -> str:
    token = jwt.encode(payload, key=secret, algorithm=algorithm)
    return token

def decode_jwt(token: str) -> dict[str, Any]:
    # Split the token into its three parts
    parts = token.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid JWT token")

    # Decode the payload and handle padding
    payload_base64 = parts[1]
    payload_base64 += '=' * (4 - len(payload_base64) % 4)  # Adjust padding
    payload_json = base64.urlsafe_b64decode(payload_base64).decode('utf-8')
    payload = json.loads(payload_json)

    return payload
