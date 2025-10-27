from datetime import date, datetime
from decimal import Decimal
from typing import Optional, Literal, Union

from pydantic import BaseModel, EmailStr, Field, root_validator


class OwnerOut(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr] = None
    class Config:
        orm_mode=True

class CarOut(BaseModel):
    id: int
    vin: str
    make: str
    model: str
    yearOfManufacture: int = Field(alias="year_of_manufacture")
    owner: OwnerOut
    class Config:
        orm_mode=True

class InsurancePolicyOut(BaseModel):
    id: int
    carId: int = Field(alias="car_id")
    provider: Optional[str] = None
    startDate: date = Field(alias="start_date")
    endDate: date = Field(alias="end_date")
    loggedExpiryAt: Optional[datetime] = Field(alias="logged_expiry_at", default=None)
    class Config:
        orm_mode=True

class ClaimOut(BaseModel):
    claimDate: date = Field(alias="claim_date")
    description: str
    amount: Decimal
    class Config:
        orm_mode=True

class InsuranceValidityOut(BaseModel):
    carId: int = Field(alias="car_id")
    date: date
    valid: bool
    class Config:
        orm_mode=True

class InsurancePolicyCreate(BaseModel):
    provider: Optional[str] = None
    startDate: date
    endDate: date

    @root_validator
    def check_date(cls,values):
        start=values.get("startDate")
        end=values.get("endDate")
        if end is None:
            raise ValueError("endDate is required")
        if start and end and end<start:
            raise ValueError("endDate must be >= startDate")
        return values

class PolicyHistoryItem(BaseModel):
    type: Literal["POLICY"] = "POLICY"
    policyId: int = Field(alias="id")
    startDate: date =Field(alias="start_date")
    endDate: date=Field(alias="end_date")
    provider: Optional[str]=None
    class Config:
        orm_mode=True

class ClaimHistoryItem(BaseModel):
    type: Literal["CLAIM"] = "CLAIM"
    claimId: int = Field(alias="id")
    claimDate: date = Field(alias="claim_date")
    amount: Decimal
    description: str

    class Config:
        orm_mode = True

HistoryItem = Union[PolicyHistoryItem, ClaimHistoryItem]