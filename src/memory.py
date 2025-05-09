import os
from datetime import datetime
from supabase import create_client
from dotenv import load_dotenv

# Load Supabase creds from .env
load_dotenv(dotenv_path=os.path.expanduser("~/projects/auto-dev/.env"))
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
client = create_client(SUPABASE_URL, SUPABASE_KEY)

def remember(prompt: str, response: str, command: str = None, output: str = None):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response,
        "command": command,
        "output": output
    }
    client.table("quasar_memory").insert(record).execute()

def recall(limit: int = 5):
    # Fetch all or many entries
    res = client.table("quasar_memory").select("*").execute()
    data = res.data or []
    # Sort by timestamp descending (ISO strings sort correctly)
    sorted_data = sorted(data, key=lambda rec: rec["timestamp"], reverse=True)
    # Return the top `limit`
    return sorted_data[:limit]
