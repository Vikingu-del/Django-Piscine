from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # Keeps guests out, per the assignment rules!
def chat_lobby(request):
    # Fake data to test the frontend
    fake_rooms = [{"name": "General"}, {"name": "Tech Talk"}, {"name": "Random"}]
    return render(request, "chat/chat_lobby.html", {"rooms": fake_rooms})


@login_required
def chat_room_view(request, room_name):
    # We just pass the room_name from the URL straight to the HTML
    return render(request, "chat/chat_room.html", {"room_name": room_name})
