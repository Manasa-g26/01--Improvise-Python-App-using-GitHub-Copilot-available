from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_checksum():
    response = client.post("/checksum", json={"text": "test"})
    assert response.status_code == 200
    assert "checksum" in response.json()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
