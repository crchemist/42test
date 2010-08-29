"""t42cc tests
"""

from django.test import TestCase
from django.test.client import Client


from t42cc.models import Person


class T42ccTests(TestCase):
    """General tests for t42cc application
    """

    def test_person_fixtures(self):
        """Test whether Person model is loaded from fixtures
        """
        persons = Person.objects.filter(name='Mykola', surname='Kharechko')
        self.assertEqual(len(persons), 1)
        person = persons.get()
        self.assertEqual(person.bio, 'my bio')
        self.assertEqual(person.contacts, 'no contacts')

    def test_index_view(self):
        """Funtional test for index view
        """
        client = Client()
        response = client.get('/')
        self.assertTrue('Mykola' in response.content)
        self.assertTrue('Kharechko' in response.content)
