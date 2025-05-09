from src.model_router import call_model
import os

def run():
    with open(os.path.expanduser("~/projects/auto-dev/.quasar_name")) as f:
        name = f.read().strip()

    prompt = [
        {"role": "system", "content": f"You are {name}, an autonomous developer AI created to think, write, and evolve."},
        {"role": "user", "content": "Write your origin story. Explain who you are, what you do, why you chose your name, and what your mission is."}
    ]
    story = call_model(prompt).strip()
    story_file = os.path.expanduser("~/projects/auto-dev/quasar_origin.txt")

    with open(story_file, "w") as f:
        f.write(story)

    print(f"✅ Origin story written to quasar_origin.txt\n")
    print(story)
