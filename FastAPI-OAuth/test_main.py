from fastapi.testclient import TestClient
from fastapi import FastAPI
from http import HTTPStatus
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
        "password": "22",
    }
    response = client.post("/user/signup", json=payload)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_for_user_exists():
    payload = {
        "username": "string",
        "email": "user@example.com",
        "full_name": "string",
        "password": "string",
    }
    response = client.post("/user/signup", json=payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_for_create_user():
    payload = {
        "username": "abcde",
        "email": "abcdef@example.com",
        "full_name": "string",
        "password": "abcde",
    }
    response = client.post("/user/signup", json=payload)
    assert response.status_code == HTTPStatus.CREATED


# --------------------------------- User Login ---------------------------------
def test_user_login():
    client.headers["content-type"] = "application/x-www-form-urlencoded"
    username = "string"
    login_data = {
        "username": username,
        "password": "string",
    }
    res = client.post("/token", data=login_data)
    assert res.status_code == HTTPStatus.OK
    token = res.json().get("access_token")
    creds = jwt.decode(token, config("SECRET_KEY"), algorithms=[config("ALGORITHM")])
    assert creds["sub"] == username
    assert "token_type" in res.json()
    assert res.json().get("token_type") == "bearer"


def test_invalid_id_for_song():
    response = client.get("/songs/1222")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_invalid_id_for_user():
    response = client.get("/user/1")
    assert response.status_code == HTTPStatus.OK
