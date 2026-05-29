from chanx.routing import path
from channels.routing import URLRouter

from .consumers import EchoConsumer

router = URLRouter(
    [
        path("echo/", EchoConsumer.as_asgi()),
    ]
)
