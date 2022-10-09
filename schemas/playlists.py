from pydantic import BaseModel

class PlaylistSchema(BaseModel):
    title: str 
    decription: str | None = None
