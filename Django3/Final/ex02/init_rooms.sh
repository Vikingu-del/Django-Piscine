#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=== Initializing Default Chat Rooms ==="

# Check if manage.py exists
if [ ! -f "manage.py" ]; then
    echo "Error: manage.py not found in the current directory."
    exit 1
fi

# Execute Python snippet inside Django shell
python manage.py shell <<'EOF'
from chat.models import Room

room_names = ["General", "Random", "Dev"]

for name in room_names:
    Room.objects.get_or_create(name=name)

rooms = list(Room.objects.values_list('name', flat=True))
print(f"Active rooms in database: {rooms}")
EOF

echo "=== Room Initialization Complete ==="
