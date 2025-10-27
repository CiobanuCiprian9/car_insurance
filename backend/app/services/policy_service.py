from sqlalchemy import select
from zope.interface import provider

from app.models import InsurancePolicy
from app.services.car_service import CarService


class PolicyService:
    @staticmethod
    def create_policy(db,car_id,payload):
        CarService.check_car_exists(car_id, db)

        policy=InsurancePolicy(
            car_id=car_id,
            provider=payload.provider,
            start_date=payload.startDate,
            end_date=payload.endDate,
        )
        db.add(policy)
        db.flush()
        db.commit()
        db.refresh(policy)
        return policy