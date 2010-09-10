"""t42cc tests
"""

from django.test import TestCase
from django.test.client import Client

from django.conf import settings
from django.http import HttpRequest
from django.core.urlresolvers import reverse
from django.template import TemplateDoesNotExist, RequestContext
from django.contrib.auth.models import User
from django.core.management import get_commands

from t42cc import views
from t42cc.models import Person, RequestModel, LogModelModification
from t42cc.templatetags import t42tags


class T42ccTests(TestCase):
    """General tests for t42cc application
    """
    def setUp(self):
        self.client = Client()
        self.username = 'admin'
        self.password = 'passwd'
        self.user = User.objects.create_user(self.username,
                    'admin@example.com', self.password)
        self.client.login(username=self.username,
                          password=self.password)
        self.edit_view = reverse(views.edit)

    def test_calendar_widget(self):
        """Test whether calendar.js is included
        """
        edit_form_resp = self.client.get(self.edit_view)
        self.assertTrue('calendar.js' in edit_form_resp.content)

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

    def test_edit_form(self):
        """Tests for edit form
        """
        get_resp = self.client.get(self.edit_view)
        self.assertEqual(get_resp.status_code, 200)

        bad_post_resp = self.client.post(self.edit_view,
                                {'name': 'Mykola'})
        self.assertTrue('This field is required' in bad_post_resp.content)

        good_post_resp = self.client.post(self.edit_view,
                                {'name': 'Ivan',
                                 'surname': 'Petrov',
                                 'bio': 'Ivan"s bio',
                                 'contacts': 'ivan@gmail.com'})

        # redirect to index page
        self.assertEqual(good_post_resp.status_code, 302)

        person = Person.objects.get()
        self.assertEqual(person.name, 'Ivan')
        self.assertEqual(person.surname, 'Petrov')
        self.assertEqual(person.bio, 'Ivan"s bio')
        self.assertEqual(person.contacts, 'ivan@gmail.com')

    def test_edit_form_auth(self):
        """Test permissions to edit person info
        """
        self.client.logout()
        anon_resp = self.client.get(self.edit_view)
        self.assertNotEqual(anon_resp.status_code, 200)

        self.client.login(username=self.username,
                    password=self.password)
        user_resp = self.client.get(self.edit_view)
        self.assertEqual(user_resp.status_code, 200)

    def test_person_singleton(self):
        """Test possiblity to create multiple Person entities
        """
        person_count = Person.objects.count()
        self.assertEqual(person_count, 1)

        person = Person(name='Ivan',
                   surname='Ivanov',
                   bio='bio',
                   contacts='contacts')
        person.save()
        self.assertEqual(Person.objects.count(), person_count)

        person = Person.objects.get()
        self.assertEqual(person.name, 'Ivan')

        person.delete()
        person = Person.objects.get()
        self.assertEqual(person.name, 'Ivan')

    def test_request_model(self):
        """Tests for models.RequestModel
        """
        req = RequestModel(path='/some/path',
                 username='',
                 method='GET')
        req.save()
        self.assertEqual(repr(req), '<RequestModel: %s>' % req.path)

    def test_fields_order(self):
        """Test fields order in PersonForm
        """
        form = views.PersonForm()
        self.assertEqual(list(form.fields), ['contacts',
              'bio', 'birth', 'surname', 'name'])

    def test_edit_link_tag(self):
        """Test 'edit_link' tag
        """
        person = Person.objects.get()
        self.assertEqual(t42tags.edit_link(person),
                  '/admin/t42cc/person/%s/' % person.id)

    def test_printmodels_command(self):
        """Test django-admin.py printmodels command
        """
        self.assertTrue(get_commands().get('printmodels'))

    def test_modifications_log(self):
        """Test model modification logging facility
        """
        # for testing LogModelModification I will use RequestModel entry
        # test object creation


        # test object modification

        # test object removing

        # test MolgModelModification entry deleting
        # models.log_delete if clause at line 82

