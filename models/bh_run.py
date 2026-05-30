from datetime import UTC, datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


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
