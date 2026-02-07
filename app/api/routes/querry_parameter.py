from fastapi import APIRouter
from app.core import USER_BASE
from fastapi import Query
from typing import Literal,Annotated
from app.schemas.QueryParameterSchema import QueryParameterSchema

router = APIRouter(prefix=USER_BASE)
@router.get("/item")
async def read_info(skip:int = 10 , limit:int=20):
    return [f"skip {skip} and limit {limit}"]

@router.get("/item2")
async def read_info(filter_query : Annotated[QueryParameterSchema,Query()] ):
    return filter_query

