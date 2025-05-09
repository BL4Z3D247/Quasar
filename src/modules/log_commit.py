from src.supabase_logger import get_client
import subprocess
from datetime import datetime

def run():
    client = get_client()
    try:
        commit = subprocess.check_output(["git", "log", "-1", "--pretty=%B"]).decode().strip()
        author = subprocess.check_output(["git", "log", "-1", "--pretty=%an"]).decode().strip()
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "role": "system",
            "content": f"Commit by {author}: {commit}",
            "tag": "commit"
        }
        client.table("quasar_chatlog").insert(log).execute()
        print("✅ Commit logged to Supabase memory.")
    except Exception as e:
        print(f"❌ Failed to log commit: {e}")
