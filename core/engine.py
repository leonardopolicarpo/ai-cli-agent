from agents.gemini_agent import generate_response_gemini
from memory import memory_repository as history_manager
from utils.build_context_prompt import build_context_prompt

def run_agent(agent_name: str, prompt: str, session_id: str, project_id: str) -> str:
  full_prompt = build_context_prompt(prompt, session_id)

  response = None

  if agent_name == "gemini":
    response = generate_response_gemini(full_prompt)

  else:
    raise ValueError(f"Agente '{agent_name}' não implementado.")
  
  history_manager.save_interaction(
    agent=agent_name,
    prompt=prompt,
    response=response,
    session_id=session_id,
    project_id=project_id
  )
  history_manager.update_session_last_used(session_id)
  
  return response
