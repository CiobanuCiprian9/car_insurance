from sqlalchemy import select

from app import exceptions
from app.models import Car


class CarService:
    @staticmethod
    def check_car_exists(car_id,db):
        car_exists = db.execute(
            select(Car.id).where(Car.id == car_id).limit(1)
        ).first()

        if not car_exists:
            raise exceptions.CarNotFound()