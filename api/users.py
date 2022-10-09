
import uuid
from sqlalchemy.dialects.postgresql import UUID
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy import update
from models import User
from schemas import UserSchema
from utils import Hasher
from database import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")
users_route = APIRouter()

async def get_user_by_email(email: str) -> User:
    with get_session() as session:
        q = session.query(User).filter(User.email == email).first()
        if q is not None:
            return q
    return None


async def get_user_by_id(user_id: UUID) -> User:
    with get_session() as session:
        q = session.query(User).filter(User.id == user_id).first()
        if q is not None:
            return q
    return None


@users_route.get("/users")
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    my_token = jwt.decode(token=token, key="HereIsSuperSecretkey")
    crurrent_user = await get_user_by_id(uuid.UUID(my_token['sub']).hex)
    if not crurrent_user:
        return None
    return crurrent_user    


@users_route.post("/users")
async def create_user(user: UserSchema) -> User:
    exist_user = await get_user_by_email(user.email)
    if exist_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address already registered",
        )

    user = User(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
    )
    with get_session() as session:
        session.begin()
        try:
            session.add(user)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            session.refresh(user)
            return user


@users_route.put("/users")
async def update_user(user: UserSchema, token: str = Depends(oauth2_scheme)) -> User:
    my_token = jwt.decode(token=token, key="HereIsSuperSecretkey")
    current_user = await get_user_by_id(my_token['sub'])
    if not current_user:
        return None

    with get_session() as session:
        stmt = (
        update(User)
        .where(User.id == current_user.id)
        .values(middle_name=user.middle_name)
        .execution_options(synchronize_session="fetch"))

        result = session.execute(stmt)
        print(result.rowcount)
        
    return current_user   