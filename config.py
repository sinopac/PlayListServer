import os


class Settings:
    PROJECT_NAME:str = "PlayList API"
    PROJECT_VERSION:str = "0.0.0.1"

    POSTGRES_USER:str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD:str = os.getenv("POSTGRES_PASSWORD", "password1!")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT:str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB:str = os.getenv("POSTGRES_DB", "playlist_db")
    DATABASE_URL:str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}" 

    JWT_SECRET_KEY:str = os.getenv("JWT_SECRET_KEY", "add18deb106c45caa01dc00a853c38aa")

settings = Settings