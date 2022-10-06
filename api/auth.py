from http.client import HTTPException
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from fastapi import status, HTTPException

from models import User
from api import get_user_by_email
from utils import Hasher 

auth_router = APIRouter()

def authenticate(username: str, password: str) -> User:
    user = get_user_by_email(email=username)
    if user is None:
        return None
    if not Hasher.verify_password(password, user.password):
        return None
    return user


@auth_router.post("")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="username and password not match")
    access_token = jwt.encode({"sub": "user.email", "exp": datetime.utcnow() + timedelta(minutes=30)}, "HereIsSuperSecretkey", algorithm="HS256") 

    return { "access_token": access_token, "token_type": "bearer" }