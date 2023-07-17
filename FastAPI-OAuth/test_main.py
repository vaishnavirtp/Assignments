from fastapi.testclient import TestClient
from fastapi import FastAPI
from jose import jwt
from main import app
from decouple import config


client = TestClient(app)
app.dependency_overrides = {}


# ------------------------------- User Signup ----------------------------
def test_incorrect_password():
    payload = {
        "username": "string",
        "email": "user@example.com",
        "full_name": "string",
        "hashed_password": "22",
    }
    response = client.post("/user/signup", json=payload)

    data = response.json()
    print(data)
    assert response.status_code == 422


def test_for_user_exists():
    payload = {
        "username": "string",
        "email": "user@example.com",
        "full_name": "string",
        "hashed_password": "string",
    }
    response = client.post("/user/signup", json=payload)

    data = response.json()
    print(data)
    assert response.status_code == 400


# def test_for_create_user():
#     payload = {
#         "username": "abcd",
#         "email": "abcd@example.com",
#         "full_name": "string",
#         "hashed_password": "abcde",
#     }
#     response = client.post("/user/signup", json=payload)

#     data = response.json()
#     print(data)
#     assert response.status_code == 201


# --------------------------------- User Login ---------------------------------
def test_user_login():
    client.headers["content-type"] = "application/x-www-form-urlencoded"
    username = "string"
    login_data = {
        "username": username,
        "password": "string",
    }
    res = client.post("/token", data=login_data)
    assert res.status_code == 200
    token = res.json().get("access_token")
    creds = jwt.decode(token, config("SECRET_KEY"), algorithms=[config("ALGORITHM")])
    assert creds["sub"] == username
    assert "token_type" in res.json()
    assert res.json().get("token_type") == "bearer"


def test_invalid_id_for_get():
    response = client.get("/songs/1222")
    assert response.status_code == 404


def test_invalid_id_for_get():
    response = client.get("/user/1")
    assert response.status_code == 200


# def test_invalid_text():
#     response = client.get("/songs/abc")
#     assert response.status_code == 422
#     assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


# def test_create_song():
#     response = client.post("/songs/")
#     assert response.status_code == 403


# def test_update_song():
#     response = client.put("/songs/2")
#     assert response.status_code == 403


# def test_delete_song():
#     response = client.delete("/1")
#     assert response.status_code == 403
