from pydantic import BaseModel

class MessageCreate(BaseModel):
    message: str

class ChatResponse(BaseModel):
    id: int
    message: str
    role: str

