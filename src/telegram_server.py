from fastapi import FastAPI, Request
import subprocess
import os
from src.model_router import call_model

app = FastAPI()
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
AUTHORIZED_USER = os.environ.get("AUTHORIZED_USER", "")

@app.post(f"/{BOT_TOKEN}")
async def receive_update(request: Request):
    data = await request.json()
    user = str(data.get("message", {}).get("from", {}).get("id"))
    text = data.get("message", {}).get("text", "")

    if user != AUTHORIZED_USER:
        return {"response": "Unauthorized"}

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous dev AI. Only respond with a command like: run build_readme."},
        {"role": "user", "content": text}
    ]
    command = call_model(prompt).strip().lower()

    if command.startswith("run "):
        mod = command.split(" ")[1]
        subprocess.Popen(["python3", "quasar.py", "run", mod])
        return {"response": f"✅ Running: {mod}"}
    return {"response": f"⚠️ No valid module detected: {command}"}
