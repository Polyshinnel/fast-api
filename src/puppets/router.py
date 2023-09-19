from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from puppets.models import puppets

from puppets.schemas import PuppetsSchema

router = APIRouter(
    prefix='/puppets',
    tags=["Puppets"]
)


@router.get('/', response_model=list[PuppetsSchema])
async def get_user_puppets(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(puppets).where(puppets.c.user_id == user_id)
    result = await session.execute(query)
    return result.all()


@router.post('/add-puppet')
async def add_puppet(new_puppet: PuppetsSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(puppets).values(**new_puppet.dict())
    await session.execute(stmt)
    await session.commit()
    return {'code': 200}
