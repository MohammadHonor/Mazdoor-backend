# app/db.py
from sqlmodel import SQLModel
from app.core.constents import DATABASE_URL,DEBUG
from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine, async_sessionmaker
from typing import AsyncGenerator

engine = create_async_engine(
    DATABASE_URL,
    echo=DEBUG,
    pool_size=10, 
    max_overflow=20,
)


async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
        print("✅ Database connected successfully.")
    except Exception as e:
        print(f"❌ DB connection failed: {e}")
        print(f"❌ DB connection failed: {type(e).__name__} → {e}")


