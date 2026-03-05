from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.animalSchema import AnimalSchema
from app.models.animalModel import Animal 

class AnimalRepo:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,animal_data:AnimalSchema)->str:
        animal_object = Animal(id=animal_data.id,name=animal_data.name,habitate=animal_data.habitate)
        self.session.add(animal_object)
        await self.session.commit()
        await self.session.refresh(animal_object)
        return "Animal is created"
