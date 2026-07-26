from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str

    mariadb_database: str
    mariadb_user: str
    mariadb_password: str
    mariadb_root_password: str

    wordpress_db_host: str
    wordpress_db_name: str
    wordpress_db_user: str
    wordpress_db_password: str

    github_token: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()