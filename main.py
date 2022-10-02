from fastapi import FastAPI
from fastapi import APIRouter
from models.users import User
from database import get_session

app = FastAPI()
router = APIRouter()

@app.get("/users/{user_id}")
async def get_user(user_id=None) -> User:
    with get_session() as session:
        print("get database session")
        q = session.query(User).filter(User.id == user_id).one()
        if q is not None:
            return q
        
    user = User()
    return user  

