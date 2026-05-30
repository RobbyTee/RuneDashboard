from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

USERNAME = settings.db_user
PASSWORD = settings.db_password
HOSTNAME = settings.db_host
DATABASE = settings.db_name
PORT = settings.db_port

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
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


def test_database_connection() -> bool:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("\nSuccessfully connected to the database!")
    except OperationalError as e:
        print("\n################################")
        print("################################")
        print(f"\nPlease fix the following error:\n\n{e}")
