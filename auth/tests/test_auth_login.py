from django.test import TestCase


class TestAuthLogin(TestCase):
    fixtures = ['auth/fixtures/auth_user.json']

    def test_auth_login_success(self):
        response = self.client.post('/auth/login/', data={'username': 'user', 'password': 'password123'}, follow=True)
        self.assertContains(response, 'Logout')

    def test_auth_login_wrong_username_password(self):
        response = self.client.post('/auth/login/', data={'username': 'user', 'password': 'password'}, follow=True)
        self.assertContains(response, 'Wrong')

    def test_auth_login_empty_username(self):
        response = self.client.post('/auth/login/', data={'username': '', 'password': 'password'}, follow=True)
        self.assertContains(response, 'username: This field is required.')

    def test_auth_login_empty_password(self):
        response = self.client.post('/auth/login/', data={'username': 'user', 'password': ''}, follow=True)
        self.assertContains(response, 'password: This field is required.')
