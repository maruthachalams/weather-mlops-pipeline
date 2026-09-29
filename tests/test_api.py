from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "My Weather API is alive!"}

def test_predict_endpoint():
    response = client.get("/predict/5")
    assert response.status_code == 200

    data = response.json()

    assert "city" in data
    assert "day_input" in data

    assert data["day_input"] == 5