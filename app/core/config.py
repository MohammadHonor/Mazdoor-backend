# app/core/config.py
from dotenv import load_dotenv
from pydantic_settings import BaseSettings , SettingsConfigDict
from pydantic import PostgresDsn
from pydantic import field_validator
from functools import lru_cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = True ,
        extra = "ignore"
    )

    PROJECT_NAME: str = "Mazdoor API"
    ENVIRONMENT: str = "development"

    #database
    DATABASE_URL: PostgresDsn
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DEBUG: bool = True

    #Auth
    JWT_SECRET_KEY:str
    JWT_ALGORITHM :str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES :int = 15
    REFRESH_TOKEN_EXPIRE_DAYS : int = 7

    #cors
    CORS: list[str] = ["*"]

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_env(cls, value:str)->str:
        allowed_envs = ["development", "production", "staging"]
        if value not in allowed_envs:
            raise ValueError(f"Invalid environment: {value}. Allowed values are: {allowed_envs}")
        return value

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()


