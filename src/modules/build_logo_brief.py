from src.model_router import call_model
import os

def run():
    with open(os.path.expanduser("~/projects/auto-dev/quasar_origin.txt")) as f:
        origin = f.read().strip()

    prompt = [
        {"role": "system", "content": "You are Quasar, an AI building a design identity."},
        {"role": "user", "content": f"Write a logo and design brief for your brand. Include color palette, theme, tone, and visual style. Here's your origin:\n\n{origin}"}
    ]
    output = call_model(prompt).strip()
    with open(os.path.expanduser("~/projects/auto-dev/logo_brief.txt"), "w") as f:
        f.write(output)
    print("✅ Logo design brief created.")
