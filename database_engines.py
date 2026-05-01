from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from cfg import settings


engine = create_engine(
    url=settings.DB_URL_psycopg,
    echo=True # чтобы видеть все логи 
)

async_engine = create_async_engine(
    url=settings.DB_URL_asyncpg,
    echo=True
)

session_factory = sessionmaker(engine)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    ...