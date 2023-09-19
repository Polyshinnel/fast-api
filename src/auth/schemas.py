from datetime import datetime

from pydantic import BaseModel


class AdminUserSchema(BaseModel):
    id: int
    login: str
    password: str
    token: str
    date_enter: datetime
