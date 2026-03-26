from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from cfg import settings


engine = create_engine(
    url=settings.DB_URL_psycopg,
    echo=True
)

session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    ...