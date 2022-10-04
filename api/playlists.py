from typing import List
from fastapi import APIRouter
from database import get_session
from models import Playlist

playlists_route = APIRouter()


@playlists_route.get("/playlists")
async def get_playlists() -> List[Playlist]:
    with get_session() as session:
        q = session.query(Playlist)
        if q is not None:
            return q
    return []


@playlists_route.get("/playlists/{playlist_id}")
async def get_playlist(playlist_id=None) -> Playlist:
    with get_session() as session:
        q = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if q is not None:
            return q
    return Playlist()


@playlists_route.post("/playlists")
async def create_playlist():
    return Playlist()
