from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

client = create_client(SUPABASE_URL, SUPABASE_KEY)

def backup_log(command: str, output: str):
    try:
        client.table("logs").insert({"command": command, "output": output}).execute()
        print("☁️  Log backed up to Supabase")
    except Exception as e:
        print("❌ Failed to backup log:", e)
