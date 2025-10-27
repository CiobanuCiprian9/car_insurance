from typing import List,Annotated

from fastapi import APIRouter,Depends
from sqlalchemy import  select
from sqlalchemy.orm import Session, joinedload
from app.models import Car
from app.repositories.database import get_db
from app.schemas import CarOut

router=APIRouter()

@router.get("/",response_model=List[CarOut])
def get_cars(db:Annotated[Session,Depends(get_db)]):
    cars=select(Car).options(joinedload(Car.owner))
    result=db.scalars(cars).all()
    return result
