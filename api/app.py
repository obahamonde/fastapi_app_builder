from api.resources import *
from orjson import loads
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prisma import Prisma
from api.aws.storage import S3Resource



app_state = {
        'title': 'Routes',
        'description': 'The list of all endpoints and resources',
        'version': 'development'
    }

class FatApi(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = app_state['title']
        self.description = app_state['description']
        self.version = app_state['version']
                
        @self.get('/api', tags=['schema'])
        def docs():
            responses = []
            schemas_ = [loads(model.schema_json())
                        for name, model in prisma_models]
            for schema in schemas_:
                schema_name = schema['$ref'].replace('#/definitions/', '')
                schema_content = schema['definitions'][schema_name]

                responses.append({
                    'name': schema_name,
                    'schema': schema_content
                })
            return jsonify(responses)
        
        
        @self.on_event('startup')
        async def startup():
            global db
            db = Prisma(auto_register=True)
            await db.connect()
            
        @self.on_event('shutdown')
        async def shutdown():
            await db.disconnect()
            
        for name, model in prisma_models:
            data = loads(model.schema_json())["definitions"][name]["properties"]
            for key, value in data.items():
                if '$ref' in value:
                    data[key] = None
            required = loads(model.schema_json())["definitions"][name]["required"]
            for item in required:
                if item in ['id', 'createdAt', 'updatedAt']:
                    required.remove(item)
            data['required'] = required
            self.include_router(Resource(schema=create_model(name, __base__ = BaseSchema, field_definitions =data), model=model), prefix='/api', tags=[name], default_response_class=JSONResponse)
            