from pydantic import BaseModel

class FormData(BaseModel):
    name:str
    role_number:int
    marks:int

class Item(BaseModel):
    name:str
    description:str
    price:int

class User(BaseModel):
    username:str
    full_name:str

class Importance(BaseModel):
    count:int

