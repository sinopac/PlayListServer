import uuid
from typing import List
from jose import jwt
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from models import Playlist
from schemas import PlaylistSchema 
from database import get_session
from config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")
playlists_route = APIRouter()


@playlists_route.get("/playlists")
async def get_playlists(token: str = Depends(oauth2_scheme)) -> List[Playlist]:
    with get_session() as session:
        q = session.query(Playlist).all()
        if q is not None:
            return q
    return []


@playlists_route.get("/playlists/{playlist_id}")
async def get_playlist(token: str = Depends(oauth2_scheme), playlist_id=None) -> Playlist:
    with get_session() as session:
        q = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if q is not None:
            return q
    return Playlist()


@playlists_route.post("/playlists")
async def create_playlist(playlist: PlaylistSchema, token: str = Depends(oauth2_scheme)) -> Playlist:
    my_token = jwt.decode(token=token, key=settings.JWT_SECRET_KEY)
    new_playlist = Playlist(
        title = playlist.title,
        decription = playlist.decription,
        owner_id = uuid.UUID(my_token['sub']).hex)

    with get_session() as session:
        session.begin()
        try:
            session.add(new_playlist)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            session.refresh(new_playlist)
            return new_playlist
