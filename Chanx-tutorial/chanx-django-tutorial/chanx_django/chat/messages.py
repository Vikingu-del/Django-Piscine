from typing import Literal

from chanx.messages.base import BaseMessage
from pydantic import BaseModel

class ChatMessagePayload(BaseModel):
    message: str
    name: str


class NewChatMessage(BaseMessage):
    action: Literal["new_chat_message"] = "new_chat_message"
    payload: ChatMessagePayload