from sqlalchemy.orm import Session
from models.chat import ChatMessage
from  models.chat_session import ChatSession

def save_message(db: Session, session_id: int, message: str, role: str):
    msg = ChatMessage(session_id=session_id, message=message, role=role)
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return msg

def get_message(db: Session, user_id: int):
    return db.query(ChatMessage).filter(ChatMessage.user_id == user_id).all()

def create_session(db: Session, user_id: int):
    session = ChatSession(user_id = user_id)
    db.add(session)
    db.commit()
    db.refresh(session)

    return session

def get_session_messages(db: Session, session_id: int):
    return db.query(ChatMessage).filter(ChatMessage.session_id ==  session_id).all()

