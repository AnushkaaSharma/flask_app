import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  

def test_invalid_method():
    # Use the Flask test client
    with app.test_client() as client:
        response = client.post('/home')  
        assert response.status_code == 405, "Expected 405 Method Not Allowed"