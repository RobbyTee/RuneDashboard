from pydantic import BaseModel, ConfigDict


class SkillLevels(BaseModel):
    attack_level: int | None = None
    strength_level: int | None = None
    defence_level: int | None = None
    ranged_level: int | None = None
    prayer_level: int | None = None
    agility_level: int | None = None
    construction_level: int | None = None
    cooking_level: int | None = None
    crafting_level: int | None = None
    farming_level: int | None = None
    firemaking_level: int | None = None
    fishing_level: int | None = None
    fletching_level: int | None = None
    herblore_level: int | None = None
    hunter_level: int | None = None
    magic_level: int | None = None
    mining_level: int | None = None
    runecraft_level: int | None = None
    sailing_level: int | None = None
    slayer_level: int | None = None
    smithing_level: int | None = None
    thieving_level: int | None = None
    woodcutting_level: int | None = None


class AccountBase(SkillLevels):
    account_name: str


class AccountResponse(AccountBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class AccountCreate(AccountBase):
    pass


class AccountPatch(AccountBase):
    account_name: str | None = None
