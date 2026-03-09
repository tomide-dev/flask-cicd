import pytest
from app import app

@pytest.fixture

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_add_route(client):
    response = client.get('/add/3/5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 8

def test_add_large_numbers(client):
    response = client.get('/add/100/200')
    assert response.status_code == 200
    assert response.get_json()['result'] == 300

def test_subtract_route(client):
    response = client.get('/subtract/10/4')
    assert response.status_code == 200
    assert response.get_json()['result'] == 6
