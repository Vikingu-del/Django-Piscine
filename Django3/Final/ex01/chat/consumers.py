from chanx.core.decorators import ws_handler, event_handler, channel
from chanx.channels.websocket import AsyncJsonWebsocketConsumer
from chanx.messages.incoming import PingMessage
from chanx.messages.outgoing import PongMessage
from .messages import (
    EchoMessage,
    EchoResponseMessage,
    NotificationMessage,
    SystemNotifyEvent,
    EchoPayload,
    NotificationPayload,
)


@channel(name="chat", description="Simple chat and echo system", tags=["demo"])
class ChatConsumer(AsyncJsonWebsocketConsumer[SystemNotifyEvent]):
    groups = ["general_chat"]

    @ws_handler(summary="Handle ping requests")
    async def handle_ping(self, message: PingMessage) -> PongMessage:
        return PongMessage()

    @ws_handler(
        summary="Echo messages back to sender",
        description="Returns the same message with a prefix",
    )
    async def handle_echo(self, message: EchoMessage) -> EchoResponseMessage:
        return EchoResponseMessage(
            payload=EchoPayload(message=f"Echo: {message.payload.message}")
        )

    @ws_handler(
        summary="Broadcast message to all connected clients",
        output_type=NotificationMessage,
    )
    async def handle_broadcast(self, message: EchoMessage) -> None:
        # Broadcast to all clients in the group
        await self.broadcast_message(
            NotificationMessage(
                payload=NotificationPayload(
                    alert=f"Broadcast: {message.payload.message}", level="info"
                )
            )
        )

    @event_handler
    async def handle_system_notify(
        self, event: SystemNotifyEvent
    ) -> NotificationMessage:
        """Handle system notifications from background tasks."""
        return NotificationMessage(payload=event.payload)
