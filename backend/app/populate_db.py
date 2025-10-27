from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session

from app.session import SessionLocal
from app.models import Owner, Car, InsurancePolicy, Claim

def run():
    s: Session = SessionLocal()
    try:
        # Owners
        o1 = Owner(name="Ana Pop",   email="ana@example.com")
        o2 = Owner(name="Mihai Ion", email=None)
        s.add_all([o1, o2])
        s.flush()

        # Cars
        c1 = Car(vin="1A2B3C4D0000", make="VW",     model="Polo", year_of_manufacture=2017, owner_id=o1.id)
        c2 = Car(vin="1W2X3Y4Z0000", make="Renault", model="Clio", year_of_manufacture=2020, owner_id=o2.id)
        s.add_all([c1, c2])
        s.flush()

        # Policies (1 an)
        p1 = InsurancePolicy(car_id=c1.id, provider="Allianz",  start_date=date(2025, 1, 1), end_date=date(2026, 1, 1))
        p2 = InsurancePolicy(car_id=c2.id, provider="Groupama", start_date=date(2025, 6, 1), end_date=date(2026, 6, 1))
        s.add_all([p1, p2])
        s.flush()

        # Claims
        cl1 = Claim(car_id=c1.id, claim_date=date(2025, 3, 10), description="Broken window",  amount=Decimal("500.00"))
        cl2 = Claim(car_id=c2.id, claim_date=date(2025, 9,  1), description="Folded wing", amount=Decimal("1250.50"))
        s.add_all([cl1, cl2])

        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()

if __name__ == "__main__":
    run()
