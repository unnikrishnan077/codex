from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "automation-suite-full"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///./automation.db"
    postgres_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/automation"
    use_postgres: bool = False
    vector_index_path: str = "./faiss.index"
    vector_meta_path: str = "./faiss_meta.npy"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
