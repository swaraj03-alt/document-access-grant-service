from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Grant Service Running"


def test_get_grants():
    response = client.get("/grants")

    assert response.status_code == 200
    assert isinstance(response.json(), list)