import unittest

from base import BaseTestCase
from flask.ext.login import current_user


class TestPeople(BaseTestCase):

    def test_people_route(self):
        response = self.client.get('/people', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add_person(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post('/people', data=dict(
                name='Somebody Somewhere', biography='The bio',
                added_by_id=current_user.id, url_handle="somebody_somewhere"
            ), follow_redirects=True)
            self.assertIn(b'Somebody Somewhere', response.data)

    def test_invalid_form_error(self):
        with self.client:
            response = self.client.post('people/', data=dict(
                name=None,
                biography=None,
                url_handle=None
            ), follow_redirects=True)
            self.assertIn(b'FIXME ERROR', response.data)

if __name__ == '__main__':
    unittest.main()
