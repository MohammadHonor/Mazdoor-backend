from fastapi import FastAPI , Depends 
from contextlib import asynccontextmanager
from app.db.database import init_db
from app.api.routes import router as all_routers
from app.dependency.auth import get_current_user
from typing import Annotated
import sqlalchemy
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    # print(sqlalchemy.__version__)
    await init_db()
    print("🚀 App is starting...")
    yield
    print("🛑 App is shutting down...")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=all_routers)