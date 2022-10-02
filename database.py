from email.generator import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

CONNECTION_STRING = settings.DATABASE_URL
_engine = create_engine("postgresql://postgres:password1!@localhost/playlist_db")
_Sessionmaker= sessionmaker(bind=_engine, autocommit=False, autoflush=False)


def get_session() -> Generator:
    session = _Sessionmaker()
    return session
    