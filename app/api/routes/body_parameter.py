from fastapi import APIRouter,Body,File,UploadFile
from app.core import USER_BASE
from app.schemas.bodyParameterSchema import FormData
from typing import Annotated


router = APIRouter(prefix=USER_BASE)

# @router.post("/form")
# async def add_form_data(data:Annotated[FormData,Body()]):
#     print(data)
#     return data

# @router.post("/form")
# async def add_form_data(data:FormData):
#     print(data)
#     return data
@router.post("/form")
async def add_form_data(data:UploadFile = File(...)):
    print(data)
    return data

