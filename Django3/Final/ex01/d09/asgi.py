import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import d09.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d09.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(d09.routing.websocket_urlpatterns)
        ),
    }
)