from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import HttpRequestInfo


class HttpMiddlewareTest(TestCase):
    fixtures = ['contact/fixtures/initial_data.json']

    def setUp(self):
        self.url = reverse('requests')

    def test_requests_are_properly_add_to_db_with_priorty_equals_one(self):
        for request_index in xrange(1, 4):
            self.client.get(self.url)
            saved_requests_count = HttpRequestInfo.objects.count()
            self.assertEqual(
                HttpRequestInfo.objects.latest('date').priority,
                1
            )
            self.assertEqual(saved_requests_count, request_index)

    def test_view_for_get_and_post_requests(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Method', response.content)
        # POST appears in body after POST request
        self.assertNotIn('POST', response.content)
        self.client.post(self.url)
        response = self.client.get(self.url)
        self.assertIn('POST', response.content)
