from pydantic import BaseModel

class ChatMessagePayload(BaseModel):
    message: str

class SendChatMessage(BaseModel):
    action: str = "send_message"
    payload: ChatMessagePayload