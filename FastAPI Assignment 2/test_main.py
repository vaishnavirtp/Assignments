from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_songs():
    response = client.get("/")
    assert response.status_code == 200


def test_get_song():
    response = client.get("/songs/1")
    assert response.status_code == 200


def test_invalid_id_for_get():
    response = client.get("/songs/3213")
    assert response.status_code == 404
    assert response.json() == {"detail": "id not found"}


def test_invalid_text():
    response = client.get("/songs/abc")
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_create_song():
    response = client.post("/songs/")
    assert response.status_code == 403


def test_update_song():
    response = client.put("/songs/2")
    assert response.status_code == 403


def test_delete_song():
    response = client.delete("/1")
    assert response.status_code == 403
