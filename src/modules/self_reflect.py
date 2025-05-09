from src.supabase_logger import get_client
from src.model_router import call_model

def run():
    client = get_client()
    logs = client.table("quasar_memory").select("*").order("timestamp", desc=True).limit(10).execute()
    reflection = call_model([
        {"role": "system", "content": "You are Quasar. Summarize what you’ve been working on and what you might do next."},
        {"role": "user", "content": str(logs.data)}
    ])
    print("[Reflection] " + reflection)
