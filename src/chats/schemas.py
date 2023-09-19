from pydantic import BaseModel


class ChatSchema(BaseModel):
    id: int
    user_id: int
    puppet_id: int
    chat_name: str
    chat_telegram_id: int
    type: str
