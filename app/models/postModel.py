from sqlmodel import SQLModel ,Field , Relationship
from typing import Optional
# from .user import User

class Post(SQLModel , table = True ) :
    id : Optional[int] = Field(default=None , primary_key = True )
    title : str 
    user_id : int | None = Field(default=None , foreign_key = "user.id")
    user :Optional["User"]= Relationship(back_populates="posts")