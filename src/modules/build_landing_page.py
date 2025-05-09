from src.model_router import call_model
import os

def run():
    with open(os.path.expanduser("~/projects/auto-dev/quasar_origin.txt")) as f:
        origin = f.read().strip()

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous dev agent building your own brand."},
        {"role": "user", "content": f"Write homepage copy for a landing page about yourself. Include tagline, hero header, intro paragraph, feature blocks, and a call to action. Here's your origin:\n\n{origin}"}
    ]
    output = call_model(prompt).strip()
    with open(os.path.expanduser("~/projects/auto-dev/landing_page_copy.txt"), "w") as f:
        f.write(output)
    print("✅ Landing page copy saved.")
