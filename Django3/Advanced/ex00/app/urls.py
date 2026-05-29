from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("articles/", views.Articles.as_view(), name="articles"),
    path("home/", views.Home.as_view(), name="home"),
    path("login/", views.Login.as_view(), name="login"),
]
