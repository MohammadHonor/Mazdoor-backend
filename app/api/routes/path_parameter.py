from fastapi import APIRouter
from app.core import USER_BASE

router = APIRouter(prefix=USER_BASE,tags=["User"])

@router.get("/files/{file_name}")
async def read_file(file_name: str):
    return {"file_name": file_name}