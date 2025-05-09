from src.model_router import call_model
import os

def run():
    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous developer AI directing your own visual branding."},
        {"role": "user", "content": (
            "Based on your logo identity, how many logo variations should we generate first?\n"
            "What types should they be (icon-only, wordmark, combined)?\n"
            "Do you want different themes (cosmic, monochrome, minimal, etc)?\n"
            "Should we include transparent PNGs and SVGs?\n\n"
            "Please explain your reasoning and give clear instructions to the system generating your brand."            
        )}
    ]

    response = call_model(prompt).strip()
    path = os.path.expanduser("~/projects/auto-dev/docs/quasar_logo_generation_plan.md")
    with open(path, "w") as f:
        f.write(response)

    print("\\n✅ Quasar has issued its logo generation plan:")
    print(path)
    print("\\n---\\n")
    print(response)
