from pydantic import BaseModel, ConfigDict


class BirdhouseRunBase(BaseModel):
    account_id: int
    bird_nests: int


class BirdhouseRunCreate(BirdhouseRunBase):
    pass


class BirdhouseRunResponse(BirdhouseRunBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
