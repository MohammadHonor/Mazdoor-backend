# app/db.py
from sqlmodel import SQLModel
from app.core.constents import DATABASE_URL,DEBUG
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker, AsyncSession 
from sqlalchemy.orm import DeclarativeBase 


engine = create_async_engine(
    DATABASE_URL,
    echo=DEBUG,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping = True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    # autoflush=False
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
class Base(DeclarativeBase):
    pass

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Database initialized successfully.")
    except Exception as e:
        print(f"❌ DB connection failed: {type(e).__name__} → {e}")
        raise e


