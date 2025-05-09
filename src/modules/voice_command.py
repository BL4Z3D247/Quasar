import sys
import subprocess
from src.model_router import call_model

def run():
    try:
        cmd_index = sys.argv.index("--cmd")
        voice_input = sys.argv[cmd_index + 1]
    except (ValueError, IndexError):
        print("❌ Voice command missing. Usage: --cmd \\"your instruction\\"")
        return

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous AI developer. Respond only with one of the available commands you know how to execute, based on a user's voice instruction."},
        {"role": "user", "content": f"Voice command: {voice_input}"}
    ]

    result = call_model(prompt).strip().lower()
    print(f"[Quasar] Interpreted command: {result}")
    if result.startswith("run"):
        parts = result.split()
        if len(parts) == 2:
            subprocess.run(["python3", "quasar.py", "run", parts[1]])
        else:
            print("⚠️ Could not parse command properly.")
    else:
        print(f"⚠️ No action taken: {result}")
