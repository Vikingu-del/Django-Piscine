from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("account/", views.account_view, name="account"),
    path("account/login/", views.ajax_login_view, name="account"),
    path("account/logout/", views.ajax_logout_view, name="account"),
]
