import os
from utils.session_utils import generate_session_id

SESSIONS_DIR = "sessions"

def ensure_sessions_dir():
  if not os.path.exists(SESSIONS_DIR):
    os.makedirs(SESSIONS_DIR)

def create_new_session(project="default"):
  ensure_sessions_dir()
  session_id = generate_session_id(project)
  with open(os.path.join(SESSIONS_DIR, f"{session_id}.txt"), "w") as f:
    f.write("")
  print(f"Sessão criada: {session_id}")
  return session_id

def list_sessions():
  ensure_sessions_dir()
  sessions = os.listdir(SESSIONS_DIR)
  return [s.replace(".txt", "") for s in sessions if s.endswith(".txt")]

def select_session():
  sessions = list_sessions()
  if not sessions:
    print("Nenhuma sessão existente.")
    return create_new_session()

  print("Sessões disponíveis:")
  for i, s in enumerate(sessions):
    print(f"{i + 1}. {s}")
  
  choice = input("Selecione o número da sessão ou digite 'n' para nova: ")
  if choice.lower() == "n":
    return create_new_session()
  try:
    return sessions[int(choice) - 1]
  except:
    print("Escolha inválida.")
    return select_session()
