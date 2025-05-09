from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.model_router import call_model
from src.module_loader import run_module
from src.supabase_logger import get_client

app = FastAPI()
client = get_client()

class UserMessage(BaseModel):
    message: str

@app.post("/quasar")
async def quasar_interface(data: UserMessage):
    try:
        prompt = [
            {"role": "system", "content": "You are Quasar, an autonomous developer. Respond only with known commands (e.g., run build_readme)."},
            {"role": "user", "content": data.message},
        ]
        response = call_model(prompt).strip().lower()

        # Log message
        client.table("quasar_chatlog").insert({
            "role": "user",
            "content": data.message,
            "tag": "api"
        }).execute()

        if response.startswith("run "):
            module = response.split(" ")[1]
            run_module(module)
            return {"response": f"✅ Executed {module}"}
        else:
            return {"response": f"⚠️ No actionable command: {response}"}

    except Exception as e:
        return {"error": str(e)}
