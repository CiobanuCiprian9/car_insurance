from typing import List,Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy import  select
from sqlalchemy.orm import Session, joinedload
from app.repositories.database import get_db
from app.schemas import CarOut, HistoryItem
from app.services.history_service import HistoryService

router=APIRouter()

@router.get("/{carId}/history",response_model=List[HistoryItem])
def get_history(
        db:Annotated[Session,Depends(get_db)],
        carId: Annotated[int, Path(gt=0)],
    ):

    return HistoryService.get_history(db,carId)
