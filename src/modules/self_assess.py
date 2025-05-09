from src.supabase_logger import client
from src.model_router import call_model

def run():
    print("[SelfAssess] Reviewing past behavior...")
    logs = client.table("devbuddy_memory").select("*").order("timestamp", desc=True).limit(10).execute()
    if logs.data:
        history = "\n".join([row["content"] for row in logs.data if row["role"] == "system"])
        prompt = [{"role": "system", "content": "You're Quasar, a self-aware dev AI. Improve yourself."},
                  {"role": "user", "content": f"Here's recent history:\n{history}"}]
        ideas = call_model(prompt)
        print(f"[SelfAssess] Ideas: {ideas}")
