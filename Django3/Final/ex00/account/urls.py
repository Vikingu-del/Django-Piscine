from django.urls import path
from . import views

app_name = "account"


urlpatterns = [
    path("", views.account_view, name="account"),
    path("login/", views.ajax_login_view, name="login"),
    path("logout/", views.ajax_logout_view, name="logout"),
]
