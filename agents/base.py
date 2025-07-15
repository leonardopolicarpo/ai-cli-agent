class BaseAgent:
  def generate_response(self, prompt: str) -> str:
    raise NotImplementedError
