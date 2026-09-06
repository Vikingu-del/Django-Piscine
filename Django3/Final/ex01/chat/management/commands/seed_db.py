from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from chat.models import Room

User = get_user_model()

class Command(BaseCommand):
    help = "Seed database with default rooms and test users"

    def handle(self, *args, **options):
        # 1. Create Default Rooms
        default_rooms = ["General", "Random", "Tech"]
        for room_name in default_rooms:
            room, created = Room.objects.get_or_create(name=room_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created room: {room_name}"))

        # 2. Create Test Users (if needed for evaluation)
        test_users = [("user1", "pass123"), ("user2", "pass123")]
        for username, password in test_users:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                self.stdout.write(self.style.SUCCESS(f"Created user: {username}"))
                