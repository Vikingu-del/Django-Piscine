from django.urls import path
from . import views

app_name = "ex01"

urlpatterns = [
    path("django/", views.django_intro, name="django_intro"),
    path("display/", views.display_processes, name="display_processes"),
    path("templates/", views.template_engine, name="template_engine"),
]
