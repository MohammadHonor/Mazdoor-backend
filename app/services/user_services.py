from app.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
from app.exceptions.custome_exception import UserException


async def add_user(user_data:UserCreate,session: AsyncSession)->dict:
    
    try:
        repo = UserRepository(session)
        await repo.create(user_data)
        return {"message":"create successfull"}
    except Exception as e :
        raise UserException(400,message=str(e))