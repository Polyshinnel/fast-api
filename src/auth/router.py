from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from auth.models import admin_users

from auth.schemas import AdminUserSchema

router = APIRouter(
    prefix='/auth',
    tags=["Authorization"]
)


@router.post('/token', response_model=list[AdminUserSchema])
async def get_token(login: str, password: str, session: AsyncSession = Depends(get_async_session)):
    query = select(admin_users).where((admin_users.c.login == login) & (admin_users.c.password == password))
    result = await session.execute(query)
    return result.all()
