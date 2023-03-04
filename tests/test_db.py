import unittest
from peewee import SqliteDatabase
from app import TimelinePost

MODELS = [TimelinePost]
TEST_DB = SqliteDatabase(":memory:")


class TestDB(unittest.TestCase):
    def setUp(self):
        TEST_DB.bind(MODELS, bind_refs=False, bind_backrefs=False)
        TEST_DB.connect()
        TEST_DB.create_tables(MODELS)

    def tearDown(self):
        TEST_DB.drop_tables(MODELS)
        TEST_DB.close()

    def test_timeline_post(self):
        posts = [
            TimelinePost.create(
                name='test1',
                email='test1@example',
                content='hello world'
            ),
            TimelinePost.create(
                name='test2',
                email='test2@example',
                content='hello world'
            ),
        ]

        assert posts[0].id == 1
        assert posts[1].id == 2

        stored_posts = TimelinePost.select().execute()

        assert len(stored_posts) == 2
        assert stored_posts[0].name == 'test1'
        assert stored_posts[1].name == 'test2'
