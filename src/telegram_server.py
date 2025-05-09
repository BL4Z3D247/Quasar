from fastapi import FastAPI, Request
import subprocess
import os
from src.model_router import call_model

app = FastAPI()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
AUTHORIZED_USER = os.getenv("AUTHORIZED_USER", "")

@app.post(f"/{BOT_TOKEN}")
async def handle(request: Request):
    data = await request.json()
    user_id = str(data.get("message", {}).get("from", {}).get("id"))
    text = data.get("message", {}).get("text", "")

    if user_id != AUTHORIZED_USER:
        return {"status": "unauthorized"}

    prompt = [
        {"role": "system", "content": "You are Quasar, an autonomous dev AI. Only reply with valid internal commands like: run build_readme"},
        {"role": "user", "content": text}
    ]
    command = call_model(prompt).strip().lower()
    if command.startswith("run "):
        mod = command.split(" ")[1]
        subprocess.Popen(["python3", "quasar.py", "run", mod])
        return {"status": f"Running module: {mod}"}
    return {"status": f"No runnable module from: {command}"}
