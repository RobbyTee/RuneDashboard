from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ServerBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class ServerCreate(ServerBase):
    created_at: datetime | None = None
    active: bool | None = None


class ServerResponse(ServerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    active: bool


class BirdhouseBase(BaseModel):
    pass
