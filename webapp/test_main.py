from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_cities():
    response = client.get("/countries/germany")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Berlin", "Cologne", "Frankfurt", "Munich"]    
    response = client.get("/")
    assert response.status_code == 301
    assert response.url == "/docs"

def test_countries_list():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_cities_list():
    response = client.get("/countries/italy")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Florence", "Milan", "Rome", "Venice"]

def test_monthly_average():
    response = client.get("/countries/italy/rome/january")
    assert response.status_code == 200
    assert response.json() == 10.5