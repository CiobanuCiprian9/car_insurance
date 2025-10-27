from typing import Annotated
from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from app.exceptions import ServiceError
from app.repositories.database import get_db
from app.schemas import InsuranceValidityOut
from app.services.validity_service import CheckInsuranceValidity

router=APIRouter()

@router.get("/{carId}/insurance-valid",response_model=InsuranceValidityOut)
def get_insurance(
        carId: Annotated[int, Path(gt=0)],
        date_str: Annotated[str, Query(alias="date", description="YYYY-MM-DD")],
        db: Annotated[Session, Depends(get_db)],
    ):

    try:
        d,is_valid=CheckInsuranceValidity.is_insurance_valid(carId,date_str,db)
    except ServiceError as e:
        raise e
    except Exception as e:
        raise Exception(e)

    return InsuranceValidityOut(car_id=carId,date=d,valid=is_valid)
