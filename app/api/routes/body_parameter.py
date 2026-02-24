from fastapi import APIRouter,Body,File,UploadFile,HTTPException
from app.core import USER_BASE
from app.schemas.bodyParameterSchema import FormData
from typing import Annotated
from app.schemas.bodyParameterSchema import Item,User , Importance


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


@router.put("/item1/{item_id}")
async def update_item(item_id:int , item:Item , user:User):
    if not item_id :
        raise HTTPException(404,detail="Item id is missing")
    result = {"item_id":item_id,"item":item, "user": user}
    return result


# here importance treated as query params
@router.put("/item2/{item_id}")
async def update_item(item_id:int , item:Item , user:User, importance:int):
    if not item_id :
        raise HTTPException(404,detail="Item id is missing")
    result = {"item_id":item_id,"item":item, "user": user,"importance":importance}
    return result

@router.put("/item4/{item_id}")
async def update_item(item_id:int , item:Item , user:User, importance:Annotated[int,Body()]):
    if not item_id :
        raise HTTPException(404,detail="Item id is missing")
    result = {"item_id":item_id,"item":item, "user": user,"importance":importance}
    return result

#Here importance treated as body parameter
@router.put("/item3/{item_id}")
async def update_item(item_id:int , item:Item , user:User, importance:Importance):
    if not item_id :
        raise HTTPException(404,detail="Item id is missing")
    result = {"item_id":item_id,"item":item, "user": user,"importance":importance}
    return result

#use of embed
@router.put("/item6/{item_id}")
async def update_item(item_id:int , item:Annotated[Item,Body(embed=True)]):
    if not item_id :
        raise HTTPException(404,detail="Item id is missing")
    result = {"item_id":item_id,"item":item,}
    return result

