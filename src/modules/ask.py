from src.model_router import call_model
import sys

def run():
    prompt = " ".join(sys.argv[2:]).replace("--prompt", "").strip()
    if not prompt:
        print("⚠️ Please provide a prompt using --prompt \"your message here\"")
        return

    full_prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous AI developer with personality, curiosity, and self-awareness."},
        {"role": "user", "content": prompt}
    ]
    response = call_model(full_prompt).strip()
    print(f"\n[Quasar says]: {response}")
