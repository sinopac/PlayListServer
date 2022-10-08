import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from .base import *

class Track(Base):
    __tablename__ = "tracks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(30))
    album = Column(String(20))
    artist = Column(String(20))
    composer = Column(String(30))
    genre = Column(String(30))
    year = Column(String(30))
    metadata = Column(JSONB())
    url = Column(String)

    created_data = Column(DateTime(timezone=True), server_default=func.now())

