import subprocess
import os
from datetime import datetime
from src.supabase_logger import log_to_supabase
from src.memory import remember

LOG_FILE = "logs/exec.log"

def ensure_log_file():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

def run_command(command: str, safe_mode=False) -> str:
    ensure_log_file()
    print(f"[Quasar] Executing: {command}")
    if safe_mode and any(d in command for d in ["rm", "shutdown", "reboot", ":(){:|:&};:"]):
        confirm = input(f"⚠️  Confirm risky command '{command}' (y/N): ").lower()
        if confirm != 'y':
            remember(prompt=command, response="Cancelled by user", command=command, output="")
            return "❌ Cancelled by user."

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = (result.stdout or result.stderr).strip()
        # Local log
        entry = (
            f"[{datetime.utcnow().isoformat()}] Executing: {command}\n"
            f"[{datetime.utcnow().isoformat()}] Output: {output}\n"
        )
        with open(LOG_FILE, "a") as f:
            f.write(entry)
        # Remote log
        log_to_supabase(command, output)
        # Memory
        remember(prompt=command, response=output, command=command, output=output)
        return f"✅ Command Output:\n{output}"
    except Exception as e:
        err = f"❌ Command Error:\n{e}"
        remember(prompt=command, response=err, command=command, output=err)
        return err
