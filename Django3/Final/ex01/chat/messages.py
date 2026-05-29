from typing import Literal
from pydantic import BaseModel
from chanx.messages.base import BaseMessage


class EchoPayload(BaseModel):
    message: str


class NotificationPayload(BaseModel):
    alert: str
    level: str = "info"


# Client messages
class EchoMessage(BaseMessage):
    """Message type for echoing text."""

    action: Literal["echo"] = "echo"
    payload: EchoPayload


# Server messages


class EchoResponseMessage(BaseMessage):
    """Message type for echo responses."""

    action: Literal["echo_response"] = "echo_response"
    payload: EchoPayload


class NotificationMessage(BaseMessage):
    """Message type for sending notifications."""

    action: Literal["notification"] = "notification"
    payload: NotificationPayload


# Events (for server-side broadcasting)
class SystemNotifyEvent(BaseMessage):
    action: Literal["system_notify"] = "system_notify"
    payload: NotificationPayload
