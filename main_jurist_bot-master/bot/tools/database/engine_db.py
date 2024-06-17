from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import MetaData, create_engine
from config import DATABASE_URL
from .models import Base


engine = create_async_engine(
    url=DATABASE_URL,
    echo = True
    )



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
