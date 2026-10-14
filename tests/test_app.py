
import os
import sys
import unittest

# Make the backend application importable
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docker", "backend"))
)

from app import app


class BackendTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["application"], "DEVOPS FA1 Backend")
        self.assertEqual(data["status"], "running")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
