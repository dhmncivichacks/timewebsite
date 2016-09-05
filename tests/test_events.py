import unittest

from base import BaseTestCase
from flask.ext.login import current_user


class TestEvents(BaseTestCase):

    # Ensure route was set up correctly
    def test_events_route(self):
        response = self.client.get('/events', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that new entries can be made
    def test_add_event(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post('/events', data=dict(
                title='An Event', description='Here is the description.',
                url_handle="an_event"
            ), follow_redirects=True)
            self.assertIn(b'An Event', response.data)
            self.assertTrue(current_user.is_active())

    # Ensure invalid form conveys errors
    def test_invalid_form_error(self):
        with self.client:
            response = self.client.post('events/', data=dict(
                title=None,
                description=None
            ), follow_redirects=True)
            self.assertIn(b'FIXME ERROR', response.data)

if __name__ == '__main__':
    unittest.main()
