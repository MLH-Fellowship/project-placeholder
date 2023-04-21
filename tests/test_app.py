# test/test_app.py

from app import app
import unittest
import os
os.environ['TESTING'] = 'true'


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Week 1 - Team Portfolio</title>" in html
        # TEST HOMEPAGE: Verifying that the homepage contains specific content
        assert "Meet The Placeholders!" in html
        assert 'href="/aboutme"' in html
        print('Laura Penza')

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        # assert len(json["timeline_posts"]) == 0
        # TEST POST REQUEST
        # data = {'name': 'Laura Doe', 'email': 'Laura@example.com',
        #         'content': 'This is a test post'}
        # print("before POST request")
        # response = self.client.post("/api/timeline_post", data=data)
        # print("response", response)
        # assert response.status_code == 200
        # TEST GET REQUEST
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        # assert len(json["timeline_posts"]) == 1

        # TEST TIMELINE PAGE
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post(
            "/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post(
            "/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
