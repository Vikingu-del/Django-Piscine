from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Article, UserFavouriteArticle


class FavoritesLogicTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = User.objects.create_user(
            username="author", password="password123"
        )
        self.user = User.objects.create_user(username="reader", password="password123")

        self.article = Article.objects.create(
            title="Test Article",
            synopsis="A short summary",
            content="Full content here",
            author=self.author,
        )

        self.client.login(username="reader", password="password123")

    def test_toggle_prevents_duplicate_favorites(self):
        """Verify that favoriting an article twice removes it (toggles), preventing duplicates."""
        url = reverse("app:favorite", kwargs={"pk": self.article.pk})

        self.client.post(url)
        self.assertEqual(
            UserFavouriteArticle.objects.filter(
                user=self.user, article=self.article
            ).count(),
            1,
        )

        self.client.post(url)
        self.assertEqual(
            UserFavouriteArticle.objects.filter(
                user=self.user, article=self.article
            ).count(),
            0,
        )

    def test_database_integrity_unique_constraint(self):
        """Check that the database count never exceeds 1 if logic were to fail."""
        url = reverse("app:favorite", kwargs={"pk": self.article.pk})

        # Simulate two rapid additions
        self.client.post(url)
        self.client.post(url)

        count = UserFavouriteArticle.objects.filter(
            user=self.user, article=self.article
        ).count()
        self.assertLessEqual(
            count,
            1,
            "The database contains duplicate favorites for the same user and article!",
        )
