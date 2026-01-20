from sqlalchemy.orm import Mapped, mapped_column
from app.core.base import Base


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(index=True)
    latitude: Mapped[float]
    longitude: Mapped[float]
