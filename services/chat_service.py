from sqlalchemy.orm import Session
from models.chat import ChatMessage
from  models.chat_session import ChatSession

from fastapi import HTTPException

# from cache.redis import redis_client
# import json

def save_message(db: Session, session_id: int, user_id: int, message: str, role: str):
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == user_id
    ).first()

    if not session:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    msg = ChatMessage(
        session_id=session_id,
        message=message,
        role=role
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    #clear old cache
    # redis_client.delete(f"chat_Sessin:{session_id}")

    return msg

def get_message(db: Session, user_id: int):
    return db.query(ChatMessage).filter(ChatMessage.user_id == user_id).all()

def create_session(db: Session, user_id: int):
    session = ChatSession(user_id = user_id)
    db.add(session)
    db.commit()
    db.refresh(session)

    return session

def get_session_messages(db: Session, session_id: int, user_id: int):
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == user_id
    ).first()

    if not session:
        raise HTTPException(status_code=403, detail="Access denied")

    messages = db.query(ChatMessage).filter(ChatMessage.session_id == session_id).all()

    return messages
    # cachey_key = f"chat_session:{session_id}"

    # #step 1 - check cache
    # cached_data = redis_client.get(cachey_key)

    # if cached_data:
    #     print("CACHE HIT")
    #     return json.loads(cached_data)
    
    # #step 2 - fetch from db
    # print("DB HIT")
    
    # messages = db.query(ChatMessage).filter(ChatMessage.session_id == session_id).all()
    # result = []

    # for msg in messages:
    #     result.append({
    #         "id" : msg.id,
    #         "role": msg.role,
    #         "message": msg.message
    #     })

    # #step 3 - store in redis
    # redis_client.set(
    #     cachey_key,
    #     json.dumps(result),
    #     ex=300
    # )

    # return result

