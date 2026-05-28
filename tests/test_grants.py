from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Grant Service Running"


def test_create_grant():

    payload = {
        "document_id": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
        "grantee_id": "33333333-3333-3333-3333-333333333333",
        "permission": "view",
        "expires_at": "2027-05-30T10:00:00"
    }

    response = client.post(
        "/grants",
        json=payload
    )

    assert response.status_code == 200