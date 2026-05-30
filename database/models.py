from datetime import UTC, datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Server(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    hostname: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )


class BirdhouseRun(Base):
    __tablename__ = "birdhouse_runs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False,
    )

    bird_nests: Mapped[int] = mapped_column(
        nullable=False,
    )

    timestamp: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        nullable=False,
    )

    account = relationship("Account", back_populates="birdhouse_runs")


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    account_name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    attack_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    strength_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    defence_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    ranged_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    prayer_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    agility_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    construction_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    cooking_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    crafting_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    farming_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    firemaking_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    fishing_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    fletching_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    herblore_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    hunter_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    magic_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    mining_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    runecraft_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    sailing_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    slayer_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    smithing_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    thieving_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    woodcutting_level: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    birdhouse_runs = relationship("BirdhouseRun", back_populates="account")
