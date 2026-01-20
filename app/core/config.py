from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/organization_api"
    API_KEY: str = "secret-key"
    API_KEY_NAME: str = "X-API-KEY"

    class Config:
        env_file = ".env"


settings = Settings()
