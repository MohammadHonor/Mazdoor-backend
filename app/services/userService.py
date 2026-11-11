from app.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.userSchema import UserSchema
from app.repositories.userRepo import UserRepository
from app.exceptions.custome_exception import UserException
from fastapi import HTTPException ,status
from app.utils.jwt_helpers import hashed_password



async def add_user(data:UserSchema,session: AsyncSession)->dict:
    # print(" add user service called")
    
    repo = UserRepository(session)
    
    try:
        # check already existing user
        user = await repo.get_by_email(email=data.email)
        if user : 
            raise UserException(400,message="User already exists")
        data.password = hashed_password(data.password)
        await repo.create(data)
        return {"message":f"{data.username} created successfully", "status" : status.HTTP_201_CREATED}
    except Exception as e :
        raise UserException(400,message=str(e))

async def get_user_info(email:str, session:AsyncSession):
    try:
        repo = UserRepository(session)
        result = await repo.get_by_email(email=email)
        return result
    except Exception as e :
        raise HTTPException(status_code=401,detail=str(e))