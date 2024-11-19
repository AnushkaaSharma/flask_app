import unittest

"""
Unit tests for the '/home' route to verify correct response status codes.
- A GET request to '/home' should return a 200 status code (OK).
- A POST request to '/home' should return a 405 status code (Method Not Allowed),
  since POST is not supported for this route.
"""

class TestHomeRoute(unittest.TestCase):
    
    def setUp(self):
        """Initialize the test client for the Flask application."""
        self.client = app.test_client()
        self.client.testing = True

    def test_get_home_success(self):
        """
        Verify that a GET request to '/home' returns a 200 OK status.
        """
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200, "Expected 200 status code for GET request to '/home'")

    def test_post_home_not_allowed(self):
        """
        Verify that a POST request to '/home' returns a 405 Method Not Allowed status.
        """
        response = self.client.post('/home')
        self.assertEqual(response.status_code, 405, "Expected 405 status code for POST request to '/home'")

if __name__ == "__main__":
    unittest.main()
