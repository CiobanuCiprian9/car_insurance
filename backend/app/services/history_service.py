from typing import List, Dict, Any

from sqlalchemy import select

from app.models import InsurancePolicy, Claim
from app.services.car_service import CarService


class HistoryService:
    @staticmethod
    def get_history(db,car_id):
        CarService.check_car_exists(car_id,db)

        policies=db.execute(
            select(
                InsurancePolicy.id,
                InsurancePolicy.start_date,
                InsurancePolicy.end_date,
                InsurancePolicy.provider
            ).where(InsurancePolicy.car_id==car_id)
        ).mappings().all()

        claims=db.execute(
            select(
                Claim.id,
                Claim.claim_date,
                Claim.amount,
                Claim.description
            ).where(Claim.car_id==car_id)
        ).mappings().all()

        items: List[Dict[str,Any]] =[]

        for p in policies:
            items.append({"type": "POLICY", **p, "_sort": p["start_date"]})
        for c in claims:
            items.append({"type": "CLAIM", **c, "_sort": c["claim_date"]})

        items.sort(key=lambda x: x["_sort"])
        for it in items:
            it.pop("_sort", None)
        return items