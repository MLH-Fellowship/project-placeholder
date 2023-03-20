import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for test.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
      # Not strictly necessary since SQLite in-memory database only live
      # for duraction of the connection, and in the next steps we close
      # the connection... but a good practice all the same.
      test_db.drop_tables(MODELS)

      # Close connection to db.
      test_db.close()
    
    def test_timeline_post(self):
      #  Create 2 timeline posts.
      first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
      assert first_post.id == 1
      second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
      assert second_post.id == 2
      
      assert first_post.name == "John Doe"
      assert first_post.email == "john@example.com"
      assert first_post.content == "Hello world, I\'m John!"

      assert second_post.name == "Jane Doe"
      assert second_post.email == "jane@example.com"
      assert second_post.content == "Hello world, I\'m Jane!"

