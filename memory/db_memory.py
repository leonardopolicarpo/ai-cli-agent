from .mongodb import get_collection
from datetime import datetime

def save_interaction(*, agent, prompt, response, session_id=None, tags=None):
  collection = get_collection()

  doc = {
    "agent": agent,
    "prompt": prompt,
    "response": response,
    "timestamp": datetime.now(),
    "session_id": session_id,
    "tags": tags or []
  }

  collection.insert_one(doc)

def load_context(project=None, session_id=None, limit=5):
  collection = get_collection()
  query = {}
  if session_id:
    query["session_id"] = session_id
  if project:
    query["project"] = project

  results = collection.find(query).sort("timestamp", -1).limit(limit)
  return list(results)[::-1]
