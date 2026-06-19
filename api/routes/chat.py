from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.chat import MessageCreate
from db.session import get_db

from services.chat_service import (
    save_message,
    get_message,
    create_session,
    get_session_messages
)

router = APIRouter()

# @router.post("/message")
# def send_message(user_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
#     save_message(db, user_id, msg.message, "user")
#     return {"status": "saved"}

# @router.get("/history")
# def history(user_id: int, db: Session = Depends(get_db)):
#     return get_message(db, user_id)


## security

from core.security import get_current_user
from models.user import User

@router.post("/message")
def send_message(session_id: int, msg: MessageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # save_message(db, current_user.id, msg.message, "user")
    # return {"status": "saved", "user":current_user.email}
    return save_message(db, session_id, msg.message, "user")

@router.get("/history")
def history(session_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_message(db, session_id)

## sessions
@router.post("/session")
def create_chat_session(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_session(db, current_user.id)

@router.get("/session/{session_id}")
def get_history(session_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_session_messages(db, session_id)