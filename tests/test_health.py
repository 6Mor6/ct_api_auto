import requests 


BASE_URL = "http://localhost:8000"


def test_helth_endpoint_returns_ok():
    url = f"{BASE_URL}/api/health"


    # Act
    response = requests.get(url)


    # Assert
    assert response.status_code == 200, f"White 200, get {response.status_code}"
    body = response.json()
    assert body.get("status") == "ok", f"White status='ok', get {body}"
