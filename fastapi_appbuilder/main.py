from fastapi_appbuilder.resources import *
from fastapi_appbuilder.auth import Auth
from json import loads
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocket, WebSocketDisconnect
from prisma import Prisma
from subprocess import check_output


web = StaticFiles(directory="www", html=True)


commands_available = {
    "install": check_output(["sudo", "pip", "install", "prisma"]).decode("utf-8"),
    "fetch": check_output(["sudo", "prisma","py","fetch"]).decode("utf-8"),
    "generate": check_output(["sudo","prisma","generate"]).decode("utf-8"),
    "push": check_output(["sudo", "prisma","db","push"]).decode("utf-8"),
    "pull": check_output(["sudo","prisma","db","pull"]).decode("utf-8"),   
    }



def ws_process(data):
    if data in commands_available:
        return commands_available[data]
    else:
        return "Unknown command"


class AppBuilder(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "FastAPI Prisma"
        self.description = "Schema Driven API with automatic CRUD operations"
        self.version = "0.0.1"
                
        @self.get('/api', tags=['schema'])
        async def api():
            responses = []
            schemas_ = [loads(model.schema_json())
                        for name, model in prisma_models]
            for schema in schemas_:
                schema_name = name
                schema_content = schema

                responses.append({
                    'name': schema_name,
                    'schema': schema_content
                })
            return responses
        
        
        @self.on_event('startup')
        async def startup():
            global db
            db = Prisma(auto_register=True)
            await db.connect()
            
        @self.on_event('shutdown')
        async def shutdown():
            await db.disconnect()
            
        for name, model in prisma_models:
            self.include_router(
                Resource(
                    schema=create_model(
                        name, __base__ = BaseSchema, 
                        field_definitions ={field.name: field.type_.__name__ for field in model.__fields__.values()}),
                    model=model), 
                prefix='/api', 
                tags=[name], 
                default_response_class=JSONResponse)
            
        @self.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            try:
                while True:
                    data = await websocket.receive_text()
                    await websocket.send_text(ws_process(data))
            except WebSocketDisconnect:
                print("Client disconnected")

        @self.get("/api/prisma")
        async def prisma_get():
            with open("prisma/schema.prisma", "r") as f:
                prisma_schema = f.read()
            return PlainTextResponse(prisma_schema)

        @self.post("/api/prisma")
        async def prisma_post(text:bytes=Body(...)):
            prisma_schema = text.decode("utf-8")
            with open("prisma/schema.prisma", "w") as f:
                f.write(prisma_schema)
            return {"message": "Prisma schema updated", "type": "success"}

        self.include_router(Auth(), prefix='/api', tags=['auth'])
        self.mount("/", web)
                    