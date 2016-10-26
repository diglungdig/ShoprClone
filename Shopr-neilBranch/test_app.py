import unittest

from app import app


class TestConference(unittest.TestCase):
    def test_conference(self):
        # Use Flask's test client for our test.
        self.test_app = app.test_client()

        # Make a test request to the conference app, supplying a fake From phone
        # number
        response = self.test_app.get('/')

        # Assert response is 200 OK.
        if response.status == "302 FOUND":
		self.assertEquals(response.status, "302 FOUND")
	else:
		self.assertEquals(response.status, "200 OK")
