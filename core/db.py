from typing import AsyncGenerator

from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker, AsyncSession

# 數據庫地址
DATABASE_URL = f"sqlite+aiosqlite:///sqlite.db"

# 創建數據庫引擎
database_engine = create_async_engine(DATABASE_URL)

# 創建會話工廠函數
session_factory = async_sessionmaker(
    bind=database_engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """創建數據庫會話"""
    async with session_factory() as session:
        yield session
