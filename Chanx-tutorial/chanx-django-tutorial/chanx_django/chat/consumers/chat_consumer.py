from chanx.channels.websocket import AsyncJsonWebsocketConsumer
from chanx.core.decorators import ws_handler
from chanx.messages.incoming import PingMessage
from chanx.messages.outgoing import PongMessage

from chat.messages import NewChatMessage

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def post_authentication(self) -> None:
        assert self.channel_layer
        self.group_name = self.scope["url_route"]["kwargs"]["group_name"]
        self.groups.append(self.group_name)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
    
    @ws_handler
    async def handle_ping(self, _message: PingMessage) -> PongMessage:
        return PongMessage()
    
    @ws_handler(output_type=NewChatMessage)
    async def handle_new_chat_message(self, message: NewChatMessage) -> None:
        await self.broadcast_message(message, exclude_current=True)