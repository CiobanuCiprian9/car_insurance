from sqlalchemy import String,Text,Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .base import Base

class Car(Base):
    __tablename__ = "car"

    id: Mapped[int]=mapped_column(primary_key=True)
    vin: Mapped[str]=mapped_column(String(32),index=True,nullable=False,unique=True)
    make: Mapped[str]=mapped_column(String(32),nullable=True)
    model: Mapped[str | None] = mapped_column(Text)
    year_of_manufacture: Mapped[int | None] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey("dbo.owner.id"), nullable=False)

    owner: Mapped["Owner"] = relationship(back_populates="cars")
    policies: Mapped[list["InsurancePolicy"]] = relationship(back_populates="car")
    claims: Mapped[list["Claim"]] = relationship(back_populates="car")