from sqlmodel import SQLModel 
from pydantic import Field

from pydantic import BaseModel

class PostCreate(BaseModel):
    id : int
    title:str
    user_id : int 

class PostCreateResponse(BaseModel) :
    message : str