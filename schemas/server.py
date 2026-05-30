from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ServerBase(BaseModel):
    hostname: str = Field(min_length=1, max_length=50)
    active: bool


class ServerCreate(ServerBase):
    created_at: datetime | None = None


class ServerResponse(ServerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ServerPatch(ServerBase):
    pass
