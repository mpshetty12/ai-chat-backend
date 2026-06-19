from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user import UserCreate, UserLogin
from db.session import get_db
from services import auth_service

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.create_user(db, user.email, user.password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = auth_service.authenticate_user(db, user.email, user.password)
    token = auth_service.generate_token(db_user)
    return {"access_token": token}

