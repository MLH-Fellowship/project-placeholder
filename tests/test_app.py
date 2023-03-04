import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        from app import app
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<title>Week 1 - Team Portfolio</title>" in html
        assert response.headers.get(
            "Content-Type") == "text/html; charset=utf-8"

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        json = response.get_json()
        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<title>MLH Timeline</title>" in html
        assert response.headers.get(
            "Content-Type") == "text/html; charset=utf-8"

    def test_create_timeline_post(self):
        response = self.client.post("/api/create_timeline_post", data={
                                    "name": "test", "email": "test@email.com", "content": "hello world"})

    def test_malformed_timeline_post(self):
        response = self.client.post(
            "/api/create_timeline_post", data={"email": "test@", "content": "missing name!!"})
        html = response.get_data(as_text=True)

        assert response.status_code == 400
        assert "expecting name parameter in body" in html

        response = self.client.post(
            "/api/create_timeline_post", data={"email": "test@", "name": "test", "content": ""})
        html = response.get_data(as_text=True)

        assert response.status_code == 400
        assert "arguments cannot be empty strings" in html

        response = self.client.post("/api/create_timeline_post", data={
                                    "email": "not-email", "name": "test", "content": "missing name!!"})
        html = response.get_data(as_text=True)

        assert response.status_code == 400
        assert "malformed email: not-email" in html
