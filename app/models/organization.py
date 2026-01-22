from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Table, Column
from app.core.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.building import Building
    from app.models.activity import Activity


organization_activity = Table(
    "organization_activity",
    Base.metadata,
    Column("organization_id", ForeignKey("organizations.id")),
    Column("activity_id", ForeignKey("activities.id")),
)


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"))

    building: Mapped["Building"] = relationship("Building")
    activities: Mapped[list["Activity"]] = relationship(
        "Activity", secondary=organization_activity, backref="organizations"
    )
    phone_numbers: Mapped[list["PhoneNumber"]] = relationship(
        "PhoneNumber", backref="organization"
    )


class PhoneNumber(Base):
    __tablename__ = "phone_numbers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    number: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
