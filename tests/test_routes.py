import unittest
"""
Unit tests for the '/home' route to validate response status codes.
- For GET requests, the status code should be 200 (success).
- For POST requests, the status code should be 405 (method not allowed),
  as the POST method is not implemented for this route.
"""

class TestHomeRoute(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the app
        self.client = app.test_client()
        self.client.testing = True

    def test_get_home_success(self):
        """
        Test that sending a GET request to '/home' returns a 200 status code.
        """
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200, "GET request to '/home' should return 200")

    def test_post_home_not_allowed(self):
        """
        Test that sending a POST request to '/home' returns a 405 status code.
        """
        response = self.client.post('/home')
        self.assertEqual(response.status_code, 405, "POST request to '/home' should return 405")

if __name__ == "__main__":
    unittest.main()