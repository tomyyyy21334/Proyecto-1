from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Simple Log API", "status": "online"}

def test_create_log():
    log_data = {"level": "INFO", "message": "Test log message"}
    response = client.post("/logs/", json=log_data)
    assert response.status_code == 200
    data = response.json()
    assert data["level"] == "INFO"
    assert data["message"] == "Test log message"
    assert "id" in data
    assert "timestamp" in data

def test_get_logs():
    # Asegurarse de que hay al menos un log
    client.post("/logs/", json={"level": "ERROR", "message": "Error message"})
    response = client.get("/logs/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_logs_filter():
    client.post("/logs/", json={"level": "DEBUG", "message": "Debug message"})
    response = client.get("/logs/?level=DEBUG")
    assert response.status_code == 200
    for log in response.json():
        assert log["level"] == "DEBUG"
