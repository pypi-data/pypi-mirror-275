import argparse
import logging
import os
import json
from jwtgen.version import get_version
from jwtgen.jwt_utils import create_jwt, decode_jwt
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.getLogger("botocore").setLevel(logging.ERROR)

now = int(time.time())

def generate_template():
    template = {
        "scope": "profile email",
        "authorization_details": ["read", "write"],
        "client_id": "a123456",
        "iss": "https://sso.example.com",
        "jti": "aBcD1234EfGh5678IjKl",
        "aud": "https://sso.exampleapp.com",
        "sub": "exampleuser",
        "auth_time": 1716307067,
        "groups": [
          "USER",
          "ADMIN"
        ],
        "cn": "u123456",
        "iat": 1716307067,
        "exp": now + 3600
    }
    with open('jwtgen.json', 'w') as f:
        json.dump(template, f, indent=4)
    print("Template jwtgen.json file created. You can edit this file with your payload.")

def main():
    parser = argparse.ArgumentParser(
        description="JWTGen: A CLI utility for generating JWT tokens."
    )

    allowed_algorithms = ["HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512"]

    parser.add_argument("--version", action="version", version=f"%(prog)s {get_version()}")
    parser.add_argument("--secret", type=str, help="The secret key to sign the JWT (required for encoding)")
    parser.add_argument("--algorithm", type=str, default="HS256", help="The algorithm to use for signing the JWT", choices=allowed_algorithms)
    parser.add_argument("--generate-template", action="store_true", help="Generate a template jwtgen.json file")
    parser.add_argument("--decode", action="store_true", help="Decode the JWT token")

    args = parser.parse_args()

    if args.decode:
        if not args.secret:
            logging.error("Secret key is not provided.")
            return
        token = input("Enter the JWT token: ")
        payload = decode_jwt(args.secret.encode(), token)
        print("Decoded payload:")
        print(json.dumps(payload, indent=4))
        return

    if args.generate_template:
        generate_template()
        return

    if not os.path.exists("jwtgen.json"):
        logging.error("jwtgen.json file not found.")
        generate_template()
        return

    with open("jwtgen.json", "r") as f:
        try:
            payload = json.load(f)
        except json.JSONDecodeError:
            logging.error("jwtgen.json is not a valid JSON file.")
            return

    if not args.secret:
        logging.error("Secret key is not provided.")
        return

    token = create_jwt(args.secret, args.algorithm, payload)
    print(f"{args.algorithm} encoded token: {token}")

if __name__ == "__main__":
    main()
