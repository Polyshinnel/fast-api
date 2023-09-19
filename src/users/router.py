from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from users.models import users

from users.schemas import UserSchema

router = APIRouter(
    prefix='/users',
    tags=["Users"]
)


@router.get('/', response_model=list[UserSchema])
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.id == user_id)
    result = await session.execute(query)
    return result.all()


@router.post('/add-user')
async def add_user(new_user: UserSchema, session: AsyncSession = Depends(get_async_session)):
    query = insert(users).values(**new_user.dict())
    result = await session.execute(query)
    return result.all()
