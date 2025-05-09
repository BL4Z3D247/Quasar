import sys
from datetime import datetime
from src.supabase_logger import get_client  # You will add this helper if it's not already defined

def observe(content: str, role: str = "user", tag: str = None):
    client = get_client()
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "role": role,
        "content": content,
        "tag": tag
    }
    try:
        client.table("quasar_chatlog").insert(log_entry).execute()
        print("✅ Observation logged to Supabase.")
    except Exception as e:
        print(f"❌ Failed to log observation: {e}")
