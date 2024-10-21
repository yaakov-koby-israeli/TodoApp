import sys
import os

# Add the TODOAPP directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status' : 'Healthy'}