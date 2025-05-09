import os
import subprocess
import time
from pathlib import Path

WATCH_PATH = Path("~/projects/auto-dev/projects").expanduser()
CHECK_INTERVAL = 30  # seconds

def git_has_changes():
    result = subprocess.run(["git", "status", "--porcelain"], cwd=WATCH_PATH.parent, stdout=subprocess.PIPE)
    return bool(result.stdout.strip())

def git_push_changes():
    subprocess.run(["python3", "quasar.py", "run", "log_commit"])
    subprocess.run(["git", "add", "."], cwd=WATCH_PATH.parent)
    subprocess.run(["git", "commit", "-m", "Auto-sync: changes detected by Scope"], cwd=WATCH_PATH.parent)
    subprocess.run(["git", "push"], cwd=WATCH_PATH.parent)

def main():
    print(f"[Scope] Watching ▶ {WATCH_PATH}")
    while True:
        if git_has_changes():
            print("[Scope] Detected change — syncing to GitHub")
            git_push_changes()
    subprocess.run(["python3", "quasar.py", "run", "log_commit"])
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
