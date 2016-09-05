import unittest

from base import BaseTestCase
from flask.ext.login import current_user


class TestHome(BaseTestCase):

    def test_max_grid_size_home_people(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )

            MAX_GRID_SIZE_HOMEPAGE_PEOPLE = 6

            for person in range(0,MAX_GRID_SIZE_HOMEPAGE_PEOPLE):
                response = self.client.post('/people', data=dict(
                    name=person, biography='The bio',
                    added_by_user_id=current_user.id, url_handle=person
                ), follow_redirects=True)

            response = self.client.get('/', content_type='html/text')

            # This depends on the text value of the home grid buttons
            self.assertEqual(response.data.count(b"View details"), MAX_GRID_SIZE_HOMEPAGE_PEOPLE)


if __name__ == '__main__':
    unittest.main()
