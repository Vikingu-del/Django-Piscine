"""
WebSocket routing configuration for the project.

This module defines the WebSocket URL routing structure using Chanx's
routing utilities. Routes are organized by app and mounted under /ws/.
"""

from channels.routing import URLRouter
from chanx.channels.routing import include, path

# Main WebSocket router - include app-specific routers here
ws_router = URLRouter(
    [
        # Uncomment these as you implement each app:
        # path("chat/", include("chat.routing")),
        # path("assistants/", include("assistants.routing")),
        # path("system/", include("system.routing")),
    ]
)

# Top-level router - mounts all WebSocket routes under /ws/
router = URLRouter(
    [
        path("ws/", include(ws_router)),
    ]
)
