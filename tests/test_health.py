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


def test_gealth_endpoint_rejects_post():

    response = requests.post(f"{BASE_URL}/api/health")
    assert response.status_code == 405, f"White code 405, return {response.status_code}"
