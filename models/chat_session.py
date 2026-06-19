from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy import func
from db.base import Base

class ChatSession(Base):
    __tablename__="chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())