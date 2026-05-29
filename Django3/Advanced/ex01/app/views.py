from django.views.generic import ListView, RedirectView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy  # what does reverse_lazy do?
from .models import Article, UserFavouriteArticle


# Create your views here.
class Articles(ListView):
    model = Article
    template_name = "app/articles.html"
    context_object_name = "articles"
    queryset = Article.objects.select_related("author").defer("content")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["favorite_ids"] = set(
                UserFavouriteArticle.objects.filter(user=self.request.user).values_list(
                    "article_id", flat=True
                )
            )
        return context


class Publications(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/publications.html"
    context_object_name = "articles"
    login_url = "/login/"

    def get_queryset(self):
        return (
            Article.objects.filter(author=self.request.user)
            .defer("content", "author")
            .all()
        )


class Favourites(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = "app/favourites.html"
    context_object_name = "articles"
    login_url = "/login/"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(
            user=self.request.user
        ).select_related("article", "article__author")


class Detail(DetailView):
    model = Article
    template_name = "app/detail.html"
    context_object_name = "article"


class Home(RedirectView):
    pattern_name = "app:articles"


class Login(LoginView):
    template_name = "app/login.html"

    def get_success_url(self):
        return reverse_lazy("app:home")

    def form_invalid(self, form):
        return super().form_invalid(form)


class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("app:home")
    login_url = "/login/"
