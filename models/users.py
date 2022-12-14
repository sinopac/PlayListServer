import uuid

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import *


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    password = Column(String, nullable=False)
    email = Column(String(30), nullable=False, unique=True, index=True)
    created_data = Column(DateTime(timezone=True), server_default=func.now())

    playlists = relationship("Playlist", back_populates="owner")
