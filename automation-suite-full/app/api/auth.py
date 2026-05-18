from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import create_access_token, hash_password, verify_password
from app.db.repositories import create_user, get_user_by_email
from app.db.session import get_db
from app.schemas import LoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register(payload: LoginRequest, db: Session = Depends(get_db)):
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="email already exists")
    user = create_user(db, payload.email, hash_password(payload.password))
    return {"id": user.id, "email": user.email}


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="invalid credentials")
    return {"access_token": create_access_token(user.email), "token_type": "bearer"}
