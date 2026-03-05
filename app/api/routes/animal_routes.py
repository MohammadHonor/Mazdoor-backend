
from fastapi import APIRouter , Depends , status
from app.core.endpoints import USER_BASE
from app.repositories.animalRepository import AnimalRepo
from app.schemas.animalSchema import AnimalSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_session
from fastapi import HTTPException
from typing import Annotated

router = APIRouter(prefix=USER_BASE,tags=["Animal api"])

@router.post("/animal")
async def add_animals(data:AnimalSchema,session:AsyncSession=Depends(get_session))->str:
    try :
        repo = AnimalRepo(session)
        info = await repo.create(data)
        return info
    except Exception as e :
        raise HTTPException(400,detail=str(e))
    
@router.get("/animal_list")
async def show_animal_list(session:AsyncSession = Depends(get_session))->dict:
    try:
        repo = AnimalRepo(session=session)
        return await repo.display()
        
    except Exception as e :
        raise HTTPException(400,str(e))

# @router.get("/animal/{id}")
# async def show_animal_list(id:int,session:AsyncSession = Depends(get_session))->dict:
#     try:
#         repo = AnimalRepo(session=session)
#         result = await repo.display_by_id(id=id)
#         return {"result":result}
#     except Exception as e :
#         HTTPException(400,str(e))

@router.get("/animal/{name}")
async def show_animal_list(name:str,session:AsyncSession = Depends(get_session)):
    try:
        repo = AnimalRepo(session=session)
        return await repo.display_by_name(name=name)  
    except Exception as e :
        raise HTTPException(400,str(e))
    
@router.get("/animal/id/name")
async def animal_search(session: Annotated[AsyncSession,Depends(get_session)])-> dict :
    try :
        repo = AnimalRepo(session=session)
        return await repo.get()
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


