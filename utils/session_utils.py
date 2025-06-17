from datetime import datetime
import uuid

def generate_session_id(project="default"):
  timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
  unique_id = uuid.uuid4().hex[:6]
  return f"{project}-{timestamp}-{unique_id}"
