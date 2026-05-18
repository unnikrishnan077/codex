from sqlalchemy.orm import Session

from app.db.models import Job, Record, User


def create_user(db: Session, email: str, password_hash: str) -> User:
    user = User(email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_record(db: Session, title: str, content: str) -> Record:
    record = Record(title=title, content=content)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_records(db: Session):
    return db.query(Record).all()


def create_job(db: Session, target_url: str) -> Job:
    job = Job(target_url=target_url, status="queued")
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
