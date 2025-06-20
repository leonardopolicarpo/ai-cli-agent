import os
from memory import file_memory
from memory import db_memory

USE_MONGO = os.getenv("USE_MONGO", "false").lower() == "true"

def save_interaction(*, agent, prompt, response, session_id=None, project=None, discipline=None, tags=None):
  if USE_MONGO:
    db_memory.save_interaction(agent, prompt, response, session_id, project, discipline, tags)
  else:
    file_memory.save_interaction(agent, prompt, response, project, discipline, tags)

def load_context(project=None, session_id=None, limit=5):
  if USE_MONGO:
    return db_memory.load_context(project, session_id, limit)
  else:
    return file_memory.load_memory()
