from fastapi import APIRouter

from api.schemas.chat import ChatRequest, ChatResponse 

from core.engine import run_agent

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def handle_chat(request: ChatRequest):
  agent_result = run_agent(
    'gemini',
    request.prompt,
    request.session_id,
    request.project_id
  )

  response = ChatResponse(
    session_id=request.session_id,
    ai_response=agent_result
  )
  
  return response