def build_prompt_with_context(prompt: str, memory: list[dict]) -> str:
  context_string = ""
  for interaction in memory:
    context_string += f"Usuário: {interaction['prompt']}\n"
    context_string += f"{interaction['agent'].capitalize()}: {interaction['response']}\n"

  context_string += f"Usuário: {prompt}"
  return context_string
