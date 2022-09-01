from django.test import TestCase


class TestAuthRegister(TestCase):
    fixtures = ['auth/fixtures/auth_user.json']

    def test_auth_register_success(self):
        response = self.client.post('/auth/register/', data={'username': 'newuser', 'password': 'password123'},
                                    follow=True)
        self.assertContains(response, 'Successfully Created User!')

    def test_auth_register_existing_user(self):
        response = self.client.post('/auth/register/', data={'username': 'user', 'password': 'password123'},
                                    follow=True)
        self.assertContains(response, 'Username already exists')

    def test_auth_register_password_invalid_length(self):
        response = self.client.post('/auth/register/', data={'username': 'invalid', 'password': 'user'}, follow=True)
        self.assertContains(response, 'password: Ensure this value has at least 8 characters')

    def test_auth_register_empty_username(self):
        response = self.client.post('/auth/register/', data={'username': '', 'password': 'password123'}, follow=True)
        self.assertContains(response, 'username: This field is required.')
