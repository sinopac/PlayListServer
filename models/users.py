import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import *

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable = False)
    created_data = Column(DateTime(timezone = True), server_default = func.now())

    playlists = relationship("Playlist", back_populates = "owner")