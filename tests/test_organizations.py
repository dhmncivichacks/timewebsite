import unittest

from base import BaseTestCase


class TestOrganizations(BaseTestCase):

    def test_organizations_route(self):
        response = self.client.get('/organizations', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add_organization(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post('/organizations', data=dict(
                name='Someorg Somewhere', description='The description',
                url_handle="someorg_somewhere"
            ), follow_redirects=True)
            self.assertIn(b'Someorg Somewhere', response.data)

    def test_invalid_form_error(self):
        with self.client:
            response = self.client.post('organizations/', data=dict(
                name=None,
                description=None,
                url_handle=None
            ), follow_redirects=True)
            self.assertIn(b'FIXME ERROR', response.data)

if __name__ == '__main__':
    unittest.main()
