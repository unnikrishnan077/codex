from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.repositories import create_record, list_records
from app.db.session import get_db
from app.schemas import RecordCreate

router = APIRouter(prefix="/records", tags=["records"])


@router.post("")
def add_record(payload: RecordCreate, db: Session = Depends(get_db)):
    rec = create_record(db, payload.title, payload.content)
    return {"id": rec.id, "title": rec.title, "content": rec.content}


@router.get("")
def get_records(db: Session = Depends(get_db)):
    rows = list_records(db)
    return [{"id": r.id, "title": r.title, "content": r.content} for r in rows]
