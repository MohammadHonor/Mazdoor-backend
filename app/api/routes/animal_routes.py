
from fastapi import APIRouter , Depends
from app.core.endpoints import USER_BASE
from app.repositories.animalRepository import AnimalRepo
from app.schemas.animalSchema import AnimalSchema
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_session
from fastapi import HTTPException

router = APIRouter(prefix=USER_BASE,tags=["Animal api"])

@router.post("/animal")
async def add_animals(data:AnimalSchema,session:AsyncSession=Depends(get_session))->str:
    try :
        repo = AnimalRepo(session)
        info = await repo.create(data)
        return info
    except Exception as e :
        raise HTTPException(400,detail=str(e))

