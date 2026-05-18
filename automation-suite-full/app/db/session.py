from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def get_database_url() -> str:
    return settings.postgres_url if settings.use_postgres else settings.database_url


engine = create_engine(get_database_url(), future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
