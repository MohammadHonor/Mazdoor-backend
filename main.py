from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db
from app.api.routes import router as all_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("🚀 App is starting...")
    yield
    print("🛑 App is shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(router=all_routers)