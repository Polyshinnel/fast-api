from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from chats.models import chats

from chats.schemas import ChatSchema

router = APIRouter(
    prefix='/chats',
    tags=["Chats"]
)


@router.get('/', response_model=list[ChatSchema])
async def get_chats(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(chats).where(chats.c.user_id == user_id)
    result = await session.execute(query)
    return result.all()


@router.post('/add-chat')
async def add_pattern(new_chat: ChatSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(chats).values(**new_chat.dict())
    await session.execute(stmt)
    return {'code': 200}
