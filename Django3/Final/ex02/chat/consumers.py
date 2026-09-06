from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from pydantic import ValidationError
from .models import Room, Message
from .messages import SendChatMessage


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{room_name}"

        if not user.is_authenticated:
            await self.close()
            return

        await self.accept()

        # 1. Send recent message history to the newly connected user
        history = await self.get_room_history(room_name)
        await self.send_json({
            "action": "room_history",
            "payload": {
                "messages": history
            }
        })

        # 2. Join Channel Layer Group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # 3. Broadcast join notification to everyone in the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "system.alert",
                "message": f"{user.username} has joined the chat",
            }
        )

    async def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive_json(self, content):
        try:
            validated_msg = SendChatMessage.model_validate(content)
        except ValidationError:
            return

        if validated_msg.action == "send_message":
            text = validated_msg.payload.message.strip()
            if not text:
                return

            room_name = self.scope["url_route"]["kwargs"]["room_name"]
            user = self.scope["user"]

            await self.save_message(room_name, user, text)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "username": user.username,
                    "message": text,
                }
            )

    # --- Group Handlers ---
    async def chat_message(self, event):
        await self.send_json({
            "action": "chat_message",
            "payload": {
                "username": event["username"],
                "message": event["message"]
            }
        })

    async def system_alert(self, event):
        await self.send_json({
            "action": "system_alert",
            "payload": {
                "message": event["message"]
            }
        })

    # --- Database Helpers ---
    @database_sync_to_async
    def get_room_history(self, room_name: str):
        # Get room by exact name match
        room = Room.objects.filter(name__iexact=room_name).first()
        if not room:
            return []

        # Get the last 50 messages for THIS ROOM across ALL users
        messages = list(
            Message.objects.filter(room=room)
            .select_related("user")
            .order_by("-timestamp")[:3]
        )
        
        return [
            {
                "username": msg.user.username,
                "message": msg.content
            }
            for msg in reversed(messages)
        ]

    @database_sync_to_async
    def save_message(self, room_name: str, user, content: str):
        # Case-insensitive match or create to ensure single room instance
        room, _ = Room.objects.get_or_create(name__iexact=room_name, defaults={"name": room_name})
        Message.objects.create(room=room, user=user, content=content)