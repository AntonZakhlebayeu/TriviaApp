from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_URI: str
    CLIENT_ID: str
    KAFKA_URI: str
    ORIGINS: str
    ALLOW_CREDENTIALS: bool
    ALLOW_METHODS: str
    ALLOW_HEADERS: str
    GROUP_ID: int
    KAFKA_CHANNEL: str

    class Config:
        env_file = ".env"


settings = Settings()
