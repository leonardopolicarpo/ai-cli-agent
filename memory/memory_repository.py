from datetime import datetime
from .mongodb import get_collection
from datetime import datetime

INTERACTIONS_COLLECTION = "interactions"
SESSIONS_COLLECTION = "sessions"

def save_interaction(agent, prompt, response, session_id, project_id=None, discipline=None, tags=None):
  collection = get_collection(INTERACTIONS_COLLECTION)
  doc = {
    "agent": agent,
    "prompt": prompt,
    "response": response,
    "timestamp": datetime.now(),
    "session_id": session_id,
    "project_id": project_id,
    "discipline": discipline,
    "tags": tags or []
  }
  collection.insert_one(doc)

  session_collection = get_collection(SESSIONS_COLLECTION)
  session_collection.update_one(
    {"session_id": session_id},
    {
      "$set": {"last_interaction": datetime.now()},
      "$setOnInsert": {"created_at": datetime.now()}
    },
    upsert=True
  )

def load_context(session_id: str, limit: int = 10):
  collection = get_collection(INTERACTIONS_COLLECTION)
  history = list(collection.find(
    {"session_id": session_id}
  ).sort("timestamp", -1).limit(limit))
  return list(reversed(history))

def update_session_title(session_id: str, title: str):
  collection = get_collection(SESSIONS_COLLECTION)
  collection.update_one(
    {"session_id": session_id},
    {"$set": {"title": title}}
  )

def update_session_last_used(session_id: str):
  collection = get_collection(SESSIONS_COLLECTION)
  collection.update_one(
    {"session_id": session_id},
    {"$set": {"last_interaction": datetime.now()}},
    upsert=True 
  )

def is_first_interaction(session_id: str) -> bool:
  collection = get_collection(INTERACTIONS_COLLECTION)
  return collection.count_documents({"session_id": session_id}) == 0

def ensure_session_exists(session_id: str, title: str = None):
  collection = get_collection(SESSIONS_COLLECTION)
  doc = {
    "session_id": session_id,
    "created_at": datetime.now(),
    "last_interaction": datetime.now()
  }
  if title:
    doc["title"] = title

  collection.update_one(
    {"session_id": session_id},
    {"$setOnInsert": doc},
    upsert=True
  )

