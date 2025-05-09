import os
from src.supabase_logger import client
import json

def export_logs(filename="log_export.json", limit=100):
    response = client.table("quasar_logs").select("*").order("timestamp", desc=True).limit(limit).execute()
    with open(filename, "w") as f:
        json.dump(response.data, f, indent=2)
    print(f"✅ Logs exported to {filename}")
