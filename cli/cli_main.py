from cli.cli_session import select_session
from core.engine import run_agent

def main():
  print("AI CLI Agent (CLI) - Digite 'sair' para encerrar.")
  session_id = select_session()
  print(f"Usando sessão: {session_id}")

  while True:
    prompt = input("Você: ")
    if prompt.lower() in ["sair", "exit", "quit"]:
      break
    response = run_agent("gemini", prompt, session_id)
    print(f"Gemini: {response}\n")
