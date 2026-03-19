from fastapi import APIRouter , HTTPException
from app.core.endpoints import USER_BASE
from app.schemas.postSchema import PostCreateResponse , PostCreate
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.db.database import get_session
from app.repositories.postRepository import PostRepository
from fastapi import status


router = APIRouter(prefix=USER_BASE, tags=["Post"])

@router.post("/post", response_model=PostCreateResponse)
async def add_post (data : PostCreate , session : Annotated[AsyncSession, Depends(get_session)]):

    try :
        post_repo_object = PostRepository(session=session)
        result = await post_repo_object.create_post(data=data)
        return result
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=str(e))

@router.get("/post")
async def get_post_details(session : Annotated[AsyncSession,Depends(get_session)]):
    try:
        repo_object = PostRepository(session=session)
        return await repo_object.get()
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=str(e))
    
    


