from datetime import datetime
from pydantic import EmailStr,BaseModel,field_validator,model_validator, computed_field
from typing import Optional

class UserSchema(BaseModel):
    id :int
    username: str
    gender: str
    phone_number: str
    email: EmailStr
    password: str

    # @field_validator('username')
    # def validate_username(cls,value:str)->str:

    #     if len(value) <= 3 :
    #         raise ValueError("username must contains more than 3 character")
    #     elif len(value ) >= 20 :
    #         raise ValueError("username must contains less than 20 character")
    #     return value
    
    # @field_validator('password')
    # def strong_password(cls,value:str)->str:

        # if not any( c.isupper() for c in value):
        #     raise ValueError('Password must include at least one uppercase letter')
        
        # if not any(c.islower() for c in value):
        #     raise ValueError("Password must include at least one lowercase letter")
        
        # if not any(c.isdigit() for c in value):
        #     raise ValueError("Password must include at least one digit")
        
        # if not any(c in "!@#$%^&*()-_=+[{]}\|;:',<.>/?`~" for c in value):
        #     raise ValueError("Password must include at least one special character")
        
        # return value
    # @model_validator

    

# class ReadUser(BaseModel):
#     first_name:str
#     last_name:str

# class UserInDB(UserCreate):
#     hashed_password = str

class LoginRequest(BaseModel):
    username: str
    password: str

# class Username(BaseModel)

