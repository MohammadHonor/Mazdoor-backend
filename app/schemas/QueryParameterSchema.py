from pydantic import BaseModel,Field

class QueryParameterSchema(BaseModel):
    skip : int = Field(10,ge=20,le=50)
    limit : int = Field(1,ge=10,le=15)