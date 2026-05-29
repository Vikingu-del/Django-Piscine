"""
ASGI config for d09 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.sessions import CookieMiddleware
from chanx.channels.routing import include

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d09.settings")
django_asgi_app = get_asgi_application()

routing = {
    "http": django_asgi_app,
    "websocket": CookieMiddleware(include("d09.routing")),
}

application = ProtocolTypeRouter(routing)
