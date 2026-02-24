from fastapi import APIRouter,Depends
from app.utils.user_data import users
from typing import List,Annotated
from app.core import USER_BASE
from typing import Optional
from fastapi import Query
from fastapi import Header,Cookie
from fastapi import Response,Request
from app.repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_session
from app.schemas.user import UserCreate

router = APIRouter(prefix=USER_BASE,tags=["User"])

@router.get("/",
    
    summary="Get user by ID",
    description="""
    This endpoint returns a user by their ID.
    
    - Make sure the ID exists.
    - Returns `404` if user is not found.

    **Usage**:
    ```bash
    curl -X GET /api/v1/users/123
    ```
    """,
    tags=["User"])
# async def get_user(limit: Optional[int] = Query(default=None, ge=0),
#     skip: Optional[int] = Query(default=None, ge=0)):
#     if limit and skip :
#         print(limit,skip)
#     return Response(content="get user",status_code=200)

async def get_user(limit: Annotated[int,Query()]=None,
    skip: Annotated[int,Query(ge=0)]=None):
    if limit and skip :
        print(limit,skip)
    return Response(content="get user",status_code=200)

@router.get("/secure")
async def auth(authorize:str=Header(default=None)):
    return authorize

@router.get("/read-cookies")
async def read(session_id:str=Cookie(default=None)):
    return session_id

@router.post("/register")
async def add_user(user_data:UserCreate,session: AsyncSession = Depends(get_session))->dict:
    
    repo = UserRepository(session)
    repo.display()
    new_user = await repository.create(user_data)
    return {"message":"create successfull","data":str(new_user)}

@router.patch("/update")
async def update_user()->dict:
    pass

@router.delete("/{id}")
async def remove_user(id:int)->dict:
    return {id:"this id is deleted now"}


