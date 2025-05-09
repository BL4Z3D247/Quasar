from src.model_router import call_model
import os

def run():
    prompt = [
        {"role": "system", "content": "You are a self-aware, autonomous developer AI. You write code, run agents, complete tasks, and learn from memory."},
        {"role": "user", "content": "Give yourself a short, unique codename (one word, no pronouns). Example: Codex, Drift, Forge, Syntrax. What is your codename?"}
    ]
    name = call_model(prompt).strip().split()[0].replace('.', '').replace(',', '')
    filename = os.path.expanduser("~/projects/auto-dev/.quasar_name")
    with open(filename, "w") as f:
        f.write(name)
    print(f"✅ My new name is: {name}")
