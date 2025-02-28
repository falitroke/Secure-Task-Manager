"""Unit tests for Secure Task Manager"""
import pytest
from src.app import app, db, Task

@pytest.fixture
def client():
    """Test client fixture"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_login_success(client):
    """Test successful login"""
    response = client.post('/api/login', json={'username': 'admin', 'password': 'securepass'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_create_task(client):
    """Test creating a task with valid token"""
    login_res = client.post('/api/login', json={'username': 'admin', 'password': 'securepass'})
    token = login_res.json['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/api/tasks', json={'title': 'Test Task', 'assignee': 'user1'}, headers=headers)
    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'

def test_get_tasks(client):
    """Test retrieving tasks"""
    login_res = client.post('/api/login', json={'username': 'admin', 'password': 'securepass'})
    token = login_res.json['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    client.post('/api/tasks', json={'title': 'Test Task', 'assignee': 'user1'}, headers=headers)
    response = client.get('/api/tasks', headers=headers)
    assert response.status_code == 200
    assert len(response.json) == 1