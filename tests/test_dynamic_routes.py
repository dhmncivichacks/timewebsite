import unittest
import uuid

from base import BaseTestCase

from project import db
from project.models import Event
from project.models import Organization
from project.models import Person


class TestDynamicRoutes(BaseTestCase):

    def test_dynamic_route_event(self):
        sample_event = str(uuid.uuid4())
        db.session.add(
            Event(
                title=sample_event,
                url_handle=sample_event,
                description=sample_event
            )
        )
        db.session.commit()
        response = self.client.get(
            '/' + sample_event,
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(sample_event, response.data.decode('utf8'))

    def test_dynamic_route_organization(self):
        sample_organization = str(uuid.uuid4())
        db.session.add(
            Organization(
                name=sample_organization,
                url_handle=sample_organization,
                description=sample_organization
            )
        )
        db.session.commit()
        response = self.client.get(
            '/' + sample_organization,
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(sample_organization, response.data.decode('utf8'))

    def test_dynamic_route_person(self):
        sample_person = str(uuid.uuid4())
        db.session.add(
            Person(
                name=sample_person,
                url_handle=sample_person,
                biography=sample_person,
                added_by_user_id=1  # admin
            )
        )
        db.session.commit()
        response = self.client.get(
            '/' + sample_person,
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(sample_person, response.data.decode('utf8'))

    def test_dynamic_route_404(self):
        sample_404 = str(uuid.uuid4())
        response = self.client.get(
            '/' + sample_404,
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
