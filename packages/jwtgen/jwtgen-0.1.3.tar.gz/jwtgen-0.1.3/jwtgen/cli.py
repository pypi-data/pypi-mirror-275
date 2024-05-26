import argparse
import logging
import os
import json
from jwtgen.version import get_version
from jwtgen.jwt_utils import create_jwt, decode_jwt
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to get detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.getLogger("botocore").setLevel(logging.ERROR)

now = datetime.now()

def generate_template():
    template = {
        "scope": "profile email",
        "authorization_details": ["read", "write"],
        "client_id": "a123456",
        "iss": "https://sso.example.com",
        "jti": "aBcD1234EfGh5678IjKl",
        "sub": "exampleuser",
        "auth_time": now.timestamp(),
        "groups": [
          "USER",
          "ADMIN"
        ],
        "cn": "u123456",
        "iat": now.timestamp(),
        "exp": now.timestamp() + 3600
    }
    with open('jwtgen.json', 'w') as f:
        json.dump(template, f, indent=4)
    print("Template jwtgen.json file created. You can edit this file with your payload.")

def main():
    parser = argparse.ArgumentParser(
        description="JWTGen: A CLI utility for generating and decoding JWT tokens."
    )

    allowed_algorithms = ["HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512"]

    parser.add_argument("--version", action="version", version=f"%(prog)s {get_version()}")
    parser.add_argument("--secret", type=str, help="The key to sign the JWT (required for encoding)")
    parser.add_argument("--algorithm", type=str, default="HS256", help="The algorithm to use for signing the JWT", choices=allowed_algorithms)
    parser.add_argument("--generate-template", action="store_true", help="Generate a template jwtgen.json file")
    parser.add_argument("--decode", action="store_true", help="Prompt to decode a JWT token without verification")

    args = parser.parse_args()

    if args.decode:
        token = input("Enter the JWT token to decode: ")
        logging.debug("Decoding token...")
        try:
            payload = decode_jwt(token)
            print("Decoded payload:")
            print(json.dumps(payload, indent=4))
        except Exception as e:
            logging.error(f"Failed to decode token: {e}")
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
        logging.error("Key is not provided.")
        return

    try:
        token = create_jwt(args.secret, args.algorithm, payload)
        print(f"{args.algorithm} encoded token: {token}")
    except Exception as e:
        logging.error(f"Failed to create token: {e}")

if __name__ == "__main__":
    main()
