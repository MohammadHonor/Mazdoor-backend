from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.models.user import User
class UserRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,user_data:UserCreate)->User:
        new_user = User(
            id=user_data.id,
            first_name= user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            email=user_data.email,
            phone=user_data.phone,
            is_active= user_data.is_active,
            is_verified= user_data.is_verified,
            created_at = user_data.created_at,
            updated_at= user_data.updated_at
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
    
    def display(self):
        print("display function")