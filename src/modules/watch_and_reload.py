import os
import subprocess
import time
from pathlib import Path

WATCH_DIR = Path("~/projects/auto-dev").expanduser()
LAST_HASH = None

def get_git_head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WATCH_DIR).decode().strip()

def reload_quasar():
    print("🔄 Code changed — restarting Quasar...")
    subprocess.run(["pm2", "restart", "quasar"], cwd=WATCH_DIR)

def main():
    global LAST_HASH
    print("[Watcher] Monitoring Quasar core for changes...")
    LAST_HASH = get_git_head()
    while True:
        current = get_git_head()
        if current != LAST_HASH:
            reload_quasar()
            LAST_HASH = current
        time.sleep(10)

if __name__ == "__main__":
    main()
