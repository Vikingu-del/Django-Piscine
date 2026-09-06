from channels.routing import URLRouter
from chanx.channels.routing import include, path

from chat.consumers.chat_consumer import ChatConsumer

router = URLRouter(
    [
        path("<str:group_name>/", ChatConsumer.as_asgi()),
    ]
)
