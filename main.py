from fastapi import FastAPI , Depends
from contextlib import asynccontextmanager
from app.db.database import init_db
from app.api.routes import router as all_routers
from app.dependency.auth import get_current_user
from typing import Annotated
import sqlalchemy


@asynccontextmanager
async def lifespan(app: FastAPI):
    # print(sqlalchemy.__version__)
    await init_db()
    print("🚀 App is starting...")
    yield
    print("🛑 App is shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(router=all_routers)