from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.animalSchema import AnimalSchema
from app.models.animalModel import Animal 
from sqlmodel import select

class AnimalRepo:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def create(self,animal_data:AnimalSchema)->str:
        animal_object = Animal(id=animal_data.id,name=animal_data.name,habitate=animal_data.habitate)
        self.session.add(animal_object)
        await self.session.commit()
        await self.session.refresh(animal_object)
        return "Animal is created"
    
    async def display(self):
        statement = select(Animal)
        result = await self.session.execute(statement=statement)
        for res in result :
            print(res)
    async def display_by_id(self,id:int)->dict:
        statment = select(Animal).where(Animal.id == id)
        result = await self.session.execute(statement=statment)
        return result.scalar()
    async def display_by_name(self,name:str)->dict:
        statment = select(Animal).where(Animal.name == name)
        result = await self.session.execute(statement=statment)
        return result.scalars().all()
    

