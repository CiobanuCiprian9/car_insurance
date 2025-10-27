from datetime import date as Date
from sqlalchemy import select
from app import exceptions
from app.models import Car, InsurancePolicy
from app.services.car_service import CarService

class CheckInsuranceValidity:
    @staticmethod
    def is_insurance_valid(car_id,date_str,db):
        try:
            d=Date.fromisoformat(date_str)
        except:
            raise exceptions.InvalidDateFormat()

        if d.year<1900 or d.year>2100:
            raise exceptions.DateOutOfRange()

        CarService.check_car_exists(car_id,db)

        active=db.execute(
            select(InsurancePolicy.id).where(
    InsurancePolicy.car_id==car_id,
                InsurancePolicy.start_date <=d,
                InsurancePolicy.end_date >=d
            ).limit(1)
        ).first() is not None

        return d,active