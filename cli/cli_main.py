from core.engine import run_agent

def main():
  print("Hub Neurodigital (CLI) - Digite 'sair' para encerrar.")
  while True:
    prompt = input("Você: ")
    if prompt.lower() in ["sair", "exit", "quit"]:
      break
    response = run_agent("gemini", prompt)
    print(f"Gemini: {response}\n")

if __name__ == "__main__":
  main()
