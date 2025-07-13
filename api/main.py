from fastapi import FastAPI
from .routers import chat

app = FastAPI(
  title="AI CLI Agent",
  description="Um hub central para interagir com diferentes modelos de IA com memória persistente.",
  version="0.1.0"
)

app.include_router(chat.router)

@app.get("/", tags=["Root"])
def read_root():
  return {"message": "Bem-vindo ao AI CLI Agent!"}
