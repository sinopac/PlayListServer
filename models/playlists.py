import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import *


class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    decription = Column(String, index=True)
    owner_id = Column(UUID, ForeignKey("users.id"))
    created_data = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="playlists")
