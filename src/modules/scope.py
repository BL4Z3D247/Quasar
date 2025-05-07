#!/usr/bin/env python3
import os, sys, subprocess, time

# ─────── PATH FIX ───────
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
# ─────────────────────────

from src.modules.lodestone import pull_changes

WATCH_DIR = os.path.expanduser("~/projects/auto-dev/projects")
IGNORE = {
    "scope-test", "smoke-test", "scout-alpha-test",
    "hello-world-demo", "hello-world-demo-final", "hello-world-demo2",
    "scout-v6", "scout-v8", "scout-v9", "scout-bot"
}

print(f"[Scope] Watching ▶ {WATCH_DIR}")
print("[Scope] Starting commit-hash watcher…")

def get_head_hash(repo_path):
    try:
        out = subprocess.check_output(
            ["git", "-C", repo_path, "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL
        )
        return out.strip().decode()
    except subprocess.CalledProcessError:
        return None

def watch_changes(callback, interval=2):
    last_seen = {}
    while True:
        for root, dirs, _ in os.walk(WATCH_DIR):
            name = os.path.basename(root)
            if name in IGNORE or ".git" not in dirs:
                continue
            head = get_head_hash(root)
            if head and last_seen.get(root) != head:
                last_seen[root] = head
                callback(root)
        time.sleep(interval)

def on_change(repo_path):
    print(f"[Scope] Detected new commit in repo: {repo_path}")
    pull_changes(repo_path)

if __name__ == "__main__":
    watch_changes(on_change)
