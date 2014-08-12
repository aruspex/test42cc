from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class UerAuthTest(TestCase):
    fixutres = ['contact/fixtures/initial_data.json']

    def setUp(self):
        self.url = reverse('contacts')
        self.password = '123456'
        self.register_url = reverse('users_signup')
        self.login_url = reverse('users_login')
        self.logout_url = reverse('users_logout')
        self.new_user_params = {
            'username': 'apet',
            'password': '123456',
            'verify_password': '123456'
        }

    def test_signup_works_as_should(self):
        # Register new Uer
        self.client.post(self.register_url, self.new_user_params)
        # he appears in User...
        self.assertEqual(
            User.objects.all()[0].username,
            self.new_user_params['username']
        )
        # ... and he logged in
        response = self.client.get(self.url)
        self.assertTrue(response.context['user'].is_authenticated())

    def test_login_and_logout_works_too(self):
        # Register new user (he logged in)
        self.client.post(self.register_url, self.new_user_params)
        # User goes to logout page and now he isn't logged in
        response_logout = self.client.get(self.logout_url)
        self.assertEqual(response_logout.status_code, 302)
        response_anon = self.client.get(self.url)
        self.assertFalse(response_anon.context['user'].is_authenticated())

        # User hits login link, passes arguments and now he logged in
        self.client.post(
            self.login_url,
            {
                'username': self.new_user_params['username'],
                'password': self.new_user_params['password']
            })
        response_auth = self.client.get(self.url)
        self.assertTrue(response_auth.context['user'].is_authenticated())
