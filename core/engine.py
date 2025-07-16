from agents.main import AGENT_REGISTRY
from memory import memory_repository as history_manager
from core.memory_engine.memory_engine import MemoryEngine

def run_agent(agent_name: str, prompt: str, session_id: str, project_id: str) -> str:
  agent = AGENT_REGISTRY.get(agent_name)
  if not agent:
    raise ValueError(f"Agente '{agent_name}' não implementado.")
  
  memory_engine = MemoryEngine(session_id, project_id)
  full_prompt = memory_engine.build_context(prompt)
  
  response = agent.generate_response(full_prompt)
  
  history_manager.save_interaction(
    agent=agent_name,
    prompt=prompt,
    response=response,
    session_id=session_id,
    project_id=project_id
  )
  history_manager.update_session_last_used(session_id)
  
  return response
