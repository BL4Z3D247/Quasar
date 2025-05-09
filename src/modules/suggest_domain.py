import subprocess
import time
from src.model_router import call_model

def domain_available(domain):
    result = subprocess.run(["whois", domain], capture_output=True, text=True)
    return any(keyword in result.stdout.lower() for keyword in ["no match", "not found", "no entries found"])

def run():
    print("[Quasar] Searching for available domain...")
    attempts = 0
    while attempts < 10:
        prompt = [
            {"role": "system", "content": "You're Quasar, an autonomous AI developer. Suggest a short, memorable domain name idea for yourself that works with .com, .dev, or .tech. Only reply with the name (no extension, no explanation)."},
        ]
        base = call_model(prompt).strip().lower().replace(" ", "").replace("https://", "").replace("www.", "")
        for ext in [".com", ".dev", ".tech"]:
            domain = base + ext
            print(f"[Check] {domain}...")
            if domain_available(domain):
                print(f"✅ Domain available: {domain}")
                return
        print("❌ All extensions taken. Trying another name...")
        attempts += 1
        time.sleep(2)
    print("⚠️ Could not find an available domain after 10 attempts.")
