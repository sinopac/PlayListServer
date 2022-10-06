from operator import imod
from fastapi import FastAPI
from api import playlists_route, users_route, auth_router
from config import settings

import uvicorn


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(playlists_route, prefix="/playlists", tags=["playlists"])
app.include_router(users_route, prefix="/users", tags=["users"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
