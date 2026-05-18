from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.repositories import create_job
from app.db.session import get_db
from app.schemas import JobCreate

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("")
def add_job(payload: JobCreate, db: Session = Depends(get_db)):
    job = create_job(db, payload.target_url)
    return {"id": job.id, "status": job.status, "target_url": job.target_url}
