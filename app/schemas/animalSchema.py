from pydantic import BaseModel

class AnimalSchema(BaseModel):
    id:int
    name:str
    habitate:str