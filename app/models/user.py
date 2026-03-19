from sqlmodel import SQLModel,Field,Column,DateTime,func,Relationship
from typing import Optional
from pydantic import EmailStr
from enum import Enum
from datetime import datetime
# from app.models.postModel import Post

class UserRole(str,Enum):
    OWNER = "owner"
    USER = "user"

class Profession(str,Enum):
    ARCHITECTURE = "architecture"
    LABOUR= "labour"
    CARPENTER = "carpenter"
    ELECTRICIAN = "electrician"
    PLUBMER = "plumber"

class User(SQLModel,table=True):
    id: Optional[int] | None = Field(default=None,primary_key=True)
    username: str
    email: EmailStr
    phone_number: str
    role:UserRole = UserRole.USER
    profession:Profession = Profession.LABOUR
    password:str
    is_active: Optional[bool]
    is_verified: Optional[bool]
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=func.now()) )
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=func.now() , server_onupdate=func.now()))
    posts: list["Post"] = Relationship(back_populates="user")