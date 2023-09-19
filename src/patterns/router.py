from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from patterns.models import patterns

from patterns.schemas import PatternSchema

router = APIRouter(
    prefix='/patterns',
    tags=["Patterns"]
)

@router.get('/', response_model=list[PatternSchema])
async def get_pattern(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(patterns).where(patterns.c.user_id == user_id)
    result = await session.execute(query)
    return result.all()


@router.post('/add-pattern')
async def add_pattern(new_pattern: PatternSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(patterns).values(**new_pattern.dict())
    await session.execute(stmt)
    return {'code': 200}
