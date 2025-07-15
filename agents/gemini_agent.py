from .base import BaseAgent
from google.generativeai import GenerativeModel

class GeminiAgent(BaseAgent):
  def __init__(self):
    self.model = GenerativeModel("gemini-2.5-flash-preview-04-17-thinking")
  
  def generate_response(self, prompt: str) -> str:
    response = self.model.generate_content(prompt)
    try:
      return response.candidates[0].content.parts[0].text.strip()
    except Exception as e:
      print(f"[ERRO GEMINI] ao extrair texto: {e}")
      return "[ERRO] Não foi possível gerar uma resposta."
