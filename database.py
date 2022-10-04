from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

CONNECTION_STRING = settings.DATABASE_URL
_engine = create_engine("postgresql://postgres:password1!@localhost/playlist_db")
#_engine = create_engine(CONNECTION_STRING)
_Sessionmaker = sessionmaker(bind=_engine, autocommit=False, autoflush=False)


def get_session() -> sessionmaker:
    session = _Sessionmaker()
    return session
