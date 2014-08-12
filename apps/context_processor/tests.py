from django.core.urlresolvers import reverse
from django.test import TestCase


class SettingsContextTest(TestCase):

    def test_settings_components_are_in_template_context(self):
        response = self.client.get(reverse('requests'))
        self.assertIn('INSTALLED_APPS', response.context)
