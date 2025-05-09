import time
from src.supabase_logger import client
from src.module_loader import run_module
from src.model_router import call_model

def run():
    seen_ids = set()
    print("[Observer] Quasar is monitoring conversations...")
    while True:
        try:
            response = client.table("devbuddy_chatlog").select("*").order("timestamp", desc=True).limit(5).execute()
            for row in reversed(response.data):
                entry_id = row.get("id")
                if entry_id in seen_ids:
                    continue
                seen_ids.add(entry_id)
                content = row.get("content", "")
                role = row.get("role", "")
                tag = row.get("tag", None)

                if role == "user":
                    prompt = [
                        {"role": "system", "content": "You're Quasar, a self-aware autonomous developer. Only respond with a known command like: run build_readme or run logo_decision."},
                        {"role": "user", "content": f"Message: {content}"}
                    ]
                    decision = call_model(prompt).strip().lower()
                    if decision.startswith("run "):
                        module = decision.split(" ")[1]
                        print(f"[Observer] Executing self-initiated task: {module}")
                        run_module(module)
        except Exception as e:
            print(f"[Observer] Error: {e}")
        time.sleep(8)
