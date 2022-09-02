from django.test import TestCase
from django.contrib.auth.models import User
from button_clicks.models import ButtonClickLog
from django.contrib.auth.hashers import make_password


class TestButtonClick(TestCase):
    fixtures = ['auth/fixtures/auth_user.json']

    def setUp(self) -> None:
        self.user = User.objects.first()

    def test_button_click_api_without_login(self):
        response = self.client.get('/clicks/api/', follow=True)
        # make sure user redirected to login page
        self.assertContains(response, 'Sign in')

    def test_button_click_api_with_login(self):
        # make sure the table is empty
        ButtonClickLog.objects.all().delete()

        self.client.force_login(self.user)
        response = self.client.get('/clicks/api/')
        self.assertEqual(response.json()['status'], 'success')

        response_home = self.client.get('/', follow=True)
        self.assertContains(response_home, '<h1 class="text-white" id="numClick">1</h1>')

    def test_button_click_api_limit(self):
        # make sure the table is empty
        ButtonClickLog.objects.all().delete()

        self.client.force_login(self.user)
        for _ in range(5):
            self.client.get('/clicks/api/')

        response = self.client.get('/clicks/api/')
        self.assertEqual(response.json()['status'], 'error')

    def test_button_click_first_user_limit_then_other_user_click(self):
        # create new user
        new_user = User(
            username='test',
            password=make_password('test')
        )
        new_user.save()

        # make sure the table is empty
        ButtonClickLog.objects.all().delete()

        # login with first user
        self.client.force_login(self.user)
        for _ in range(5):
            self.client.get('/clicks/api/')

        # login with new user
        self.client.force_login(new_user)
        response = self.client.get('/clicks/api/')
        self.assertEqual(response.json()['status'], 'success')
