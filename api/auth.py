from datetime import datetime, timedelta
from jose import jwt
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from models import User
from api import get_user_by_email
from utils import Hasher

auth_router = APIRouter()

async def authenticate(username: str, password: str) -> User:
    user = await get_user_by_email(email=username)
    if not user:
        return None
    if not Hasher.verify_password(password, user.password):
        return None
    return user


@auth_router.post("/auth")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = jwt.encode(
        {"sub": str(user.id), "exp": datetime.utcnow() + timedelta(minutes=30)},
        "HereIsSuperSecretkey",
        algorithm="HS256",
    )

    return {"access_token": access_token, "token_type": "bearer"}
