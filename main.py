from fastapi import FastAPI
from api.playlists import playlists_route
from models.users import User
from schemas.users import UserCreate
from database import get_session
from config import settings

import uvicorn


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(playlists_route, prefix="/playlists", tags=["playlists"])


@app.get("/users/{user_id}")
async def get_user(user_id=None) -> User:
    with get_session() as session:
        q = session.query(User).filter(User.id == user_id).one()
        if q is not None:
            return q
    return User()


@app.post("/users")
async def create_user(user: UserCreate):
    user = User(
        last_name=user.last_name,
        first_name=user.first_name,
        email=user.email,
        password=user.password,
    )
    with get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
