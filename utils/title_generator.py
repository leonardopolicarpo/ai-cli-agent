from agents.gemini_agent import generate_response_gemini

MAX_TITLE_LENGTH = 40

def generate_title_from_conversartion(prompt: str, response: str) -> str:
  instruction = (
    "Gere um título curto e descritivo (máximo 40 caracteres) para esta conversa.\n"
    "Seja direto, sem pontuação final. Não inclua 'conversa sobre' ou similares.\n"
    "Usuário: {}\nIA: {}\nTítulo:".format(prompt, response)
  )

  raw_title = generate_response_gemini(instruction)

  title = raw_title.strip().replace("\n", "")[:MAX_TITLE_LENGTH]

  return title