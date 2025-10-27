from typing import Annotated
from app.repositories.database import get_db
from fastapi import APIRouter, Depends, Path, Response
from sqlalchemy.orm import Session
from app.schemas import InsurancePolicyOut, InsurancePolicyCreate
from app.services.policy_service import PolicyService

router=APIRouter()

@router.post("/{carId}/policies",response_model=InsurancePolicyOut)
def create_policies(
        carId: Annotated[int,Path(gt=0)],
        db:Annotated[Session,Depends(get_db)],
        payload: InsurancePolicyCreate,
        response: Response,
    ):

    policy=PolicyService.create_policy(db,carId,payload)
    response.headers["Location"] = f"/api/cars/{carId}/policies/{policy.id}"
    return policy