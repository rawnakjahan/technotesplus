from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.core.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):

    def setUp(self) -> None:
        self.login_page_url = reverse('auth:login')
        self.logout_page_url = reverse('auth:logout')

    def test_login_page_url_resolved(self) -> None:
        response = resolve(self.login_page_url)
        # check login url redirects to the correct view
        self.assertEqual(response.func.view_class, LoginView)

    def test_logout_page_url_resolved(self) -> None:
        response = resolve(self.logout_page_url)
        # check logout url redirects to the correct view
        self.assertEqual(response.func.view_class, LogoutView)
