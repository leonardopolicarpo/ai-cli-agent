# api/routers/chat.py
from fastapi import APIRouter

# Importe seus schemas
from ..schemas.chat import ChatRequest, ChatResponse 

# Importe sua lógica de negócio!
# from memory.memory_manager import get_session_history # Exemplo
# from agents.deepseek_agent import query_deepseek      # Exemplo

# Cria um "roteador", como no Express
router = APIRouter(
    prefix="/chat",  # Todas as rotas aqui começarão com /chat
    tags=["Chat"]    # Agrupa as rotas na documentação automática
)

@router.post("/", response_model=ChatResponse)
def handle_chat(request: ChatRequest):
    # 1. A mágica do FastAPI: `request` já foi validado contra o schema ChatRequest.
    # Se o cliente enviar dados errados, o FastAPI retorna um erro 422 automaticamente.
    
    # 2. Chame sua lógica de negócio (que não sabe nada sobre HTTP)
    # history = get_session_history(request.session_id)
    context = f"{history}\nUser: {request.prompt}"
    
    # Supondo que sua função de agente retorne um dicionário
    # agent_result = query_deepseek(context, api_key="...") # Pegar a key do .env
    
    # 3. Formate a resposta usando o schema de resposta
    response = ChatResponse(
        session_id=request.session_id,
        ai_response=agent_result.get("text"),
        # tokens_used=agent_result.get("usage").get("total_tokens")
    )
    
    return response