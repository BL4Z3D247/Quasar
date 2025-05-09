import os, json, time
from src.scheduler import run_due_tasks
from src.module_loader import run_module

QUEUE_FILE = os.path.expanduser("~/projects/auto-dev/.quasar_queue.json")

def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE) as f:
        return json.load(f)

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def daemon_loop():
    print("🌀 Quasar Daemon running... Press Ctrl+C to stop.")
    while True:
        run_due_tasks()
        queue = load_queue()
        new_queue = []
        for item in queue:
            try:
                print(f"\n▶ Running queued task: {item}")
                run_module(item)
            except Exception as e:
                print(f"⚠️ Error running {item}: {e}")
                new_queue.append(item)  # Retry next loop
        save_queue(new_queue)
        time.sleep(60)
