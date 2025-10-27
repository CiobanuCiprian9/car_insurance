from typing import Annotated, List
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from app.exceptions import ServiceError
from app.repositories.database import get_db
from app.schemas import ClaimOut
from app.services.claim_service import ClaimService

router=APIRouter()

@router.get("/{carId}/claims",response_model=List[ClaimOut])
def get_claim(
        carId: Annotated[int,Path(gt=0)],
        db:Annotated[Session,Depends(get_db)],
    ):

    try:
        claims=ClaimService.get_claim(carId,db)
    except ServiceError as e:
        raise e
    except Exception as e:
        raise Exception(e)

    return claims

@router.get("/{carId}/claims/{claim_id}",response_model=ClaimOut)
def get_one_claim(
        carId: Annotated[int,Path(gt=0)],
        db:Annotated[Session,Depends(get_db)],
        claim_id: Annotated[int,Path(gt=0)]
    ):

    try:
        claims=ClaimService.get_one_claim(carId,db,claim_id)
    except ServiceError as e:
        raise e
    except Exception as e:
        raise Exception(e)

    return claims