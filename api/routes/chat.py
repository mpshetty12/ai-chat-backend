from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.chat import MessageCreate
from db.session import get_db

from services.chat_service import (
    save_message,
    get_message
)

router = APIRouter()

@router.post("/message")
def send_message(user_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    save_message(db, user_id, msg.message, "user")
    return {"status": "saved"}

@router.get("/history")
def history(user_id: int, db: Session = Depends(get_db)):
    return get_message(db, user_id)

