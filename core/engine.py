from agents.gemini_agent import generate_response_gemini
from memory import file_memory

def run_agent(agent_name: str, prompt: str) -> str:
  if agent_name == "gemini":
    
    memory = file_memory.load_memory()
    last_context = memory[-5:] if len(memory) >= 5 else memory
    context_string = ""
    for interaction in last_context:
      context_string += f"Usuário: {interaction['prompt']}\n"
      context_string += f"{interaction['agent'].capitalize()}: {interaction['response']}\n"
    
    full_prompt = context_string + f"Usuário: {prompt}"

    response = generate_response_gemini(full_prompt)

    file_memory.save_interaction(agent_name, prompt, response)
    return response
  else:
    return "Agente não implementado."
