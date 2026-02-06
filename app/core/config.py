# app/core/config.py
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Mazdoor-backend"
    DEBUG: bool = True
    MAZDOOR_DATABASE_URL: str
    JWT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()

