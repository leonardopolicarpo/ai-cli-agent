import os
from datetime import datetime

MEMORY_DIR = "memory_logs"
MEMORY_FILE = os.path.join(MEMORY_DIR, "interactions.txt")

if not os.path.exists(MEMORY_DIR):
  os.makedirs(MEMORY_DIR)

def save_interaction(agent: str, prompt: str, response: str) -> None:
  with open(MEMORY_FILE, "a", encoding="utf-8") as f:
    f.write(f"=== Interação ===\n")
    f.write(f"Agent: {agent}\n")
    f.write(f"Prompt: {prompt}\n")
    f.write(f"Response: {response}\n")
    f.write(f"Timestamp: {datetime.now()}\n\n")

def load_memory() -> list[dict]:
  if not os.path.exists(MEMORY_FILE):
    return []
  with open(MEMORY_FILE, "r", encoding="utf-8") as f:
    content = f.read()

  interactions = []
  blocks = content.strip().split("=== Interação ===")
  for block in blocks:
    block = block.strip()
    if not block:
      continue
    lines = block.split("\n")
    data = {}
    for line in lines:
      if line.startswith("Agent: "):
        data["agent"] = line[len("Agent: "):]
      elif line.startswith("Prompt: "):
        data["prompt"] = line[len("Prompt: "):]
      elif line.startswith("Response: "):
        data["response"] = line[len("Response: "):]
      elif line.startswith("Timestamp: "):
        data["timestamp"] = line[len("Timestamp: "):]
    if data:
      interactions.append(data)
  return interactions
