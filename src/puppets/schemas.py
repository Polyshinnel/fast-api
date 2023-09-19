from pydantic import BaseModel


class PuppetsSchema(BaseModel):
    id: int
    user_id: int
    api_id: str
    api_hash: str
