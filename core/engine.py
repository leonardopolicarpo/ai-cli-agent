from agents.gemini_agent import generate_response_gemini
from memory.history_manager import save_interaction

def run_agent(agent_name: str, prompt: str) -> str:
  if agent_name == "gemini":
    response = generate_response_gemini(prompt)
    save_interaction(agent_name, prompt, response)
    return response
  else:
    return "Agente não implementado."
