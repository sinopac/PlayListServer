import os
from dotenv import load_dotenv

load_dotenv('.env')

class Settings:
    PROJECT_NAME:str = "PlayList API"
    PROJECT_VERSION:str = "0.0.0.1"

    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT:str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB:str = os.getenv("POSTGRES_DB")
    DATABASE_URL:str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}" 

    JWT_SECRET_KEY:str = os.getenv("JWT_SECRET_KEY")

settings = Settings