import os
from .mongodb import get_collection
from datetime import datetime
from memory import file_memory as memory

USE_MONGO = os.getenv("USE_MONGO", "false").lower() == "true"

def save_interaction(agent, prompt, response):
  if USE_MONGO:
    collection.insert_one({
      "agent": agent,
      "prompt": prompt,
      "response": response,
      "timestamp": datetime.now()
    })
  else:
    memory.save_interaction(agent, prompt, response)
