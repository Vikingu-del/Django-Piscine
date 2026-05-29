from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def room_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/room_list.html")


def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(request, "chat/room.html", {"room_name": room_name})
