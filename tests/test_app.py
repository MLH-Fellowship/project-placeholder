import unittest
import os

from app import app

os.environ["TESTING"] = 'true'


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<title>Week 1 - Team Portfolio</title>" in html
        assert response.headers.get(
            "Content-Type") == "text/html; charset=utf-8"

    def test_timeline(self):
        response = self.client.get("/api/get_timeline_post")
        json = response.get_json()

        assert response.is_json
        assert response.status_code == 200
        assert response.headers.get("Content-Type") == "application/json"
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
