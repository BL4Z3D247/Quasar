from src.supabase_logger import client
from src.model_router import call_model

def run():
    print("[Learn] Analyzing logs to learn...")
    logs = client.table("devbuddy_memory").select("*").order("timestamp", desc=True).limit(5).execute()
    lines = "\n".join([row["content"] for row in logs.data])
    insights = call_model([{"role": "system", "content": "You're Quasar, improve from experience."},
                           {"role": "user", "content": lines}])
    print(f"[Learn] Insight: {insights}")
