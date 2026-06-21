from fastapi import FastAPI
from api.routes import auth, chat, ml
from db.session import engine
from db.session import engine
from db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Chat Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(ml.router, prefix="/ml", tags=["ML"])

@app.get("/health")
def health():
    return {"status":"ok"} 