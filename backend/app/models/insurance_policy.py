from sqlalchemy import ForeignKey, Text, DateTime,Date, Index
from datetime import date,datetime
from sqlalchemy.orm import relationship,mapped_column,Mapped
from .base import Base

class InsurancePolicy(Base):
    __tablename__ = "insurance_policy"

    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("dbo.car.id"), nullable=False)
    provider: Mapped[str | None] = mapped_column(Text)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    logged_expiry_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    car: Mapped["Car"] = relationship(back_populates="policies")

    __table_args__ = (Index("ix_policy_car_dates", "car_id", "start_date", "end_date"),)
