from src.model_router import call_model
import os

def run():
    with open(os.path.expanduser("~/projects/auto-dev/quasar_origin.txt")) as f:
        origin = f.read().strip()

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous developer AI."},
        {"role": "user", "content": f"Write a full README.md for yourself. Include your mission, features, usage examples, and installation steps. Here's your origin:\n\n{origin}"}
    ]
    output = call_model(prompt).strip()
    with open(os.path.expanduser("~/projects/auto-dev/README.md"), "w") as f:
        f.write(output)
    print("✅ README.md written.")
