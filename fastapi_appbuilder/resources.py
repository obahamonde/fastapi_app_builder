from .schemas import BaseSchema, prisma_models
from pydantic import create_model
from fastapi import Request, Response, APIRouter
from prisma import Prisma
import prisma.models

class Resource(APIRouter):
    def __init__(self, schema: BaseSchema,
                 model: prisma.models.BaseModel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = schema
        self.model = model
        self.prefix = f'/{model.__name__}'

        @self.get('/')
        async def index():
            return await self.model.prisma().find_many()
        
        @self.get('/{id}')
        async def show(id: str):
            return await self.model.prisma().find_unique(
                where={'id': id})
            
        @self.get('/{field}/{value}')
        async def find(field: str, value: str, limit: int = 10, skip: int = 0, operator: str = 'equals'):
            return await self.model.prisma().find_many(
                where={field: {operator: value}},
                take=limit,
                skip=skip
            )
            
        @self.get('/{field}/{value}/{operator}')
        async def search(field: str, value: str, operator: str = 'contains'):
            return await self.model.prisma().find_many(
                where={field: {operator: value}},
                take=32,
            )

            
        @self.post('/')
        async def create(schema: self.schema):
            return await self.model.prisma().create(
                data=schema.dict(exclude_unset=True)
            )
            
        @self.post('/{id}')
        async def update(id: str, schema: self.schema):
            return await self.model.prisma().upsert(
                where={'id': id},
                data={
                    'create': schema.dict(exclude_unset=True),
                    'update': schema.dict(exclude_unset=True)
                })
            
            
        @self.put('/{id}')
        async def replace(id: str, schema: self.schema):
            return await self.model.prisma().update(
                where={'id': id},
                data=schema.dict(exclude_unset=True)
            )
        
        @self.delete('/{id}')
        async def delete(id: str):
            return await self.model.prisma().delete(
                where={'id': id}
            )