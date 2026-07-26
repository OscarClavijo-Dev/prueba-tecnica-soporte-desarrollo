from sqlalchemy import create_engine

from app.config import settings


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.postgres_user}:{settings.postgres_password}"
    f"@{settings.postgres_host}:{settings.postgres_port}"
    f"/{settings.postgres_db}"
)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)