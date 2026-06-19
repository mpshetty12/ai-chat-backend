from sqlalchemy.orm import Session
from models.chat import ChatMessage

def save_message(db: Session, user_id: int, message: str, role: str):
    msg = ChatMessage(user_id=user_id, message=message, role=role)
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return msg

def get_message(db: Session, user_id: int):
    return db.query(ChatMessage).filter(ChatMessage.user_id == user_id).all()
