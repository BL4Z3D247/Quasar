#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.supabase_logger import fetch_logs

def show_logs(limit: int = 10):
    """
    Fetch and pretty-print the last `limit` entries from Supabase.
    """
    entries = fetch_logs(limit=limit)
    print(f"=== Last {limit} Quasar logs ===")
    for e in entries:
        ts = e["timestamp"]
        cmd = e["command"]
        out = e["output"]
        print(f"{ts} | {cmd} → {out}")
