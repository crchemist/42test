"""t42cc tests
"""

from django.test import TestCase
from django.test.client import Client

from django.conf import settings
from django.http import HttpRequest
from django.template import TemplateDoesNotExist, RequestContext


from t42cc.models import Person, RequestModel


class T42ccTests(TestCase):
    """General tests for t42cc application
    """
    def setUp(self):
        self.client = Client()

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
        response = self.client.get('/')
        self.assertTrue('Mykola' in response.content)
        self.assertTrue('Kharechko' in response.content)

    def test_request_middleware(self):
        """Tests for RequestMiddleware
        """
        good_path = '/'
        self.client.get(good_path)
        good_path_reqs = RequestModel.objects.filter(path=good_path)
        self.assertTrue(good_path_reqs.count() > 0)

        wrong_path = '/wrong_path'
        self.assertRaises(TemplateDoesNotExist,
                  self.client.get, wrong_path)
        wrong_path_reqs = RequestModel.objects.filter(path=wrong_path)
        self.assertTrue(wrong_path_reqs.count() > 0)

    def test_context_processor(self):
        """Test context_processors.django_settings
        """
        processors = settings.TEMPLATE_CONTEXT_PROCESSORS
        self.assertIn('t42cc.context_processors.django_settings', processors)

        #check for availability of django_settings attribute in context
        context = RequestContext(HttpRequest())
        self.assertTrue(context.get('django_settings') is not None)
