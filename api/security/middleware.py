from api.typed import *
from prisma.models import Irequest as PrismaRequest
from json import dumps
from fastapi import Request
from urllib.parse import unquote


def use_logging(app: FastAPI) -> FastAPI:
    @app.middleware("http")
    async def log_request(request: Request, call_next: Callable):
        response = await call_next(request)
        try:
            ip = request.client.host or request.headers.get(
                "x-Forwarded-For") or request.headers.get("cf-connecting-ip")
        except:
            ip = "unknown"
        try:
            url = unquote(str(request.url))
        except:
            url = "unknown"
        try:
            headers = dumps(dict(request.headers))
        except:
            headers = "unknown"
        try:
            body = dumps(await request.json())
        except:
            body = "unknown"
        try:
            response = dumps(await response.text(encoding="utf-8"))
        except:
            response = "unknown"
        try:
            status = response.status_code
        except:
            status = "unknown"
        try:
            contentType = response.headers.get("content-type")
        except:
            contentType = "unknown"
        try:
            method = request.method
        except:
            method = "unknown"
        await PrismaRequest.prisma().create(data={
                                            "ip": ip,
                                            "url": url,
                                            "headers": headers,
                                            "body": body,
                                            "response": response,
                                            "status": status,
                                            "contentType": contentType,
                                            "method": method

                                            })
        return await call_next(request)
    return app
