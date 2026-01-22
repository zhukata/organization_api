from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/organization_api"
    API_KEY: str = "secret-key"
    API_KEY_NAME: str = "X-API-KEY"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
