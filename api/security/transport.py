from api.typed import *
from nmap import PortScannerAsync
from fastapi import APIRouter, HTTPException, WebSocket, status
from fastapi.responses import JSONResponse
from json import dumps, loads
from pathlib import Path
from boto3 import Session


UBUNTU_20_04_IMAGE_ID_US_EAST_1 = 'ami-0a313d6098716f372'
FREE_TIER_INSTANCE_ID = 't2.micro'


class TCPScanner(object):
    def __init__(self, ip: str, port: int = None):
        self.ip = ip
        self.port = port

    @property
    def scanner(self) -> PortScannerAsync:
        """Get's scanner"""
        return PortScannerAsync()

    async def scan(self) -> Dict[str, Any]:
        """Scan's a port"""
        if self.port is None:
            self.port = '1-65535'
        response = await self.scanner.scan(self.ip, self.port)
        return response

    async def scan_args(self, args: str) -> Dict[str, Any]:
        """Scan's a port with args"""
        response = await self.scanner.scan(self.ip, self.port, arguments=args)
        return response


class TCPResource(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get('/scan/{ip}')
        async def scan(ip: str):
            """Scan's a port"""
            scanner = TCPScanner(ip)
            response = await scanner.scan()
            return JSONResponse(response)

        @self.get('/scan/{ip}/{args}')
        async def scan(ip: str, args: str):
            """Scan's a port with args"""
            scanner = TCPScanner(ip, '1-65535')
            response = await scanner.scan_args(args)
            return JSONResponse(response)