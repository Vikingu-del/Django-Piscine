from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room


# Create your views here.
@login_required
def chat_lobby(request):
    rooms = Room.objects.all()
    return render(request, "chat/chat_lobby.html", {"rooms": rooms})


@login_required
def chat_room_view(request, room_name):
    # We just pass the room_name from the URL straight to the HTML
    room = get_object_or_404(Room, name=room_name)
    messages = room.messages.all().order_by('timestamp')[:30]
    return render(request, "chat/chat_room.html", {
        "room_name": room.name,
        'messages': messages
    })
