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
