creating rooms

python manage.py shell

from chat.models import Room

room_names = ["General", "Random", "Dev"]

for name in room_names:
    Room.objects.get_or_create(name=name)

print("Created rooms:", list(Room.objects.values_list('name', flat=True)))
exit()