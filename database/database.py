import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

USERNAME = os.getenv("POSTGRES_USERNAME")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOSTNAME = os.getenv("POSTGRES_HOSTNAME")
DATABASE = os.getenv("POSTGRES_DATABASE")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db
