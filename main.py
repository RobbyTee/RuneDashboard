from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models.account import Account
from models.bh_run import BirdhouseRun
from models.server import Server
from schemas.account import AccountCreate, AccountPatch, AccountResponse
from schemas.bh_run import BirdhouseRunCreate, BirdhouseRunResponse
from schemas.server import ServerCreate, ServerPatch, ServerResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# # # # # # #
# # HTML  # #
# # # # # # #


@app.get("/", include_in_schema=False)
def home():
    return {"message": "Hello world!"}


# # # # # # #
# #  API  # #
# # # # # # #


@app.get(
    "/api/servers",
    response_model=list[ServerResponse],
)
def get_servers(db: Annotated[Session, Depends(get_db)]):
    return db.query(Server).all()


@app.get("/api/servers/id/{server_id}")
def get_server_by_id(server_id: int, db: Annotated[Session, Depends(get_db)]):
    return db.query(Server).filter(Server.id == server_id)


@app.post(
    "/api/servers",
    response_model=ServerResponse,
)
def create_new_server(server: ServerCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.query(Server).filter(Server.hostname == server.hostname)

    existing_server = result.first()

    if existing_server:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Server already exists",
        )

    new_server = Server(
        hostname=server.hostname,
        created_at=server.created_at,
        active=server.active,
    )

    db.add(new_server)
    db.commit()
    db.refresh(new_server)

    return new_server


@app.patch(
    "/api/servers/id/{server_id}",
    response_model=ServerResponse,
)
def update_server_by_id(
    server_id: int,
    updates: ServerPatch,
    db: Annotated[Session, Depends(get_db)],
):
    server = db.query(Server).filter(Server.id == server_id).first()

    if not server:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Server ID {server_id} is not associated with a server.",
        )

    server_updates = updates.model_dump(exclude_unset=True)

    for field, value in server_updates.items():
        setattr(server, field, value)

    db.commit()
    db.refresh(server)

    return server


@app.get(
    "/api/accounts",
    response_model=list[AccountResponse],
)
def get_all_accounts(db: Annotated[Session, Depends(get_db)]):
    return db.query(Account).all()


@app.get(
    "/api/accounts/name/{account_name}",
    response_model=AccountResponse,
)
def get_account_info_by_name(
    account_name: str,
    db: Annotated[Session, Depends(get_db)],
):
    account = db.query(Account).filter(Account.account_name == account_name).first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No account found with name: {account_name}",
        )

    return account


@app.post(
    "/api/accounts",
    response_model=AccountResponse,
)
def create_account(
    account: AccountCreate,
    db: Annotated[Session, Depends(get_db)],
):
    result = db.query(Account).filter(Account.account_name == account.account_name)

    existing_account = result.first()

    if existing_account:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Account with name {account.account_name} already exists!",
        )

    new_account = Account(
        account_name=account.account_name,
        attack_level=account.attack_level,
        strength_level=account.strength_level,
        defence_level=account.defence_level,
        ranged_level=account.ranged_level,
        prayer_level=account.prayer_level,
        agility_level=account.agility_level,
        construction_level=account.construction_level,
        cooking_level=account.cooking_level,
        crafting_level=account.crafting_level,
        farming_level=account.farming_level,
        firemaking_level=account.firemaking_level,
        fishing_level=account.fishing_level,
        fletching_level=account.fletching_level,
        herblore_level=account.herblore_level,
        hunter_level=account.hunter_level,
        magic_level=account.magic_level,
        mining_level=account.mining_level,
        runecraft_level=account.runecraft_level,
        sailing_level=account.sailing_level,
        slayer_level=account.slayer_level,
        smithing_level=account.smithing_level,
        thieving_level=account.thieving_level,
        woodcutting_level=account.woodcutting_level,
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


@app.patch(
    "/api/accounts/id/{account_id}",
    response_model=AccountResponse,
)
def update_account_by_id(
    account_id: int,
    updates: AccountPatch,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    account = db.query(Account).filter(Account.id == account_id).first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account ID {account_id} is not associated with an account.",
        )

    update_data = updates.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(account, field, value)

    db.commit()
    db.refresh(account)

    return account


@app.delete("/api/accounts/id/{account_id}")
def delete_account_by_id(account_id, db: Annotated[Session, Depends(get_db)]):
    account = db.query(Account).filter(Account.id == account_id).first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account ID {account_id} is not associated with an account.",
        )

    db.delete(account)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get(
    "/api/runs",
    response_model=list[BirdhouseRunResponse],
)
def get_runs(db: Annotated[Session, Depends(get_db)]):
    return db.query(BirdhouseRun).all()


@app.get("/api/runs/account/{account_id}", response_model=list[BirdhouseRunResponse])
def get_runs_by_account_id(
    account_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    return db.query(BirdhouseRun).filter(BirdhouseRun.account_id == account_id).all()


@app.post("/api/runs", response_model=BirdhouseRunResponse)
def create_run(
    run: BirdhouseRunCreate,
    db: Annotated[Session, Depends(get_db)],
):
    new_run = BirdhouseRun(
        account_id=run.account_id,
        bird_nests=run.bird_nests,
    )

    db.add(new_run)
    db.commit()
    db.refresh(new_run)

    return new_run
