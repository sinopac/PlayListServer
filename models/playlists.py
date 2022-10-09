import uuid

from sqlalchemy import Table, Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from .base import *

association_table = Table(
    "track_associations",
    Base.metadata,
    Column("playlist_id", UUID, ForeignKey("playlists.id"), primary_key=True),
    Column("track_id", UUID, ForeignKey("tracks.id"), primary_key=True)
)


class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    decription = Column(String, index=True)
    owner_id = Column(UUID, ForeignKey("users.id"))
    created_data = Column(DateTime(timezone=True), server_default=func.now())
    
    owner = relationship("User", back_populates="playlists")
    tracks = relationship("Track", secondary=association_table)


class Track(Base):
    __tablename__ = "tracks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(30))
    album = Column(String(30))
    artist = Column(String(30))
    composer = Column(String(30))
    genre = Column(String(30))
    year = Column(String(30))
    audio_metadata = Column(JSONB())
    url = Column(String(30))
    cover_url = Column(String(30))
    created_data = Column(DateTime(timezone=True), server_default=func.now())    
