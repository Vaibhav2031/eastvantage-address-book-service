from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_address():
    payload = {
        "name": "Home",
        "street": "MG Road",
        "city": "Pune",
        "latitude": 18.5204,
        "longitude": 73.8567
    }

    response = client.post("/api/v1/addresses/", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Home"
    assert data["city"] == "Pune"
    assert "id" in data


def test_get_nearby_addresses():
    # create two addresses
    client.post("/api/v1/addresses/", json={
        "name": "Office",
        "street": "Baner",
        "city": "Pune",
        "latitude": 18.5590,
        "longitude": 73.7868
    })

    client.post("/api/v1/addresses/", json={
        "name": "FarPlace",
        "street": "Mumbai",
        "city": "Mumbai",
        "latitude": 19.0760,
        "longitude": 72.8777
    })

    response = client.get(
        "/api/v1/addresses/nearby",
        params={
            "center_lat": 18.5204,
            "center_lon": 73.8567,
            "max_km": 20
        }
    )

    assert response.status_code == 200

    data = response.json()

    # should find Pune addresses but not Mumbai
    assert any(addr["name"] == "Office" for addr in data)