from channels.routing import URLRouter
from chanx.channels.routing import path
from chat.consumers import ChatConsumer

router = URLRouter(
    [
        path("ws/chat/", ChatConsumer.as_asgi()),
    ]
)
