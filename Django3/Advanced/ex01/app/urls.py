from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("articles/", views.Articles.as_view(), name="articles"),
    path("home/", views.Home.as_view(), name="home"),
    path("login/", views.Login.as_view(), name="login"),
    # ask about what next_page is
    path("logout/", views.Logout.as_view(next_page="app:home"), name="logout"),
    path("publications/", views.Publications.as_view(), name="publications"),
    path("article/<int:pk>/", views.Detail.as_view(), name="detail"),
    path("favourites/", views.Favourites.as_view(), name="favourites"),
]
