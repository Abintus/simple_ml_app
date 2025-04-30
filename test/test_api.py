import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


@pytest.mark.parametrize(
    "endpoint, expected_status, expected_response",
    [
        ("/", 200, {"message": "Welcome to the ML API"}),  # Test root endpoint
        ("/health", 200, {"status": "ok"}),  # Test health check endpoint
    ],
)
def test_endpoints(endpoint, expected_status, expected_response):
    response = client.get(endpoint)
    assert response.status_code == expected_status
    assert response.json() == expected_response
