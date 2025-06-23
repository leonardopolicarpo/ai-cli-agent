from agents.gemini_agent import generate_response_gemini
from memory import memory_repository as history_manager
from utils.context_string import build_prompt_with_context

def run_agent(agent_name: str, prompt: str, session_id: str) -> str:
  if agent_name == "gemini":
    memory = history_manager.load_context(session_id=session_id)
    context = memory[-5:] if len(memory) >= 5 else memory
    full_prompt = build_prompt_with_context(prompt, context)

    response = generate_response_gemini(full_prompt)

    history_manager.save_interaction(agent=agent_name, prompt=prompt, response=response, session_id=session_id)
    return response
  else:
    return "Agente não implementado."
