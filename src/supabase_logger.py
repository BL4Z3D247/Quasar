import os
from dotenv import load_dotenv
from supabase import create_client

# load .env in project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Please set SUPABASE_URL and SUPABASE_KEY in your .env")

client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_to_supabase(command: str, output: str):
    """Insert a log entry into Supabase."""
    client.table("quasar_logs") \
          .insert({ "command": command, "output": output }) \
          .execute()

def fetch_logs(limit: int = 10):
    """Fetch the last `limit` log entries (newest first)."""
    resp = client.table("quasar_logs") \
                 .select("*") \
                 .order("timestamp", desc=True) \
                 .limit(limit) \
                 .execute()
    return resp.data or []

def get_client():
    return client

