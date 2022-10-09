from operator import imod
from fastapi import FastAPI
from api import playlists_route, users_route, auth_router
from config import settings

import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME, 
    version=settings.PROJECT_VERSION,
    description="A simple web service for music playlist with FastAPI", 
    contact={"name": "Alxe Huang", "email": "paojen.huang@gmail.com"})

app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(playlists_route, prefix="/api", tags=["playlists"])
app.include_router(users_route, prefix="/api", tags=["users"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
