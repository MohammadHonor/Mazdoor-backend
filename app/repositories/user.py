from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.models.user import User
class UserRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,user_data:UserCreate)->User:
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            phone_number=user_data.phone_number,
            password=user_data.password,
            is_active= True,
            is_verified= True
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
    
    def display(self):
        print("display function")