#!/usr/bin/env python3
import os, sys

# ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.modules.scope import watch_changes, on_change

if __name__ == "__main__":
    print("[Scope Runner] Starting watcher…")
    watch_changes(on_change)
