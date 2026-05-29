from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import translation


class AccessControlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        translation.activate("en")

    def test_favourites_view_requires_login(self):
        """Check that favourites is only accessible by registered users"""
        url = reverse("app:favourites")
        login_url = reverse("app:login")
        response = self.client.get(url)
        expected_url = f"{login_url}?next={url}"
        self.assertRedirects(response, expected_url, fetch_redirect_response=False)

    def test_publications_view_requires_login(self):
        """Check that publications is only accessible by registered users"""
        url = reverse("app:publications")
        login_url = reverse("app:login")
        response = self.client.get(url)
        expected_url = f"{login_url}?next={url}"
        self.assertRedirects(response, expected_url, fetch_redirect_response=False)

    def test_publish_view_requires_login(self):
        """Check that publish is only accessible by registered users"""
        url = reverse("app:publish")
        login_url = reverse("app:login")
        response = self.client.get(url)
        expected_url = f"{login_url}?next={url}"
        self.assertRedirects(response, expected_url, fetch_redirect_response=False)

    def test_logged_in_user_cannot_access_register_view(self):
        """Check that a registered user cannot access the new user creation form."""
        self.client.login(username="testuser", password="password123")
        url = reverse("app:register")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            302,
            "Logged-in user was able to access the register form.",
        )
