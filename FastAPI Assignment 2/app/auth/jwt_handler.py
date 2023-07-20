# This file is responsible for signing,encoding,decoding and returning JWTs.

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# This function returns generated tokens from JWT
def token_response(token: str):
    return {"access-token": token}


# Function used for signing the token
def sign_jwt(userID: str):
    payload = {"userID": userID, "expires": time.time() + 60 * 60}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token["expires"] >= time.time() else None
    except:
        return {}
