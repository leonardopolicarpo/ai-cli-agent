from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
  session_id: str
  prompt: str
  project_id: Optional[str] = None

class ChatResponse(BaseModel):
  session_id: str
  ai_response: str
  tokens_used: int
