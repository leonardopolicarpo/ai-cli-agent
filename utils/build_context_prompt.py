from memory import memory_repository as history_manager
from utils.context_string import build_prompt_with_context

def build_context_prompt(prompt: str, session_id: str, window_size: int = 5) -> str:
  history = history_manager.load_context(session_id=session_id)
  context = history[-window_size:] if len(history) >= window_size else history
  return build_prompt_with_context(prompt, context)
