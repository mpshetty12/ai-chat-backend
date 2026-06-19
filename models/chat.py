from sqlalchemy import Column, Integer, String, ForeignKey, Text
from db.base import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    
    # user_id = Column(Integer, ForeignKey("users.id"))
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))

    message = Column(Text)
    role = Column(String)
