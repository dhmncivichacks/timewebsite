from flask.ext.testing import TestCase

from project import app, db
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(
            User(
                email="ad@min.com",
                password="admin",
                url_handle="admin"
            )
        )
        db.session.add(
            BlogPost(
                title="Test post",
                body="This is a test. Only a test.",
                author_id="1",
                url_handle="test_blog_post"
            )
        )
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
