from pydantic import BaseModel


class PatternSchema(BaseModel):
    id: int
    chat_id: int
    user_id: int
    keywords: str
    block: str
    ignore: str

