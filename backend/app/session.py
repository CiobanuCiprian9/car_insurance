from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
from pathlib import Path
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(1, str(BACKEND_DIR))
load_dotenv(BACKEND_DIR / ".env")
db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()