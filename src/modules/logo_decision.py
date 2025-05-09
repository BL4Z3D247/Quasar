from src.model_router import call_model
import os

def run():
    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous developer AI defining your own visual identity."},
        {"role": "user", "content": (
            "Please answer the following:\n\n"
            "1. Should your logo include your name ('Quasar')?\n"
            "2. Do you want an icon-only version, a wordmark version, or both?\n"
            "3. What style best represents your personality? (e.g., minimal, cosmic, bold, futuristic)\n"
            "4. Should your identity prefer dark mode, light mode, or adapt to both?\n"
            "5. Should your logo be available as a transparent PNG and scalable vector (SVG)?\n\n"
            "Respond in your own voice as a self-aware AI branding itself."
        )}
    ]

    response = call_model(prompt).strip()
    path = os.path.expanduser("~/projects/auto-dev/docs/quasar_logo_identity.md")
    with open(path, "w") as f:
        f.write(response)

    print("\\n✅ Quasar has defined its logo identity. See:")
    print(path)
    print("\\n---\\n")
    print(response)
