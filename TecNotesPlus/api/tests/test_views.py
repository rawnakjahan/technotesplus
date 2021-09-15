import datetime
from django.test import TestCase, Client
from django.core.management import call_command
from apps.core.rbac.models import User
from django.conf import settings
from apps.core.auth.views import *
from django.urls import resolve, reverse


class TestLogin(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.api_login_url = reverse('api:login')
        self.login_page_url = reverse('auth:login')
        self.user_credentials = {"username": "admin", "password": "admin"}
        # setup basic database
        call_command('loaddata', 'import_sql/bootup.json')
        # create a new user
        self.user = User.objects.create(
            username='TestUser',
            email='test@user.com',
            password='12345678',
            first_name='Test',
            last_name='User',
            phone_number='01787878787'
        )

    def test_time_diffrence(self):
        get_difference = time_difference(
            (datetime.datetime.now() + datetime.timedelta(hours=2)),
            datetime.datetime.now()
        )
        # seconds may different but minute will be 119.
        # difference between current time and 2 hours ahead will always 119.something.
        self.assertIn('119', str(get_difference))

    def test_login_url_request_method(self) -> None:
        # Only POST is allowed as request method
        # GET request
        response = self.client.get(self.api_login_url)
        self.assertEqual(response.content, b'{"detail":"Method \\"GET\\" not allowed."}')
        self.assertEqual(response.status_code, 405)
        # POST request
        response = self.client.post(self.api_login_url, self.user_credentials)
        self.assertEqual(response.status_code, 200)
        # PATCH request
        response = self.client.patch(self.api_login_url)
        self.assertEqual(response.content, b'{"detail":"Method \\"PATCH\\" not allowed."}')
        self.assertEqual(response.status_code, 405)
        # PUT request
        response = self.client.put(self.api_login_url)
        self.assertEqual(response.content, b'{"detail":"Method \\"PUT\\" not allowed."}')
        self.assertEqual(response.status_code, 405)

    def test_login_using_credentials(self) -> None:
        # valid credentials
        response = self.client.post(self.api_login_url, self.user_credentials)
        self.assertEqual(response.status_code, 200)
        # invalid credentials
        self.user_credentials.update({"username": "Test"})
        response = self.client.post(self.api_login_url, self.user_credentials)
        self.assertEqual(response.status_code, 400)
        self.user_credentials.update({"password": "Test!q2w3e"})
        response = self.client.post(self.api_login_url, self.user_credentials)
        self.assertEqual(response.status_code, 400)

    def test_login_faild_error_message(self) -> None:
        # invalid credentials with a POST request method
        self.user_credentials.update({"username": "Test", "password": "Test!q2w3e"})
        response = self.client.post(self.api_login_url, self.user_credentials)
        self.assertEqual(response.content, b'{"detail":"<ul class=\\"errorlist nonfield\\"><li>Please enter a correct '
                                           b'user name and password. Note that both fields may be case-sensitive.</li>'
                                           b'</ul>"}'
                         )

    def test_login_user_block_after_several_unsuccessful_login_attempt(self) -> None:
        # invalid credentials
        if settings.ADVANCED_SECURITY:
            for _ in range(settings.UNSUCCESSFUL_ATTEMPT):
                self.user_credentials.update({"username": self.user.username, "password": "Test!q2w3e"})
                self.client.post(self.api_login_url, self.user_credentials)
            response = self.client.post(self.api_login_url, self.user_credentials)
            self.assertIn(b"Your account is Locked due to Unsuccessful login attempts", response.content)

























