
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_valid_python_upload():
    response = client.post(
        "/validate-source",
        files={"file": ("hello.py", b"print('hello')\n", "text/x-python")},
    )

    assert response.status_code == 200
    assert response.json()["valid"] is True
    assert response.json()["filename"] == "hello.py"


def test_invalid_extension_is_rejected():
    response = client.post(
        "/validate-source",
        files={"file": ("hello.txt", b"hello", "text/plain")},
    )

    assert response.status_code == 400
    assert "valid .py filename" in response.json()["detail"]


def test_oversized_file_is_rejected():
    content = b"x" * 1_000_001

    response = client.post(
        "/validate-source",
        files={"file": ("large.py", content, "text/x-python")},
    )

    assert response.status_code == 413
    assert "1 MB limit" in response.json()["detail"]
