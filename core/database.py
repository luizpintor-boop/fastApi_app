import os
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:123user@localhost:5432/my_api_flutter"
)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session