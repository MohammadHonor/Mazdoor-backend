from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.postSchema import PostCreateResponse,PostCreate
from app.models.postModel import Post
from fastapi import HTTPException
from app.models.user import User 
from app.models.postModel import Post
from sqlmodel import select
from fastapi import status

class PostRepository :
    def __init__(self,session :AsyncSession):
        self.session = session

    async def create_post(self, data : PostCreate )->PostCreateResponse:
       
        try :
            
            result = await self.session.execute(select(User).where(User.id == data.user_id))
            user = result.scalar_one_or_none()

            if not user :
                return PostCreateResponse(message=f"User whose id {data.user_id} not exist")

            new_post = Post(title = data.title , user_id = data.user_id)
            self.session.add(new_post)
            await self.session.commit()
            await self.session.refresh(new_post)
            return PostCreateResponse(message=f"user {new_post.id} post create successfully")
        except Exception as e :
            raise HTTPException(status_code=400,detail= str(e))

    async def get(self):
        try:
            result = await self.session.execute(select(Post))
            return result.scalars().all()
        except Exception as e :
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=str(e))

