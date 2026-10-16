from fastapi import APIRouter,Depends,HTTPException,status
from app.utils.user_data import users
from typing import List,Annotated
from app.core import USER_BASE
from typing import Optional
from fastapi import Query
from fastapi import Header,Cookie
from fastapi import Response,Request
from app.repositories.userRepo import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_session
from app.schemas.userSchema import UserSchema
from app.services.userService import add_user
from fastapi import BackgroundTasks
from app.task.email_tasks import send_welcome_email
from app.dependency.auth import authenticate_user
from app.services.userService import get_user_info
from datetime import timedelta
from app.core.security import create_access_token
from app.core.config import settings
from app.schemas.auth import Token
from app.schemas.userSchema import LoginRequest

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
async def read(session_id:str=Cookie(default=None),request:Request=None):
    print(request.cookies)
    return session_id

@router.post("/register")
async def register(user_data:UserSchema, session : Annotated[AsyncSession, Depends(get_session)], background_tasks:BackgroundTasks) :
    # background_tasks.add_task(send_welcome_email,user_data.email)
    return await add_user(user_data,session)

@router.patch("/update")
async def update_user()->dict:
    pass

@router.delete("/{id}")
async def remove_user(id:int)->dict:
    return {id:"this id is deleted now"}

@router.post("/login")
async def login_user(login:LoginRequest, session:Annotated[AsyncSession,Depends(get_session)],response:Response = None ):
    user = await authenticate_user(session=session, username=login.username, password=login.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=False,   
        secure=False,     
        samesite="Strict" 
    )
    return {"message":"login successfully"}



    



