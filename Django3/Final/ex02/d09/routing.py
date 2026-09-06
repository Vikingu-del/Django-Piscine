from chat.routing import websocket_urlpatterns as chat_ws_patterns

websocket_urlpatterns = [
    *chat_ws_patterns,
]