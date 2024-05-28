from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    GOOGLE_CLOUD_PROJECT: str
    PUBSUB_TOPIC: str
    OTEL_EXPORTER_OTLP_ENDPOINT: str
    GOOGLE_APPLICATION_CREDENTIALS: str

    class Config:
        env_file = ".env"

settings = Settings()
