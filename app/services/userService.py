from app.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.userSchema import UserSchema
from app.repositories.userRepo import UserRepository
from app.exceptions.custome_exception import UserException
from fastapi import HTTPException ,status
from app.utils.jwt_helpers import hashed_password



async def add_user(data:UserSchema,session: AsyncSession)->dict:
    print(data)
    try:
        data.password = hashed_password(data.password)
        repo = UserRepository(session)
        await repo.create(data)
        return {"message":f"{data.username} created successfully", "status" : status.HTTP_201_CREATED}
    except Exception as e :
        raise UserException(400,message=str(e))

async def get_user_info(username:str, session:AsyncSession):
    try:
        repo = UserRepository(session)
        result = await repo.get_by_name(username=username)
        return result
    except Exception as e :
        raise HTTPException(status_code=401,detail=str(e))