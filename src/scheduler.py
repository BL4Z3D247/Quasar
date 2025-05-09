import json, os, time
from datetime import datetime
from src.module_loader import run_module

SCHEDULE_FILE = os.path.expanduser("~/projects/auto-dev/.quasar_schedule.json")

def load_schedule():
    if not os.path.exists(SCHEDULE_FILE):
        return []
    with open(SCHEDULE_FILE) as f:
        return json.load(f)

def save_schedule(schedule):
    with open(SCHEDULE_FILE, "w") as f:
        json.dump(schedule, f, indent=2)

def add_schedule(task, when):
    schedule = load_schedule()
    schedule.append({"task": task, "when": when})
    save_schedule(schedule)
    print(f"✅ Scheduled {task} for {when}")

def run_due_tasks():
    now = datetime.now().strftime("%H:%M")
    schedule = load_schedule()
    new_schedule = []
    for entry in schedule:
        if entry["when"] == now:
            print(f"⏰ Running scheduled task: {entry['task']}")
            run_module(entry["task"])
        else:
            new_schedule.append(entry)
    save_schedule(new_schedule)
