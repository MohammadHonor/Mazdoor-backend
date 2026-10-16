from fastapi import Depends
from typing import Annotated
from app.exceptions.credential_exception import credentials_exception
from app.core.config import settings
from app.core.security import get_payload
from jwt.exceptions import InvalidTokenError
from app.schemas.auth import TokenData
from fastapi import HTTPException
from app.schemas.userSchema import UserSchema
from app.core.security import oauth2_scheme
from app.utils.jwt_helpers import verify_password,hashed_password
from app.services.userService import get_user_info
from app.db.database import get_session



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    try:
        payload =get_payload(token)
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[UserSchema, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def authenticate_user(session,username: str, password: str):
    user = await get_user_info(username=username, session=session)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user