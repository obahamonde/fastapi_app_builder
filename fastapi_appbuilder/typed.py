from fastapi import FastAPI, APIRouter, File, UploadFile, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse, PlainTextResponse

from pydantic import BaseModel, BaseConfig, Field, validator, EmailStr, HttpUrl, AnyHttpUrl, AnyUrl, IPvAnyAddress, IPvAnyInterface, IPvAnyNetwork
from typing import List, Dict, Optional, Union, Callable, Any, Tuple, Coroutine

from datetime import datetime, date, time, timedelta
from uuid import UUID, uuid4

import prisma.models
from prisma import Prisma

from boto3 import Session
from botocore.exceptions import ClientError, BotoCoreError

from json import dumps, loads
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class env:
    DATABASE_URL = getenv('DATABASE_URL')