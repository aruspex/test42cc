from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Person


class ContactPageTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.url = reverse('contacts')

    def test_status_code_and_appropriate_template_usage(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contacts.html')

    def test_context_has_appropriate_person_object(self):
        response = self.client.get(self.url)
        self.assertIn('person', response.context)
        person = Person.objects.all()[0]
        self.assertEqual(person, response.context['person'])

    def test_person_model_count(self):
        people_count = Person.objects.count()
        self.assertEqual(people_count, 1)


class EditPageTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.url = reverse('edit_form')
        self.login_url = reverse('users_login')
        self.password = '123456'
        self.user = User.objects.create_user(
            username='apet', password='123456')
        self.person_params = Person.objects.values()[0]

    def _loign(self):
        self.client.post(
            self.login_url,
            {'username': self.user.username, 'password': self.password}
        )

    def test_edit_page_status_code(self):
        # Redirect to login page
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        # Login page works, and now user can edit form
        self._loign()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_form_edittion_works_fine(self):
        self._loign()
        self.person_params['name'] = 'othername'
        self.person_params['photo'] = ''
        response = self.client.post(self.url, self.person_params)
        # Redirect to contact page works fine
        self.assertEqual(response.status_code, 302)
        changed_person_name = Person.objects.all()[0].name
        self.assertEqual(changed_person_name, self.person_params['name'])

    def test_form_edition_works_with_ajax_requests(self):
        self._loign()
        self.person_params['name'] = 'othername'
        self.person_params['photo'] = ''
        response = self.client.post(
            self.url, self.person_params,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 302)
        changed_person_name = Person.objects.all()[0].name
        self.assertEqual(changed_person_name, self.person_params['name'])
