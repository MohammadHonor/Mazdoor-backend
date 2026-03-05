from sqlmodel import SQLModel ,Field 

class Animal(SQLModel ,table=True):
    id:int | None = Field(default=None , primary_key=True)
    name:str = Field(default="Tiger")
    habitate:str
