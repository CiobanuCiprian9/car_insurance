from sqlalchemy import select
from app.models import Car, Claim
from app import exceptions
from app.services.car_service import CarService

class ClaimService:
    @staticmethod
    def get_claim(car_id,db):
        CarService.check_car_exists(car_id,db)

        return db.execute(
            select(Claim).where(
                Claim.car_id==car_id
            ).order_by(Claim.claim_date.desc(), Claim.id.desc())
        ).scalars().all()

    @staticmethod
    def get_one_claim(car_id, db, claim_id):
        CarService.check_car_exists(car_id,db)

        claim=db.execute(
            select(Claim).where(
                Claim.car_id == car_id,
                Claim.id==claim_id
            ).limit(1)
        ).scalars().first()

        if claim is None:
            raise exceptions.ClaimNotFound()

        return claim