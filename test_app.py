import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Flask app!"}

def test_add(client):
    response = client.post('/add', json={"num1": 3, "num2": 4})
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}

    response = client.post('/add', json={"num1": 3})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Please provide num1 and num2"}

def test_subtract(client):
    response = client.post('/subtract', json={"num1": 10, "num2": 4})
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}

    response = client.post('/subtract', json={"num1": 10})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Please provide num1 and num2"}
