from typing import List
from fastapi import APIRouter
from database import get_session
from models import User
from schemas import UserSchema
from utils import Hasher

users_route = APIRouter()

@users_route.get("")
async def get_users() -> List[User]:
    with get_session() as session:
        q = session.query(User).all()
        if q is not None:
            return q
    return []

@users_route.get("/{user_id}")
async def get_user(user_id=None) -> User:
    with get_session() as session:
        q = session.query(User).filter(User.id == user_id).first()
        if q is not None:
            return q
    return User()


@users_route.post("")
async def create_user(user: UserSchema):
    user = User(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        password=Hasher.get_password_hash(user.password)
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
