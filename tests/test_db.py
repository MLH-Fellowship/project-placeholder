# test_db.py

import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of all
        # models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(
            name='Laura Penza', email='laura@gmail.com', content='Hello, I\'m Laura!')
        assert first_post.id == 1
        second_post = TimelinePost.create(
            name='Jane Doe', email='jane@example.com', content='Hello, I\'m Jane!')
        assert second_post.id == 2

        # Get timeline posts and assert that they are correct
        stored_posts = TimelinePost.select()
        assert len(stored_posts) == 2
