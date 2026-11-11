from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.userSchema import UserSchema
from app.models.userModel import User
from sqlalchemy import select
class UserRepository:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,data:UserSchema):
        new_user = User(
            username=data.username,
            gender=data.gender,
            email=data.email,
            phone_number=data.phone_number,
            password=data.password,
            profession=data.profession,
            sub_profession=data.sub_profession,
            role=data.role,
            rating=data.rating,
            salary=data.salary,
            is_active=data.is_active,
            is_verified=data.is_verified    
        )
        print('create function called')
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return data 
    
    def display(self):
        print("display function")

    async def get_by_email(self,email:str):
        # print("username",username)
        result= await self.session.execute(select(User).where(User.email == email))
        user = result.scalars().first()
        if user :
            return user

