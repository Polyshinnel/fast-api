from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from messages.models import messages

from messages.schemas import MessageSchema

router = APIRouter(
    prefix='/messages',
    tags=["Messages"]
)


@router.get('/', response_model=list[MessageSchema])
async def get_pattern(chat_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(messages).where(messages.c.chat_id == chat_id)
    result = await session.execute(query)
    return result.all()


@router.post('/add-message')
async def add_pattern(new_message: MessageSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(messages).values(**new_message.dict())
    await session.execute(stmt)
    return {'code': 200}
