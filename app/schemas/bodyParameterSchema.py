from pydantic import BaseModel

class FormData(BaseModel):
    name:str
    role_number:int
    marks:int