from utils.session_utils import generate_session_id
from datetime import datetime
from memory.mongodb import get_collection

def create_new_session():
  project = input("Projeto: ")
  discipline = input("Disciplina: ")
  session_id = generate_session_id(project)

  session = {
    "session_id": session_id,
    "project": project,
    "discipline": discipline,
    "created_at": datetime.now()
  }

  collection = get_collection("sessions")
  collection.insert_one(session)
  print(f"Sessão cirada: {session_id}")
  return session_id

def list_sessions():
  collection = get_collection("sessions")
  return list(collection.find())

def select_session():
  sessions = list_sessions()
  if not sessions:
    print("Nenhuma sessão existente.")
    return create_new_session()
  
  print("Sessões disponíveis:")
  for i, s in enumerate(sessions):
    print(f"{i + 1}. [{s.get('discipline')}] {s.get('project')} - {s.get('session_id')}")

  choice = input("Selecione o número da sessão ou digite 'n' para nova: ")
  if choice.lower() == 'n':
    return create_new_session()
  try:
    index = int(choice) - 1
    return sessions[index]["session_id"]
  except:
    print("Escolha inválida.")
    return select_session()