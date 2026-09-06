from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_lobby, name="chat_lobby"),
    path("<str:room_name>/", views.chat_room_view, name="room"),
]
