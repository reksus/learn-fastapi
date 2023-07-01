from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "localhost"

    class Config:
        env_file = ".env"

settings = Settings()