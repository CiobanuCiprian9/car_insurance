from sqlalchemy import Text
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .base import Base

class Owner(Base):
    __tablename__ = "owner"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str | None] = mapped_column(Text)

    cars: Mapped[list["Car"]] = relationship(back_populates="owner")

