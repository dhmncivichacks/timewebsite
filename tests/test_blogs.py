import unittest

from base import BaseTestCase
from flask.ext.login import current_user


class TestBlog(BaseTestCase):

    # Ensure that blog route was set up correctly
    def test_blog_route(self):
        response = self.client.get('/blog', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that new posts can be made
    def test_add_blogpost(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post('/blog', data=dict(
                title='A Post about Something', body='Here is the body.',
                author=current_user.id, url_handle="a_post_about_something "
            ), follow_redirects=True)
            self.assertIn(b'A Post about Something', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    # Ensure invalid form conveys errors
    def test_invalid_form_error(self):
        with self.client:
            response = self.client.post('blog/', data=dict(
                title=None,
                body=None
            ), follow_redirects=True)
            self.assertIn(b'FIXME ERROR', response.data)

if __name__ == '__main__':
    unittest.main()
