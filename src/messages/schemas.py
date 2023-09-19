from datetime import datetime

from pydantic import BaseModel


class MessageSchema(BaseModel):
    id: int
    chat_id: int
    chat_to_send_id: int
    offset_num: int
    message_hash: str
    date_enter: datetime

