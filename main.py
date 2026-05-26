from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select, text
from sqlalchemy.orm import Session

import database.models as models
from database.database import Base, engine, get_db
from database.schemas import ServerCreate, ServerResponse

# from runelite_library.database import add_server

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello world!"}


@app.get(
    "/api/servers",
    response_model=list[ServerResponse],
)
def get_servers(db: Annotated[Session, Depends(get_db)]):
    return db.query(models.Servers).all()


@app.get("/api/servers/{server_id}")
def get_server_by_id(server_id: int):
    pass


@app.post(
    "/api/servers",
    response_model=ServerResponse,
)
def create_new_server(server: ServerCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.Servers).where(models.Servers.name == server.name),
    )

    existing_server = result.scalars().first()

    if existing_server:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Server already exists",
        )

    new_server = models.Servers(
        name=server.name,
        created_at=server.created_at,
        active=server.active,
    )

    db.add(new_server)
    db.commit()
    db.refresh(new_server)

    return new_server
