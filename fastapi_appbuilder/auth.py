from prisma.models import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, HTTPException, status, Request
from hashlib import sha256
from pydantic import  BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    email: str


class Auth(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = '/auth'
        
        @self.post("/token")
        async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
            payload = {
                'username': form_data.username,
                'password': sha256(form_data.password.encode()).hexdigest(),
                'email': form_data.client_id
            }
            user = UserIn(**payload)
            return {'access_token': user.password, 'token_type': 'bearer'}

        @self.get("/user_info")
        async def user_info(current_user: User = Depends(self.get_current_user)):
            return current_user
    
    @property
    def auth(self):
        return OAuth2PasswordBearer(tokenUrl="auth/token")
    
    async def get_current_user(self, request:Request):
        token = request.headers.get("Authorization").split(" ")[1]
        try:
            return await User.prisma().find_unique(
                where={'token': token}
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )