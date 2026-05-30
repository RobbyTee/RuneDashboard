from datetime import UTC, datetime

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


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
