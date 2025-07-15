from memory.memory_repository import load_context
from utils.context_string import build_prompt_with_context

class MemoryEngine:
  def __init__(self, session_id: str, project_id: str):
    self.session_id = session_id
    self.project_id = project_id

  def get_short_term_memory(self, limit: int = 5) -> list[dict]:
    return load_context(self.session_id, limit=limit)

  def get_long_term_memory(self, query: str) -> list[dict]:
    # busca em embeddings
    # TODO: Implementar vector DB e buscar por similaridade
    return []

  def build_context(self, prompt: str) -> str:
    short_term = self.get_short_term_memory()
    long_term = self.get_long_term_memory(prompt)

    combined_memory = short_term + long_term
    
    return build_prompt_with_context(prompt, combined_memory)
